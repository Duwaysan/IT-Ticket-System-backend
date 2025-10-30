from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, ProfileSerializer, TicketSerializer
from rest_framework.views import APIView
from .models import Ticket

# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    UserSerializer = UserSerializer
    ProfileSerializer = ProfileSerializer

    def create(self, request, *args, **kwargs):
        try:
            print(request.data, "line 17")
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            profile_data = {
                'nickname': request.data.get('nickname'),
                'user': user.id
            }
            profile_serializer = ProfileSerializer(data=profile_data)
            profile_serializer.is_valid(raise_exception=True)
            profile = profile_serializer.save(user=user)



            refresh = RefreshToken.for_user(user)
            data = {
        	    'refresh': str(refresh),
        	    'access': str(refresh.access_token),
        	    'user': UserSerializer(user).data,
                'profile': ProfileSerializer(profile).data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as err:
            print("line 41", err)
            print(user_serializer.errors, profile_serializer.errors, "line 42")
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class LoginView(APIView):

  def post(self, request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            data = {
        	    'refresh': str(refresh),
        	    'access': str(refresh.access_token),
        	    'user': UserSerializer(user).data,
                'profile': ProfileSerializer(user.profile).data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TicketIndex(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    def get(self, request,profile_id):
        try: 
            #filter tickets if profile ismanager get assigned_to else get created_by
            # print(request.user.profile.is_manager, "line 90")
            # print(profile_id, "line 91")
            queryset = Ticket.objects.filter(assigned_to__id=profile_id) if request.user.profile.is_manager else Ticket.objects.filter(created_by__id=profile_id)
            serializer = TicketSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
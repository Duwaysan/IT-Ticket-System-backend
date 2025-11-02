from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, ProfileSerializer, TicketSerializer
from rest_framework.views import APIView
from .models import Ticket, Profile
from django.shortcuts import get_object_or_404

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
    
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    try:
      user = User.objects.get(username=request.user.username)
      try:
        refresh = RefreshToken.for_user(user)
        data = {
        	    'refresh': str(refresh),
        	    'access': str(refresh.access_token),
        	    'user': UserSerializer(user).data,
                'profile': ProfileSerializer(user.profile).data
            }
        return Response(data, status=status.HTTP_200_OK)
      except Exception as token_error:
        return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class fetchManagers(APIView):

    def get(self, request):
        try:
            queryset = Profile.objects.filter(is_manager=True)
            managers = ProfileSerializer(queryset, many=True)
            return Response(managers.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TicketIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request,profile_id):
        try: 
            queryset = Ticket.objects.filter(assigned_to__id=profile_id) if request.user.profile.is_manager else Ticket.objects.filter(created_by__id=profile_id)
            serializer = TicketSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request, profile_id):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TicketDetail(APIView):
    serializer_class = TicketSerializer
    lookup_field = 'id'

    def get(self, request, ticket_id):
          permission_classes = [permissions.IsAuthenticated]
          try:
              queryset = get_object_or_404(Ticket, id=ticket_id)
              ticket = self.serializer_class(queryset)
              print("retrieved ticket",ticket.data)
              return Response(ticket.data, status=status.HTTP_200_OK)
          except Exception as err:
              return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, ticket_id):
        permission_classes = [permissions.IsAuthenticated]
        try:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            serializer = self.serializer_class(ticket, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, ticket_id):
        permission_classes = [permissions.IsAuthenticated]
        try:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            ticket.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

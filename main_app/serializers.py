from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Ticket,Message
 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'user', "created_at", 'is_manager')

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()
    
    class Meta:
        model = Ticket
        fields = '__all__'

    def get_created_by(self, obj):
        return ProfileSerializer(obj.created_by).data if obj.created_by else None

    def get_assigned_to(self, obj):
        return ProfileSerializer(obj.assigned_to).data if obj.assigned_to else None
    
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = '__all__'

    def get_sender(self,obj):
        return ProfileSerializer(obj.profile).data if obj.profile else None
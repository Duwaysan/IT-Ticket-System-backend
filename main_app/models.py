from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    nickname = models.CharField(max_length=50)
    is_manager = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile' )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Profile: {self.nickname} (Manager: {self.is_manager})"
    
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tickets_created')
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tickets_assigned')

    def __str__(self):
        return f"Ticket: {self.title} (Resolved: {self.is_resolved})"
    
    class Meta:
        ordering = ['-created_at']
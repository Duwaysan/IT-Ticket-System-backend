from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('profiles/signup/', CreateUserView.as_view(), name='signup'),
]
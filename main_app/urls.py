from django.urls import path
from .views import CreateUserView, LoginView, TicketIndex

urlpatterns = [
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('profiles/<int:profile_id>/tickets/', TicketIndex.as_view(), name='ticket-index'),

]
from django.urls import path
from .views import CreateUserView, LoginView, TicketIndex, VerifyUserView

urlpatterns = [
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('profiles/<int:profile_id>/tickets/', TicketIndex.as_view(), name='ticket-index'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),

]
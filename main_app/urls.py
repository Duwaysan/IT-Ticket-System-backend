from django.urls import path
from .views import CreateUserView, LoginView, VerifyUserView
from .views import TicketIndex, TicketDetail

urlpatterns = [
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('profiles/<int:profile_id>/tickets/', TicketIndex.as_view(), name='ticket-index'),
    path('tickets/<int:ticket_id>/', TicketDetail.as_view(), name='ticket-detail'),

]
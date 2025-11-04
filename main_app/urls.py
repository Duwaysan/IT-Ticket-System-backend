from django.urls import path
from .views import CreateUserView, LoginView, VerifyUserView, fetchManagers
from .views import TicketIndex, TicketDetail
from .views import MessagesIndex
urlpatterns = [
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('users/managers/', fetchManagers.as_view(), name='managers'),
    path('profiles/<int:profile_id>/tickets/', TicketIndex.as_view(), name='ticket-index'),
    path('tickets/<int:ticket_id>/', TicketDetail.as_view(), name='ticket-detail'),
    path('tickets/<int:ticket_id>/messages/', MessagesIndex.as_view(), name='message-index'),
    path('tickets/<int:ticket_id>/messages/<int:message_id>/', MessagesIndex.as_view(), name='message-index'),

]
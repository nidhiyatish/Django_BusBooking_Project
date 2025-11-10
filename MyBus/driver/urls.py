
from django.urls import path
from .views import ViewDriver,AddDriver,EditDriver,RemoveDriver



urlpatterns = [
    path('', ViewDriver.as_view(), name='view_drivers'),
    path('add/', AddDriver.as_view(), name = 'add_driver'),
    
    path('edit/<int:pk>/',EditDriver.as_view(), name='edit_driver'),
    path('del/<int:pk>/', RemoveDriver.as_view(), name='del_driver'),

    
]
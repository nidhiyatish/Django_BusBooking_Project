from django.urls import path
from .views import ViewStop,AddStop,EditStop,RemoveStop



urlpatterns = [
    path('', ViewStop.as_view(), name='view_stops'),
    path('add/', AddStop.as_view(), name = 'add_stop'),
    
    path('edit/<int:pk>/',EditStop.as_view(), name='edit_stop'),
    path('del/<int:pk>/', RemoveStop.as_view(), name='del_stop'),

    
]
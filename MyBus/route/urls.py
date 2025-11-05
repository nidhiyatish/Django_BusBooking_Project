from django.urls import path
from .views import ViewRoute,AddRoute,EditRoute,RemoveRoute



urlpatterns = [
    path('', ViewRoute.as_view(), name='view_routes'),
    path('add/', AddRoute.as_view(), name = 'add_route'),
    
    path('edit/<int:pk>/',EditRoute.as_view(), name='edit_route'),
    path('del/<int:pk>/', RemoveRoute.as_view(), name='del_route'),

]
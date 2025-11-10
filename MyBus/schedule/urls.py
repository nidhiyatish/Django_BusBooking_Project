from django.urls import path
from .views import ViewSchedule,AddSchedule,EditSchedule,RemoveSchedule


from .views import ajax_search_schedules


urlpatterns = [
    path('', ViewSchedule.as_view(), name='view_schedules'),
    path('add/', AddSchedule.as_view(), name = 'add_schedule'),
    
    path('edit/<int:pk>/',EditSchedule.as_view(), name='edit_schedule'),
    path('del/<int:pk>/', RemoveSchedule.as_view(), name='del_schedule'),

    path('ajax/search-schedules/', ajax_search_schedules, name='ajax_search_schedules'),

    
]
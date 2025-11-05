from django.urls import path
from .views import ViewBuses,AddBus, BusDetail,EditBus,RemoveBus

from .views import UpdateBusImage, DelBusImage

urlpatterns = [
    path('', ViewBuses.as_view(), name='view_buses'),
    path('add/', AddBus.as_view(), name = 'add_bus'),
    path('<int:pk>/', BusDetail.as_view(), name= 'bus_details'),
    path('edit/<int:pk>/',EditBus.as_view(), name='edit_bus'),
    path('del/<int:pk>/', RemoveBus.as_view(), name='del_bus'),

    # bus image
    path('bus/image/edit/<int:pk>', UpdateBusImage.as_view(), name='edit_bus_image'),
    path('bus/image/del/<int:pk>', DelBusImage.as_view(), name='del_bus_image'),
]
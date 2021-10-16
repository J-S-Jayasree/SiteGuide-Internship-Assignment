from django.urls import path

from . import views

urlpatterns = [
    path('', views.VehicleList.as_view(), name='vehicle_list'),
    path('view/<int:pk>', views.VehicleView.as_view(), name='vehicle_view'),
    path('new', views.VehicleCreate.as_view(), name='vehicle_new'),
    path('view/<int:pk>', views.VehicleView.as_view(), name='vehicle_view'),
    path('edit/<int:pk>', views.VehicleUpdate.as_view(), name='vehicle_edit'),
    path('delete/<int:pk>', views.VehicleDelete.as_view(), name='vehicle_delete'),
]

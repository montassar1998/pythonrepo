from django.urls import path
from .views import DepCreate, DepDeleteView, DepUpdateView, DepView
app_name = "GestionDepartement"
urlpatterns = [
    path('list', DepView.as_view(), name='listhtml'),
    path('create', DepCreate.as_view(), name='createhtml'),
    path('update/<int:pk>', DepUpdateView.as_view(), name='updatehtml'),
    path('delete/<int:pk>', DepDeleteView.as_view(), name='deletehtml'), ]

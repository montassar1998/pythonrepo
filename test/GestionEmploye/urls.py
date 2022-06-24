from django.urls import path
from .views import EmpCreate, EmpDeleteView, EmpUpdateView, EmpView
app_name = "GestionEmploye"
urlpatterns = [
    path('list', EmpView.as_view(), name='listhtml'),
    path('create', EmpCreate.as_view(), name='createhtml'),
    path('update/<int:pk>', EmpUpdateView.as_view(), name='updatehtml'),
    path('delete/<int:pk>', EmpDeleteView.as_view(), name='deletehtml'), ]

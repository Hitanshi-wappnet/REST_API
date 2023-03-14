from django.urls import path
from employee import views

# Provided URL of Class based Views.
urlpatterns = [
    path('emp/', views.EmployeeView.as_view(), name='emp'),
    path('emp/<int:pk>/', views.EmployeeView.as_view(), name='emp')
]

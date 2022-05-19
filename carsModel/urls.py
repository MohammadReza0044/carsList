from django.urls import path
from carsModel.views import carList , car_details 

urlpatterns = [
    path ('',carList.as_view()),
    path ('<int:pk>/',car_details.as_view()),

    
]

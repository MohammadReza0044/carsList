from django.urls import path

from .views import personView, person_detailView

urlpatterns = [
    path('', personView.as_view()),
    path('<int:pk>/', person_detailView.as_view()),
    
    
]

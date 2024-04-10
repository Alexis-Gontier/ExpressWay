from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show/<id_train>', views.show_id, name="show_id"),
    path('aleatoir/', views.aleatoir, name="aleatoir"),
    path('addTrain/', views.addTrain, name="addTrain"),
]
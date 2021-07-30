from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addperson/<int:FamilyID>/', views.addPerson, name="add_person"),
    path('ajax/load-qualification/',views.load_qualification,name='ajax_load_qualification'),
]

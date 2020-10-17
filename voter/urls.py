from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('db/<int:pk>/',views.view_candidates,name="view_candidates"),
]
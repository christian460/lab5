from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.form_add_productos, name="productos"),
]
from django.urls import path
from forms_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form_page/', views.form_page_view, name="form_page")
]
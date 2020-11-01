from django.urls import path
from users_app import views

# TEMPLATE TAGGING
app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name="register")

]

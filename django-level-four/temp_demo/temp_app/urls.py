from django.urls import path
from . import views


# Template Tagging
app_name = "temp_app"

urlpatterns = [
    path('other/', views.other, name="other"),
    path('relative/', views.relative, name="relative")
]
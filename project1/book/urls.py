from django.urls import path
from . import views

urlpatterns = [
    path('by/',views.say_by)
]

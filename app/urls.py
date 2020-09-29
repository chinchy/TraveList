from django.contrib import admin
from django.urls import path, include
from app.views import *

app_name = 'TraveList'
urlpatterns = [
    path('object/create/', ObjectCreateView.as_view()),
    path('object/all/', ObjectListView.as_view()),
]

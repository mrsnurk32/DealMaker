from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles
from datetime import date
import re
today = date.today()
urlpatterns = [
    path('', views.index, name = "index"),
    path('daily/', ListView.as_view(queryset=Articles.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day), template_name="mainApp/daily_news.html")),
]

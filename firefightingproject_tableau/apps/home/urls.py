# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('situations.html', views.fire_status_chart),
    path('chartjs1.html', views.wind_velocity_factors),
    path('chartjs2.html', views.humidity_factors),
    path('chartjs3.html', views.temperature_factors),
    path('fire_type', views.select_fire_type),
    path('index.html', views.fire_fighting_main),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

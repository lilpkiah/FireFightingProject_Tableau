# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
    
class dw_fire_fighter(models.Model):
    occupation = models.CharField(null=False, max_length=50)
    occupation_code = models.CharField(null=False, max_length=50)
    position = models.CharField(null=False, max_length=50)
    position_code = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    fire_station = models.CharField(null=False, max_length=50)
    fire_station_code = models.CharField(null=False, max_length=50)
    cnt_of_officers = models.IntegerField(null=False)
    

class dw_fire_fighting(models.Model):
    fire_date = models.CharField(null=False, max_length=50)
    city = models.CharField(null=False, max_length=50)
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    fire_type = models.CharField(null=False, max_length=50)
    type_code = models.CharField(null=False, max_length=50)
    fire_source = models.CharField(null=False, max_length=50)
    fire_source_code = models.CharField(null=False, max_length=50)
    fire_factor = models.CharField(null=False, max_length=50)
    fire_factor_code = models.CharField(null=False, max_length=50)
    casualties = models.IntegerField(null=False)
    dead = models.IntegerField(null=False)
    injury = models.IntegerField(null=False)
    property_damage = models.IntegerField(null=False)
    place = models.CharField(null=False, max_length=50)
    place_code = models.CharField(null=False, max_length=50)
    
    
class dw_house(models.Model):
    city = models.CharField(null=False, max_length=50)
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    town = models.CharField(null=False, max_length=50)
    town_code = models.CharField(null=False, max_length=50)
    sum = models.IntegerField(null=False)
    house = models.IntegerField(null=False)
    apartment = models.IntegerField(null=False)
    

class dw_humidity(models.Model):
    city = models.CharField(null=False, max_length=50)
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    humidity_date = models.CharField(null=False, max_length=50)
    avg_humidity = models.IntegerField(null=False)
    min_humidity = models.IntegerField(null=False)
    max_humidity = models.IntegerField(null=False)
    

class dw_wind_velocity(models.Model):
    city = models.CharField(null=False, max_length=50)
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    wind_velocity_date = models.CharField(null=False, max_length=50)
    avg_wind_velocity = models.IntegerField(null=False)
    min_wind_velocity = models.IntegerField(null=False)
    max_wind_velocity = models.IntegerField(null=False)
    

class dw_temperature(models.Model):
    city = models.CharField(null=False, max_length=50)
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    temperature_date = models.CharField(null=False, max_length=50)
    avg_temperature = models.IntegerField(null=False)
    min_temperature = models.IntegerField(null=False)
    max_temperature = models.IntegerField(null=False)
    
    
class dw_public_facilites(models.Model):
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    town = models.CharField(null=False, max_length=50)
    town_code = models.CharField(null=False, max_length=50)
    public_cnt = models.IntegerField(null=False)
    cultural_facility = models.IntegerField(null=False)
    religious_establishment = models.IntegerField(null=False)
    medical_facility = models.IntegerField(null=False)
    education_research_facility = models.IntegerField(null=False)
    elderly_facility = models.IntegerField(null=False)
    training_facility = models.IntegerField(null=False)
    exercise_facility = models.IntegerField(null=False)
    cemetery_related_facilities = models.IntegerField(null=False)
    tourist_rest_facilities = models.IntegerField(null=False)
    funeral_facility = models.IntegerField(null=False)
    other_facilites = models.IntegerField(null=False)
    
class dw_commerce(models.Model):
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    town = models.CharField(null=False, max_length=50)
    town_code = models.CharField(null=False, max_length=50)
    convenience = models.IntegerField(null=False)
    c1_living_facility = models.IntegerField(null=False)
    c2_living_facility = models.IntegerField(null=False)
    sales_facility = models.IntegerField(null=False)
    transportation_facility = models.IntegerField(null=False)
    business_facilites = models.IntegerField(null=False)
    accommodation_facility = models.IntegerField(null=False)
    amusement_facility = models.IntegerField(null=False)
    dst_facility = models.IntegerField(null=False)
    automobile_facility = models.IntegerField(null=False)
    etc = models.IntegerField(null=False)
    
    
class dw_merge_inner(models.Model):
    district = models.CharField(null=False, max_length=50)
    district_code = models.CharField(null=False, max_length=50)
    town = models.CharField(null=False, max_length=50)
    town_code = models.CharField(null=False, max_length=50)
    convenience = models.IntegerField(null=False)
    c1_living_facility = models.IntegerField(null=False)
    c2_living_facility = models.IntegerField(null=False)
    sales_facility = models.IntegerField(null=False)
    transportation_facility = models.IntegerField(null=False)
    business_facilites = models.IntegerField(null=False)
    accommodation_facility = models.IntegerField(null=False)
    amusement_facility = models.IntegerField(null=False)
    dst_facility = models.IntegerField(null=False)
    automobile_facility = models.IntegerField(null=False)
    etc = models.IntegerField(null=False)
    cultural_facility = models.IntegerField(null=False)
    religious_establishment = models.IntegerField(null=False)
    medical_facility = models.IntegerField(null=False)
    education_research_facility = models.IntegerField(null=False)
    elderly_facility = models.IntegerField(null=False)
    training_facility = models.IntegerField(null=False)
    exercise_facility = models.IntegerField(null=False)
    cemetery_related_facilities = models.IntegerField(null=False)
    tourist_rest_facilities = models.IntegerField(null=False)
    funeral_facility = models.IntegerField(null=False)
    house = models.IntegerField(null=False)
    apartment = models.IntegerField(null=False)
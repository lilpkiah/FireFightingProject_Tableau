# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home import bigdataPro
import pandas as pd
from apps.home.models import dw_fire_fighting, dw_humidity, dw_wind_velocity,\
    dw_temperature, dw_commerce, dw_merge_inner
from django.shortcuts import render, redirect
import os
import folium
import json
from core.settings import STATIC_DIR

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



def fire_status_chart(request):
    fire_date=dw_fire_fighting.objects.values('fire_date')
    m_property_damage=dw_fire_fighting.objects.values('property_damage')
    factor0 = pd.DataFrame(fire_date)
    factor1 = pd.DataFrame(m_property_damage)
    factor5 = pd.DataFrame({
        'fire_date':factor0['fire_date'],
        'property_damage':factor1['property_damage']
        })
    
    # ??? ??????
    month = []
    for m in factor5['fire_date']:
        if m not in month:
            month.append(m)
    # ??? ????????????        
    monthsum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ms = m['fire_date'].count()
        monthsum.append(ms)
        
    # ??? ????????????
    m_damagesum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ds = m['property_damage'].sum()
        m_damagesum.append(ds)
        
    month_df = pd.DataFrame({
        'fire_date':month,
        'occur_cnt':monthsum
        })

    # ?????? ????????????
    month_damage_df = pd.DataFrame({
        'fire_date' : month,
        'property_damage_sum_k' : m_damagesum
        })
    
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????

    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })
    
    
    de=dw_fire_fighting.objects.values('dead')
    dead = pd.DataFrame(de)
    dead_sum = dead['dead'].sum()
    inju=dw_fire_fighting.objects.values('injury')
    injury = pd.DataFrame(inju)
    injury_sum = injury['injury'].sum()
    
    damage_people = ['?????????', '?????????']
    damage_sum = [dead_sum, injury_sum]
    
    dp = pd.DataFrame({
        'damage_people':damage_people,
        'damage_sum':damage_sum
        })
    

    type=dw_fire_fighting.objects.values('fire_type')
    source=dw_fire_fighting.objects.values('fire_source')
    firefactor=dw_fire_fighting.objects.values('fire_factor')
    
    firetype = pd.DataFrame(type)
    firesource = pd.DataFrame(source)
    firefactor = pd.DataFrame(firefactor)
    
    # ????????????
    fire_type = []
    for t in firetype['fire_type']:
        if t not in fire_type:
            fire_type.append(t)
    
    type_sum = []
    for t in range(len(fire_type)):
        ft = firetype[firetype.fire_type == fire_type[t]]
        fts = ft['fire_type'].count()
        type_sum.append(fts)
    
    # ????????????
    fire_source = []
    for s in firesource['fire_source']:
        if s not in fire_source:
            fire_source.append(s)
            
    source_sum = []
    for s in range(len(fire_source)):
        fs = firesource[firesource.fire_source == fire_source[s]]
        fss = fs['fire_source'].count()
        source_sum.append(fss)
    
    # ????????????
    fire_factor = []
    for f in firefactor['fire_factor']:
        if f not in fire_factor:
            fire_factor.append(f)
    
    factor_sum = []
    for f in range(len(fire_factor)):
        ff = firefactor[firefactor.fire_factor == fire_factor[f]]
        ffs = ff['fire_factor'].count()
        factor_sum.append(ffs)
        
    type_df = pd.DataFrame({
    'fire_type':fire_type,
    'type_sum':type_sum
    })

    source_df = pd.DataFrame({
    'fire_source':fire_source,
    'source_sum':source_sum
    })

    factor_df = pd.DataFrame({
    'fire_factor':fire_factor,
    'factor_sum':factor_sum
    })


    bigdataPro.dead_injury_makeGraph(dp['damage_people'], dp['damage_sum'])
    bigdataPro.cause1(type_df['fire_type'], type_df['type_sum'])
    bigdataPro.cause2(source_df['fire_source'], source_df['source_sum'])
    bigdataPro.cause3(factor_df['fire_factor'], factor_df['factor_sum'])
    bigdataPro.month_cnt_makeGraph(month_df['fire_date'], month_df['occur_cnt'])
    bigdataPro.month_damage_makeGraph(month_damage_df['fire_date'], month_damage_df['property_damage_sum_k'])
    bigdataPro.district_cnt_makeGraph(district_df['district'], district_df['occur_cnt'])
    bigdataPro.district_damage_makeGraph(d_damage_df['district'], d_damage_df['district_property_damage_k'])
    
    
    return render(request, 'home/situations.html') 


# ????????????
def humidity_factors(request):
    fire_date=dw_fire_fighting.objects.values('fire_date')
    m_property_damage=dw_fire_fighting.objects.values('property_damage')
    factor0 = pd.DataFrame(fire_date)
    factor1 = pd.DataFrame(m_property_damage)
    factor5 = pd.DataFrame({
        'fire_date':factor0['fire_date'],
        'property_damage':factor1['property_damage']
        })
    
    # ??? ??????
    month = []
    for m in factor5['fire_date']:
        if m not in month:
            month.append(m)
    # ??? ????????????        
    monthsum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ms = m['fire_date'].count()
        monthsum.append(ms)
        
    # ??? ????????????
    m_damagesum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ds = m['property_damage'].sum()
        m_damagesum.append(ds)
        
    month_df = pd.DataFrame({
        'fire_date':month,
        'occur_cnt':monthsum
        })
    
    # ?????? ????????????
    month_damage_df = pd.DataFrame({
        'fire_date' : month,
        'property_damage_sum_k' : m_damagesum
        })
    
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????
    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })
    
    # ????????????, ??????, ??????
    h=pd.DataFrame(dw_humidity.objects.values('avg_humidity'))
    hd=pd.DataFrame(dw_humidity.objects.values('district'))
    hdd=pd.DataFrame(dw_humidity.objects.values('humidity_date'))
    
    humidity = pd.DataFrame({
        'district':hd['district'],
        'humidity_date':hdd['humidity_date'],
        'avg_humidity':h['avg_humidity']})
    
    # d_avg
    avg_humidity = []
    for i in range(len(district)):
        d = humidity[humidity.district == district[i]]   
        ds = d['avg_humidity'].sum()
        dss = ds / 12
        avg_humidity.append(dss)
    
    
    # m_avg
    avg_humidity_m = []
    for i in range(len(month)):
        d = humidity[humidity.humidity_date == month[i]]   
        ds = d['avg_humidity'].sum()
        dss = ds / 12
        avg_humidity_m.append(dss)
    
    
    bigdataPro.humidity_month_cnt(month, avg_humidity_m, month_df['occur_cnt'])
    bigdataPro.humidity_district_cnt(district, avg_humidity, district_df['occur_cnt'])
    bigdataPro.humidity_month_damage(month, avg_humidity_m, month_damage_df['property_damage_sum_k'])
    bigdataPro.humidity_district_damage(district, avg_humidity, d_damage_df['district_property_damage_k'])
    
    return render(request, 'home/chartjs2.html')


# ?????? ??????
def wind_velocity_factors(request):
    fire_date=dw_fire_fighting.objects.values('fire_date')
    m_property_damage=dw_fire_fighting.objects.values('property_damage')
    factor0 = pd.DataFrame(fire_date)
    factor1 = pd.DataFrame(m_property_damage)
    factor5 = pd.DataFrame({
        'fire_date':factor0['fire_date'],
        'property_damage':factor1['property_damage']
        })
    
    # ??? ??????
    month = []
    for m in factor5['fire_date']:
        if m not in month:
            month.append(m)
    # ??? ????????????        
    monthsum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ms = m['fire_date'].count()
        monthsum.append(ms)
        
    # ??? ????????????
    m_damagesum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ds = m['property_damage'].sum()
        m_damagesum.append(ds)
        
    month_df = pd.DataFrame({
        'fire_date':month,
        'occur_cnt':monthsum
        })
    
    # ?????? ????????????
    month_damage_df = pd.DataFrame({
        'fire_date' : month,
        'property_damage_sum_k' : m_damagesum
        })
    
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????
    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })    
    
    wind_velocity=pd.DataFrame(dw_wind_velocity.objects.values('avg_wind_velocity'))
    wvd=pd.DataFrame(dw_wind_velocity.objects.values('district'))
    wvdd=pd.DataFrame(dw_wind_velocity.objects.values('wind_velocity_date'))
    
    wv=pd.DataFrame({
        'district':wvd['district'],
        'wind_velocity_date':wvdd['wind_velocity_date'],
        'avg_wind_velocity':wind_velocity['avg_wind_velocity']})
    
    # d_avg
    avg_wind_velocity = []
    for i in range(len(district)):
        d = wv[wv.district == district[i]]   
        ds = d['avg_wind_velocity'].sum()
        dss = ds / 12
        avg_wind_velocity.append(dss)
        
    # m_avg
    avg_wind_velocity_m = []
    for i in range(len(month)):
        d = wv[wv.wind_velocity_date == month[i]]   
        ds = d['avg_wind_velocity'].sum()
        dss = ds / 12
        avg_wind_velocity_m.append(dss)
        
    
    bigdataPro.wind_velocity_month_cnt(month,avg_wind_velocity_m, month_df['occur_cnt'])
    bigdataPro.wind_velocity_district_cnt(district, avg_wind_velocity, district_df['occur_cnt'])    
    bigdataPro.wind_velocity_month_damage(month, avg_wind_velocity_m, month_damage_df['property_damage_sum_k'])
    bigdataPro.wind_velocity_district_damage(district, avg_wind_velocity, d_damage_df['district_property_damage_k'])
    

    return render(request, 'home/chartjs1.html')
    

# ?????? ??????
def temperature_factors(request):
    fire_date=dw_fire_fighting.objects.values('fire_date')
    m_property_damage=dw_fire_fighting.objects.values('property_damage')
    factor0 = pd.DataFrame(fire_date)
    factor1 = pd.DataFrame(m_property_damage)
    factor5 = pd.DataFrame({
        'fire_date':factor0['fire_date'],
        'property_damage':factor1['property_damage']
        })
    
    # ??? ??????
    month = []
    for m in factor5['fire_date']:
        if m not in month:
            month.append(m)
    # ??? ????????????        
    monthsum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ms = m['fire_date'].count()
        monthsum.append(ms)
        
    # ??? ????????????
    m_damagesum = []
    for i in range(len(month)):
        m = factor5[factor5.fire_date == month[i]]
        ds = m['property_damage'].sum()
        m_damagesum.append(ds)
        
    month_df = pd.DataFrame({
        'fire_date':month,
        'occur_cnt':monthsum
        })
    
    # ?????? ????????????
    month_damage_df = pd.DataFrame({
        'fire_date' : month,
        'property_damage_sum_k' : m_damagesum
        })
    
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????
    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })        
    
    
    t=pd.DataFrame(dw_temperature.objects.values('avg_temperature'))
    td=pd.DataFrame(dw_temperature.objects.values('district'))
    tdd=pd.DataFrame(dw_temperature.objects.values('temperature_date'))
    
    temperature=pd.DataFrame({
        'district':td['district'],
        'temperature_date':tdd['temperature_date'],
        'avg_temperature':t['avg_temperature']})
    
    # d_avg
    avg_temperature = []
    for i in range(len(district)):
        d = temperature[temperature.district == district[i]]   
        ds = d['avg_temperature'].sum()
        dss = ds / 12
        avg_temperature.append(dss)
    
    # m_avg
    avg_temperature_m = []
    for i in range(len(month)):
        d = temperature[temperature.temperature_date == month[i]]   
        ds = d['avg_temperature'].sum()
        dss = ds / 12
        avg_temperature_m.append(dss)
        
    
    bigdataPro.temperature_month_cnt(month, avg_temperature_m, month_df['occur_cnt'])
    bigdataPro.temperature_district_cnt(district, avg_temperature, district_df['occur_cnt'])
    bigdataPro.temperature_month_damage(month, avg_temperature_m, month_damage_df['property_damage_sum_k'])
    bigdataPro.temperature_district_damage(district, avg_temperature, d_damage_df['district_property_damage_k'])

    return render(request, 'home/chartjs3.html')


def select_fire_type(request):
    
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    place=pd.DataFrame(dw_fire_fighting.objects.values('place'))
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage'],
        'place':place['place']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????
    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })        
    
    # ????????????
    '''
    merge_inner = pd.DataFrame(list(dw_merge_inner.objects.all().values()))
    
    merge_inner = merge_inner.rename(columns={'convenience':'??????????????????',
                                   'c1_living_facility':'???1?????????????????????',
                                   'c2_living_facility':'???2?????????????????????',
                                   'sales_facility':'????????????',
                                   'transportation_facility':'????????????',
                                   'business_facilites':'????????????',
                                   'accommodation_facility':'????????????',
                                   'amusement_facility':'????????????',
                                   'DST_facility':'??????????????????????????????',
                                   'automobile_facility':'?????????????????????',
                                   'etc':'??????',
                                   'cultural_facility':'?????????????????????',
                               'religious_establishment':'????????????',
                               'medical_facility':'????????????',
                               'Education and Research Facility':'??????????????????',
                               'elderly_facility':'???????????????',
                               'training_facility':'????????????',
                               'exercise_facility':'????????????',
                               'cemetery_related_facilities':'??????????????????',
                               'tourist_rest_facilities':'??????????????????',
                                'funeral_facility':'????????????',
                                'house':'????????????',
                                'apartment':'????????????'})
    '''
    
    place1 = request.GET['place']
    if place1 == None:
        place1 = '????????????'
    
  
    
        
    bigdataPro.place_district_map(factor4, district, place1)
    
    
    # ????????? ??? ?????? ??????
    fire_place = []
    for p in factor4['place']:
        if p not in fire_place:
            fire_place.append(p)
    
    # ???????????? ????????????
    fire_place_sum = []
    for p in range(len(fire_place)):
        pp = factor4[factor4.place == fire_place[p]]
        pps = pp['place'].count()
        fire_place_sum.append(pps)
    
    # ???????????? ?????????
    fire_place_damage_sum = []
    for p in range(len(fire_place)):
        pp = factor4[factor4.place == fire_place[p]]
        pps = pp['property_damage'].sum()
        fire_place_damage_sum.append(pps)
    
    bigdataPro.place_percent_cnt(fire_place, fire_place_sum, fire_place_damage_sum, place1)
    bigdataPro.place_percent_damage(fire_place, fire_place_sum, fire_place_damage_sum, place1)
    
    bigdataPro.place_district_sum(district, factor4, place1)
    bigdataPro.place_district_sum_map(district, factor4, place1)
    bigdataPro.place_district_damage_sum_map(district, factor4, place1)
    
    
    return render(request, 'home/fire_type.html', {'place': place1})    
    
    
    
    
def fire_fighting_main(request):
    district=dw_fire_fighting.objects.values('district')
    property_damage=dw_fire_fighting.objects.values('property_damage')
    place=pd.DataFrame(dw_fire_fighting.objects.values('place'))
    factor2 = pd.DataFrame(district)
    factor3 = pd.DataFrame(property_damage)
    factor4 = pd.DataFrame({
        'district':factor2['district'],
        'property_damage':factor3['property_damage'],
        'place':place['place']
        })
    
    district = [] # ???
    for c in factor4['district']:
        if c not in district:
            district.append(c)
            
            
    district_sum = [] # ??? ????????????
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]   
        ds = d['district'].count()
        district_sum.append(ds)
        
     # ??? ????????????
    d_damage_sum = []
    for i in range(len(district)):
        d = factor4[factor4.district == district[i]]
        ds = d['property_damage'].sum()
        d_damage_sum.append(ds)

        
    district_df = pd.DataFrame({
        'district': district,
        'occur_cnt' : district_sum
         })
    
    d_damage_df = pd.DataFrame({
    'district': district,
    'district_property_damage_k': d_damage_sum
    })        
    
    
    bigdataPro.main_district_cnt(district_df)
    
    return render(request, 'home/index.html')


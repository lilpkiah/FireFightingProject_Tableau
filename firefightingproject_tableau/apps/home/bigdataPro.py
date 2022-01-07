# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import folium
import json

#from core.settings import STATICFILES_DIRS
from core.settings import STATIC_DIR, TEMPLATE_DIR

from matplotlib import font_manager, rc
# Create your tests here.

def month_cnt_makeGraph(v1, v2):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.figure()
    plt.rc('font', size=12)
    plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
    # 월별 화재건수
    plt.xticks(rotation = 30)
    plt.ylabel('화재발생 건수')
    #plt.grid(True)
    plt.bar(v1, v2, color='#A1C9F4')
    for i, v in enumerate(v1):
        plt.text(v, v2[i], str(v2[i]),
                 fontsize=11,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig01.png'), dpi=300)
    
    
def district_cnt_makeGraph(v3, v4):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.figure()
    plt.rc('font', size=12)
    plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
    # 월별 화재건수
    plt.xticks(rotation = 30)
    plt.ylabel('화재발생 건수')
    #plt.grid(True)
    plt.bar(v3, v4, color='#A1C9F4')
    for i, v in enumerate(v3):
        plt.text(v, v4[i], str(v4[i]),
                 fontsize=11,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig02.png'), dpi=300)
    
def month_damage_makeGraph(v5, v6):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.figure()
    plt.rc('font', size=12)
    plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
    # 월별 화재건수
    plt.xticks(rotation = 30)
    plt.ylabel('화재발생 피해규모')
    #plt.grid(True)
    plt.bar(v5, v6, color='#A1C9F4')
    for i, v in enumerate(v5):
        plt.text(v, v6[i], str(v6[i]),
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    #plt.title('월별 피해규모', fontsize=20)
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig03.png'), dpi=300)
    
    
    
def district_damage_makeGraph(v7, v8):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.figure()
    plt.rc('font', size=12)
    plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
    # 월별 화재건수
    plt.xticks(rotation = 30)
    plt.ylabel('화재발생 피해규모')
    #plt.grid(True)
    plt.bar(v7, v8, color='#A1C9F4')
    for i, v in enumerate(v7):
        plt.text(v, v8[i], str(v8[i]),
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    #plt.title('지역별 피해규모', fontsize=20)
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig04.png'), dpi=300)
    
    
def dead_injury_makeGraph(v9, v10):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5}
    pie_colors = ['#ff9999', '#A1C9F4']
    damage_people = ['사망자', '부상자']
    plt.figure()
    
    plt.rc('font', size=20)
    plt.rc('xtick', labelsize=13)
    plt.pie(v10, autopct='%.2f%%', startangle=250, counterclock=False, labels=damage_people, wedgeprops=wedgeprops, colors=pie_colors)
    plt.title('부산광역시 인명피해 규모', fontsize=20)
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig05.png'), dpi=300)
    
    
def cause1(c1, c2):
    #fig, axes = plt.subplots(1, 3, figsize=(64,20))

    #plt.rc('xtick', labelsize=40)
    #plt.rc('ytick', labelsize=30)
    #axes[0].bar(c1, c2)
    #axes[0].set_xticklabels(c1, rotation=35)
    #axes[1].bar(c3, c4)
    #axes[1].set_xticklabels(c3, rotation=35)
    #axes[2].bar(c5, c6)
    #axes[2].set_xticklabels(c5, rotation=35)
    #plt.savefig(os.path.join(STATIC_DIR, 'images/fig06.png'), dpi=300)
    
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.figure()
    plt.bar(c1, c2, color='#A1C9F4')
    plt.xticks(rotation = 20)
    
    for i, v in enumerate(c1):
        plt.text(v, c2[i], str(c2[i]),
            fontsize=9,
            color='black',
            horizontalalignment='center',
            verticalalignment='bottom')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig06.png'), dpi=300)

        
def cause2(c3, c4):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.figure()
    plt.bar(c3, c4, color='#A1C9F4')
    plt.xticks(rotation = 20)
    
    for i, v in enumerate(c3):
        plt.text(v, c4[i], str(c4[i]),
            fontsize=9,
            color='black',
            horizontalalignment='center',
            verticalalignment='bottom')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig07.png'), dpi=400)    
    
    
def cause3(c5, c6):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.figure()
    plt.bar(c5, c6, color='#A1C9F4')
    plt.xticks(rotation = 20)
    
    for i, v in enumerate(c5):
        plt.text(v, c6[i], str(c6[i]),
            fontsize=9,
            color='black',
            horizontalalignment='center',
            verticalalignment='bottom')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig08.png'), dpi=300)
    
 
# 평균 습도    
def humidity_month_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 습도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig09.png'), dpi=300)
    
    
def humidity_district_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 습도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig10.png'), dpi=300)    
    

def humidity_month_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 습도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig11.png'), dpi=300)
    
    
def humidity_district_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 습도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig12.png'), dpi=300)        
   
    
   
# 평균 풍속
def wind_velocity_month_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 풍속', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig13.png'), dpi=300)
    
    
def wind_velocity_district_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 풍속', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig14.png'), dpi=300)    
    

def wind_velocity_month_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 풍속', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig15.png'), dpi=300)
    
    
def wind_velocity_district_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 풍속', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig16.png'), dpi=300)        
      
      
      
# 평균 온도
def temperature_month_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 온도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig17.png'), dpi=300)
    
    
def temperature_district_cnt(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 온도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='화재건수', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig18.png'), dpi=300)    
    

def temperature_month_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 온도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig19.png'), dpi=300)
    
    
def temperature_district_damage(h1, h2, h3):
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.rc('font', size=12)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(h1, h2, color='green', markersize=4, linewidth=1, alpha=0.7, label='평균 온도', marker='o')
    for i, v in enumerate(h1):
        plt.text(v, h2[i], str('%.2f'%float(h2[i])),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax2 = ax1.twinx()
    ax2.bar(h1, h3, color='#92b8b1', label='피해규모', alpha=0.7, width=0.7)
    for i, v in enumerate(h1):
        plt.text(v, h3[i], str(h3[i]),
                fontsize=8,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
        
    ax1.set_xticklabels(h1, rotation=30, ha='right')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig20.png'), dpi=300)
    
    
    
# 지역별 특정시설 분포 맵 시각화
def place_district_map(factor, district, place1):
    
    geo_path = os.path.join(STATIC_DIR, 'json/busan_gu.json')
    geo_str = json.load(open(geo_path, encoding='utf-8'))
    
    place_district_sum = []
    for i in range(len(district)):
        cs = factor[factor.place == place1][factor.district == district[i]]
        css = cs['place'].count()
        place_district_sum.append(css)
        
    pds_fd = pd.DataFrame({
        'district':district,
        'pds':place_district_sum
    })
    
    pds_fd.to_csv(os.path.join(STATIC_DIR,'maps/%s_pds_fd.csv'%(place1)))
    
    df = pd.read_csv(os.path.join(STATIC_DIR,'maps/%s_pds_fd.csv'%(place1)), index_col=1)
    
    map = folium.Map(location = [35.1856505, 129.1], zoom_start=11)
    map.choropleth(geo_data = geo_str,
              data = df['pds'],
              columns = [df.index, df['pds']],
              fill_color = 'PuRd',
              key_on='feature.id',
                  legend_name='%s 분포'%(place1))
    map.save(os.path.join(STATIC_DIR, 'maps/%s_district.html'%(place1)))
    
    
# 장소이름
def place_percent_cnt(fire_place, fire_place_sum, fire_place_damage_sum, place):
    
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    place_df = pd.DataFrame({
    'fire_place':fire_place,
    'fire_place_sum':fire_place_sum,
    'fire_place_damage_sum':fire_place_damage_sum
    })
    
    place_num = 0
    place_damage_num = 0
    place_sum = 0
    place_damage_sum = 0
    for i in range(len(fire_place)):
        if place_df['fire_place'][i] != place:
            place_sum += place_df['fire_place_sum'][i]
            place_damage_sum += place_df['fire_place_damage_sum'][i]
        else:
            place_num += place_df['fire_place_sum'][i]
            place_damage_num += place_df['fire_place_damage_sum'][i]
            
    place_sn = [place_sum, place_num]
    place_sn_damage = [place_damage_sum, place_damage_num]
    place_sn_name = ['전체', place]
            
    wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5} 
    pie_colors = ['#95C2B7', 'teal']
    
    plt.figure()
    plt.rc('font', size=20)
    plt.rc('xtick', labelsize=13)
    sns.set_palette('pastel')
    plt.title("%s 건수 비율"%(place), fontsize=20)
    plt.pie(place_sn, labels=place_sn_name, autopct='%.2f%%', startangle=180, wedgeprops=wedgeprops, colors=pie_colors)
    plt.axis('equal')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig21.png'), dpi=300) 
    
    
# 장소이름
def place_percent_damage(fire_place, fire_place_sum, fire_place_damage_sum, place):
    
    font_location = 'c:/windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    place_df = pd.DataFrame({
    'fire_place':fire_place,
    'fire_place_sum':fire_place_sum,
    'fire_place_damage_sum':fire_place_damage_sum
    })
    
    place_num = 0
    place_damage_num = 0
    place_sum = 0
    place_damage_sum = 0
    for i in range(len(fire_place)):
        if place_df['fire_place'][i] != place:
            place_sum += place_df['fire_place_sum'][i]
            place_damage_sum += place_df['fire_place_damage_sum'][i]
        else:
            place_num += place_df['fire_place_sum'][i]
            place_damage_num += place_df['fire_place_damage_sum'][i]
  
    place_sn = [place_sum, place_num]
    place_sn_damage = [place_damage_sum, place_damage_num]
    place_sn_name = ['전체', place]
            
    wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5} 
    pie_colors = ['#95C2B7', 'teal']
    
    plt.figure()
    plt.rc('font', size=20)
    plt.rc('xtick', labelsize=13)
    sns.set_palette('pastel')
    plt.title("%s 피해액 비율"%(place), fontsize=20)
    plt.pie(place_sn_damage, labels=place_sn_name, autopct='%.2f%%', startangle=180, wedgeprops=wedgeprops, colors=pie_colors)
    plt.axis('equal')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig22.png'), dpi=300) 
        

def place_district_sum(district, factor, place):
    place_district_sum = []
    place_district_damage_sum = []
    for i in range(len(district)):
        p = factor[factor.place == place][factor.district == district[i]]
        ps = p['district'].count()
        place_district_sum.append(ps)  # 화재장소 - 구 단위 화재건수
        pps = p['property_damage'].sum()
        place_district_damage_sum.append(pps) # 화재장소 - 구 단위 피해액
        
    pds_fd = pd.DataFrame({
        'district':district,  # 구
        'pds':place_district_sum,  # 화재장소 - 구별 화재건수
        'pdds':place_district_damage_sum # 화재장소 - 구별 피해액
    })
    
    pds_fd.to_csv(os.path.join(STATIC_DIR,'maps/%s_pds_fd.csv'%(place)))
    
    fig, ax1 = plt.subplots(figsize=(22,15))
    plt.title('%s의 화재 발생건수 및 재산피해규모'%(place), fontsize=19)
    plt.rc('xtick', labelsize=18)
    plt.rc('font', size=18)
    ax1.plot(district, place_district_sum, color='darkkhaki', markersize=7, linewidth=3, alpha=0.7, label='화재발생건수', marker='o')
    ax1.set_xlabel('구')
    ax1.set_ylabel('화재발생건수')
    for i, v in enumerate(district):
        plt.text(v, place_district_sum[i], str(place_district_sum[i]),
                fontsize=18,
                color='black',
                horizontalalignment='left',
                verticalalignment='bottom')
    ax2 = ax1.twinx()
    ax2.bar(district, place_district_damage_sum, color='#95C2B7', label='재산피해액(천원)', alpha=0.7, width=0.7)
    ax2.set_ylabel('피해액(천원)')
    ax2.set_ylim(0, 1600000)
    for i, v in enumerate(district):
        plt.text(v, place_district_damage_sum[i], str(place_district_damage_sum[i]),
                fontsize=18,
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig(os.path.join(STATIC_DIR, 'images/fig23.png'), dpi=300) 
    
    
# 지역별 장소 화재건수
def place_district_sum_map(district, factor, place):
    geo_path = os.path.join(STATIC_DIR, 'json/busan_gu.json')
    geo_str = json.load(open(geo_path, encoding='utf-8'))
    
    df = pd.read_csv(os.path.join(STATIC_DIR, 'maps/%s_pds_fd.csv'%(place)), index_col=1)
 
    place_district_sum = []
    place_district_damage_sum = []
    for i in range(len(district)):
        p = factor[factor.place == place][factor.district == district[i]]
        ps = p['district'].count()
        place_district_sum.append(ps)
        pps = p['property_damage'].sum()
        place_district_damage_sum.append(pps)
        
    pds_fd = pd.DataFrame({
        'district':district,
        'pds':place_district_sum,
        'pdds':place_district_damage_sum
    })
    map = folium.Map(location = [35.1856505, 129.1], zoom_start=11)
    map.choropleth(geo_data = geo_str,
              data = df['pds'],
              columns = [df.index, df['pds']],
              fill_color = 'PuRd',
              key_on='feature.id',
              legend_name='%s 지역별 화재건수'%(place))
    map.save(os.path.join(STATIC_DIR, 'maps/%s_district_cnt.html'%(place)))    
   
    
# 지역별 장소 피해규모
def place_district_damage_sum_map(district, factor, place):
    geo_path = os.path.join(STATIC_DIR, 'json/busan_gu.json')
    geo_str = json.load(open(geo_path, encoding='utf-8'))
    
    df = pd.read_csv(os.path.join(STATIC_DIR, 'maps/%s_pds_fd.csv'%(place)), index_col=1)
 
    place_district_sum = []
    place_district_damage_sum = []
    for i in range(len(district)):
        p = factor[factor.place == place][factor.district == district[i]]
        ps = p['district'].count()
        place_district_sum.append(ps)
        pps = p['property_damage'].sum()
        place_district_damage_sum.append(pps)
        
    pds_fd = pd.DataFrame({
        'district':district,
        'pds':place_district_sum,
        'pdds':place_district_damage_sum
    })
    map = folium.Map(location = [35.1856505, 129.1], zoom_start=11)
    map.choropleth(geo_data = geo_str,
              data = df['pdds'],
              columns = [df.index, df['pdds']],
              fill_color = 'PuRd',
              key_on='feature.id',
              legend_name='%s 지역별 피해규모'%(place))
    map.save(os.path.join(STATIC_DIR, 'maps/%s_district_damage.html'%(place)))    
    
# 지역별 화재발생건수 맵    
def main_district_cnt(district_df):   
    
    geo_path = os.path.join(STATIC_DIR, 'json/busan_gu.json')
    geo_str = json.load(open(geo_path, encoding='utf-8'))
     
    # 지역별 화재발생건수 맵
    district_df.to_csv(os.path.join(STATIC_DIR, 'maps/all_district_occur_cnt.csv'))
    df_cnt = pd.read_csv(os.path.join(STATIC_DIR, 'maps/all_district_occur_cnt.csv'), index_col=1)

    map = folium.Map(location = [35.1856505, 129.1], zoom_start=11)
    map.choropleth(geo_data = geo_str,
               data = df_cnt['occur_cnt'],
               columns = [df_cnt.index, df_cnt['occur_cnt']],
                          fill_color = 'PuRd', 
                          key_on='feature.id',
              legend_name='화재발생건수')
    map.save(os.path.join(STATIC_DIR, 'maps/main_district_cnt_map.html'))

  
  
  
  
  
    
    
    
    
    
    
from django.urls import path
from Milkshakes.views import *
app_name='Milkshakes'
urlpatterns = [
    path('oreoshake/',oreoshake,name='oreoshake'),
    path('kitkatshake/',kitkatshake,name='kitkatshake'),

]

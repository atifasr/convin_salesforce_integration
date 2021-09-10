from django.urls import path
from .views import *


app_name = 'users_data'


urlpatterns = [
    path('',index,name='index'),
    path('get_data/',get_data,name='get_data'),
    path('view_data/',view_data,name='view_data'),
]

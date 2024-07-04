from django.urls import path
from .views import postData
from .views import getData
from .views import delData
from .views import upData


urlpatterns = [
    path('getall/', getData),
    path('add/', postData),
    path('del/<str:pk>', delData),
    path('up', upData)

]

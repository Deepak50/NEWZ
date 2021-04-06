from django.conf.urls import url
from . import views   #from local directory

urlpatterns = [
    url('',views.index),
]


# from django.conf.urls import url

# urlpatterns = [
#     url('', views.homepageview, name='home')
# ]
from django.urls import path
from . import views

app_name = 'blog' #to reference all urls to blog and avoid mistakes with urls to others apps as portfolio

urlpatterns = [
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]

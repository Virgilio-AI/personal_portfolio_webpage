
# Date: 09/March/2022 - Wednesday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com

# first create the file urls in the app

# import the views from the same directorie

# from . import views
# from django.urls import path
#
# urlpatterns = [
#		path('inicio/',views.index,name='index'),
#		]
from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
		path('home/',views.blog_main,name='blog_main'),
		path('<int:blog_id>/',views.detail,name = 'detail'),
]



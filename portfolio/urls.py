
# Date: 09/March/2022 - Wednesday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com

from . import views
from django.urls import path

app_name = 'project'

urlpatterns = [
		path('home/',views.home,name='index'),
		path('',views.home,name='index'),
		path('<str:tag_name>/',views.tag_view,name = 'tag_view'),
		path('project_view/<int:project_id>/',views.project_view,name = 'project_view'),
		path('pdf_view/<str:file_name>/',views.pdf_view,name = 'pdf_view'),
]


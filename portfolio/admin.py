from django.contrib import admin
from .models import Project
from .models import Project_Tag
from .models import File_pdf


admin.site.register(Project)
admin.site.register(Project_Tag)
admin.site.register(File_pdf)

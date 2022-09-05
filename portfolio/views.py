from django.shortcuts import render,get_object_or_404

from .models import Project,Project_Tag,File_pdf


# Create your views here.




def home(request):
	projects = Project.objects.all()
	tags = Project_Tag.objects.all()
	dic = {}
	relevant = []
	relevant_tags = []
	for p in projects:
		tgs = p.tags.all()
		for tag in tgs:
			if tag.title == "Relevant":
				relevant.append(p)
				relevant_tags.append(tgs)
	dic['relevant'] = relevant
	dic['tags'] = tags
	return render(request,'portfolio/home.html',dic)



def tag_view(request,tag_name):
	dic = {}
	tag = get_object_or_404(Project_Tag,tag_name=tag_name)
	dic['tag'] = tag
	projects = tag.project_set.all()
	certificates = tag.file_pdf_set.all()
	dic['certificates'] = certificates
	dic['projects'] = projects
	return render(request,'portfolio/tag_detail.html',dic)



def project_view(request,project_id):
	dic = {}
	project = get_object_or_404(Project,pk=project_id)
	dic['project'] = project
	subprojects = project.project_set.all()
	dic['subprojects'] = subprojects
	return render(request,'portfolio/project_detail.html',dic)


def pdf_view(request,file_name):
	dic = {}
	pdf_file = get_object_or_404(File_pdf,file_name=file_name)
	dic['pdf'] = pdf_file.pdf
	dic['title'] = pdf_file.title
	dic['img'] = pdf_file.image
	return render(request,'portfolio/show_pdf.html',dic)



def tag_view_pdf(request,tag_id):
	dic = {}
	tag = get_object_or_404(Project_Tag,pk=tag_id)
	dic['tag'] = tag
	projects = tag.project_set.all()
	certificates = tag.file_pdf_set.all()
	dic['certificates'] = certificates
	dic['projects'] = projects
	return render(request,'portfolio/tag_detail.html',dic)






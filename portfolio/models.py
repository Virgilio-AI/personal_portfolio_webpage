from django.db import models

# Create your models here.





class Project_Tag(models.Model):
	# create a CharFiled that has a unique value
	tag_name = models.CharField(max_length=200,unique=True)
	title = models.CharField(max_length=100)
	url = models.URLField(blank=True)
	color = models.CharField(max_length=20,blank=True)
	disPlayInMenu = models.BooleanField(blank=True,default=True)


	def __str__(self):
		return self.title



class File_pdf(models.Model):
	file_name = models.CharField(max_length=200,unique=True)
	title = models.CharField(max_length=50)
	pdf = models.FileField(upload_to='portfolio/pdfs')
	main_resume = models.BooleanField(default=False,help_text="set only one pdf as the main pdf for the main page")
	image = models.ImageField(upload_to='portfolio/pdfs',blank=True)
	tags = models.ManyToManyField(Project_Tag,blank=True)

	def __str__(self):
		return self.title



class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images')
	url = models.URLField(blank=True)
	urlClean = models.CharField(max_length=100,blank=True)
	father = models.ForeignKey('self',null=True,on_delete=models.SET_NULL,blank=True)
	tags = models.ManyToManyField(Project_Tag,blank=True)


	def __str__(self):
		return self.title







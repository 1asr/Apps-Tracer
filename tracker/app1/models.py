from django.db import models

# Create your models here.

class commoninfo(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    modified_at=models.DateField()
    modified_by=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        abstract=True
    

class Department(commoninfo):
    pass
    
class Domain(commoninfo):
   pass

class Status(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Technology(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    documentation_url=models.URLField(blank=True)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=100)
    modified_at=models.DateField()
    modified_by=models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class projects(models.Model):
    
    progress={"1":"Hold","2":"Inprogress","3":"Completed"}
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Category=models.ForeignKey(Domain,on_delete =models.CASCADE)
    current_owner=models.CharField(max_length=100)
    demo_url=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)
    status=models.ForeignKey(Status,on_delete=models.CASCADE)
    techstack=models.ManyToManyField(Technology)
    POC=models.CharField(max_length=100)
    comment=models.TextField(blank=True)
    Git_link= models.URLField(blank=True)
    Application_Doc=models.URLField(blank=True)
    Research_Doc=models.URLField(blank=True)
    Deployment=models.DateTimeField(auto_now_add=True)
    code_review=models.TextField(default="not yet done")
    contact_owner=models.EmailField(null=True,blank=True)


    

    def __str__(self):
        return self.name
    



from django.urls import path
from .import views

urlpatterns=[
    path("projectList",views.projectList,name="getprojects"),
    path("projectList/<str:pk>",views.projectListbyid,name="getprojects"),
    path("projects/category/<str:category_id>",views.projectListbycategory,name="getprojectscat"),
    path("addproj",views.addproject,name="postprojects"),
    path("deleteproj/<str:pk>",views.removeproject,name="deleteproject"),
    path("techList", views.getTechnologies,name="gettech"),
    path("addTech",views.addTechnology,name="addproject"),
    path("deleteTech/<str:pk>",views.removeTech,name="removeTechnology"),
    path("domainList",views.domainList,name="getdomain"),
    path("addDomain",views.addDomain,name="postDomain"),
    path("deleteDomain/<str:pk>",views.removeDomain,name="deleteDomain"),
    path("deptList",views.DeptList,name="getDepartment"),
    path("addDept",views.addDept,name="postDept"),
    path("deleteDept/<str:pk>",views.removeDept,name="deleteDept"),

    path("statusList",views.getstatus,name="getstatus"),

]
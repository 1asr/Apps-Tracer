from django.shortcuts import render


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import projects,Technology,Domain,Department,Status
from .serializers import ProjectSerializer,TechnologySerializer,DepartmentSerializer,DomainSerializer,StatusSerializer

# Create your PROJECT views here.

@api_view(["GET"])

def projectList(request):
    projectitems= projects.objects.all()
    serializer= ProjectSerializer(projectitems,many=True)
    return Response(serializer.data)

@api_view(["GET"])

def projectListbyid(request,pk):
    projectitems= projects.objects.get(id=pk)
    serializer= ProjectSerializer(projectitems,many=True)
    return Response(serializer.data)

@api_view(["GET"])

def projectListbycategory(request,Category_id):
 projectitems=projects.objects.filter(Category=Category_id)
 serializer=ProjectSerializer(projectitems,many=True)
 return Response(serializer.data)


@api_view(['POST'])

def addproject(request):
    serializer=ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def removeproject(request, pk):
    try:
        project = projects.objects.get(id=pk)
        project.delete()
        return Response("Project item successfully deleted", status=status.HTTP_204_NO_CONTENT)
    except project.DoesNotExist:
        return Response("Project does not exist!", status=status.HTTP_404_NOT_FOUND)



# Create your TECHNOLOGY views here.

@api_view(['GET'])
def getTechnologies(request):
    tech= Technology.objects.all()
    serializer=TechnologySerializer(tech,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addTechnology(request):
    serializer=TechnologySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view((['DELETE']))
def removeTech(request,pk):
     
    try:
      tech= Technology.objects.get(id=pk)
      tech.delete()
      return Response("technology deleted successfully!",status=status.HTTP_204_NO_CONTENT)
    except tech.DoesNotExist:
        return Response("technology does not exists!" ,status=status.HTTP_404_NOT_FOUND)
    


# Create your Domain views here.


@api_view(['GET'])
def domainList(request):
    domains=Domain.objects.all()
    serializer=DomainSerializer(domains,many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addDomain(request):

    serializer= DomainSerializer(data=request.data)
    if serializer.is_valid():
          serializer.save()
          return Response(serializer.data ,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      

@api_view(['DELETE'])
def removeDomain(request,pk):
    

    try:
        domain=Domain.objects.get(id=pk)
        domain.delete()
        return Response("Domain has been removed successfully!" ,status=status.HTTP_204_NO_CONTENT)
    except domain.DoesNotExist:
        return Response("Domain does not exists!",status=status.HTTP_404_NOT_FOUND)
    

# Create your Department views here.

@api_view(['GET'])
def DeptList(request):
    depts=Department.objects.all()
    serializer=DepartmentSerializer(depts,many=True)
    return Response(serializer.data)

@api_view(['POST'])

def addDept(request):
    serializer=DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def removeDept(request,pk):
    try:
        dept=Department.objects.get(id=pk)
        dept.delete()
        return Response("Department deleted successfully!",status=status.HTTP_204_NO_CONTENT)
    except dept.DoesNotExist:
        return Response("Department does not exist",status=status.HTTP_404_NOT_FOUND)
    


#view for getStatus
#
@api_view(['GET'])
def getstatus(request):
    stats=Status.objects.all()

    serializer=StatusSerializer(stats,many=True)
    return Response(serializer.data)    


    




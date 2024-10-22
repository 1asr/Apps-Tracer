from rest_framework import serializers

from .models import projects,Technology,Department,Domain,Status



class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model= Technology
        fields="__all__"
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields="__all__"

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model= Domain
        fields="__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields="__all__"   


class ProjectSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model= projects
        fields="__all__"             





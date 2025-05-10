from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description']  # ✅ explicitly list only what user should send


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

def validate(self, data):
    print("DEBUG - Incoming data to ProjectSerializer:", data)
    return data
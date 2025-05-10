from django.urls import path, include
from rest_framework_nested import routers
from .views import ProjectViewSet, TaskViewSet
from .views import register_user

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)  # ✅ Needed for global task DELETE

project_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
project_router.register(r'tasks', TaskViewSet, basename='project-tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('register/', register_user),
]

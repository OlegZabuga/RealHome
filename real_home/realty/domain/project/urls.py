from django.urls import path

from .views import ProjectListView, ProjectDetailView


urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:project_id>/', ProjectDetailView.as_view(), name='project-detail'),
]
from django.urls import path, include
from . import views

# Template URLs
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('certifications/<int:pk>/', views.certification_detail_view, name='certification_detail'),
    path('contact/', views.contact_view, name='contact'),
]

# API URLs 
api_patterns = [
    path('about/', views.AboutMeListAPIView.as_view(), name='api_about'),
    path('skills/', views.SkillListAPIView.as_view(), name='api_skills'),
    path('projects/', views.ProjectListAPIView.as_view(), name='api_projects'),
    path('projects/<int:pk>/', views.ProjectDetailAPIView.as_view(), name='api_project_detail'),
    path('certifications/', views.CertificationListAPIView.as_view(), name='api_certifications'),
    path('certifications/<int:pk>/', views.CertificationDetailAPIView.as_view(), name='api_certification_detail'),
    path('contact/', views.contact_api_view, name='api_contact'),
]

urlpatterns += [
    path('', include(api_patterns)),
]
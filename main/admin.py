from django.contrib import admin
from .models import AboutMe, Skill, Project, Certification, ContactMe  # Add Certification

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email_public', 'created']
    readonly_fields = ['created', 'modified']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created']
    list_filter = ['category']
    readonly_fields = ['created', 'modified']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'featured', 'created']
    list_filter = ['project_type', 'featured', 'technologies_used']
    filter_horizontal = ['technologies_used']  
    readonly_fields = ['created', 'modified']

@admin.register(Certification)  
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'category', 'issue_date', 'is_expired']
    list_filter = ['category', 'issue_date']
    readonly_fields = ['created','modified']
    search_fields = ['name', 'issuer', 'credential_id']

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created']
    readonly_fields = ['name', 'email', 'message', 'created', 'modified']
    
    # Make contact messages read-only in admin
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
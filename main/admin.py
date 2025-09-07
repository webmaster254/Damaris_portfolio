from django.contrib import admin
from .models import AboutMe, Skill, Project, Certification, ContactMe  
from django.utils.html import format_html
from .models import Project
import re


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
    readonly_fields = ['description_preview']
    
    def description_preview(self, obj):
        """Convert description text with bullet points to HTML"""
        if not obj.description:
            return "No description provided"
        
        # Split the description into lines
        lines = obj.description.split('\n')
        html_lines = []
        
        for line in lines:
            stripped_line = line.strip()
            
            # Skip empty lines
            if not stripped_line:
                continue
                
            # Check if line starts with a bullet indicator
            if re.match(r'^[-*]\s', stripped_line):
                content = re.sub(r'^[-*]\s*', '', stripped_line)
                if content:
                    html_lines.append(f'<li>{content}</li>')
            # Check for headings
            elif stripped_line.startswith('## '):
                content = stripped_line[3:].strip()
                html_lines.append(f'<h3>{content}</h3>')
            elif stripped_line.startswith('# '):
                content = stripped_line[2:].strip()
                html_lines.append(f'<h2>{content}</h2>')
            else:
                # Check if this line might be a bullet point without space
                if stripped_line.startswith(('-', '*')):
                    content = stripped_line[1:].strip()
                    html_lines.append(f'<li>{content}</li>')
                else:
                    # Regular paragraph
                    html_lines.append(f'<p>{stripped_line}</p>')
        
        # If we have list items, wrap them in <ul>
        if any('<li>' in line for line in html_lines):
            final_html = []
            in_list = False
            
            for line in html_lines:
                if '<li>' in line:
                    if not in_list:
                        final_html.append('<ul>')
                        in_list = True
                    final_html.append(line)
                else:
                    if in_list:
                        final_html.append('</ul>')
                        in_list = False
                    final_html.append(line)
            
            if in_list:
                final_html.append('</ul>')
                
            return format_html(''.join(final_html))
        else:
            return format_html(''.join(html_lines))
    
    description_preview.short_description = 'Description Preview'
    description_preview.allow_tags = True
    
    fieldsets = [
        (None, {
            'fields': ['title', 'project_type', 'technologies_used', 'featured']
        }),
        ('Content', {
            'fields': ['description', 'description_preview'],
            'description': 'Enter your description. Use "-" or "*" for bullet points. Use "#" for headings.'
        }),
        ('URLs & Media', {
            'fields': ['github_url', 'live_demo_url', 'architecture_diagram'],
            'classes': ['collapse']
        }),
    ]

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
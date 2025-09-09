# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django portfolio website for Damaris, showcasing skills, projects, certifications, and providing a contact form. The project uses Django 5.2.5 with Django REST Framework for API endpoints and includes both template-based views and API endpoints.

## Development Commands

### Running the Development Server
```bash
python manage.py runserver
```

### Database Management
```bash
# Apply migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations

# Create superuser for admin access
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test main
```

## Project Architecture

### Core Structure
- **portfolio_project/**: Main project directory containing settings and root URL configuration
- **main/**: Primary Django app containing all portfolio functionality
- **media/**: User-uploaded files (profile photos, architecture diagrams, certification images)
- **db.sqlite3**: SQLite database (development only)

### Models Architecture (main/models.py)
- **TimeStampedModel**: Abstract base class providing created/modified timestamps
- **AboutMe**: Personal information, bio, social links, contact details
- **Skill**: Technical skills with categories and optional icons
- **Project**: Portfolio projects with technology stack, GitHub links, featured status
- **Certification**: Professional certifications with expiration tracking
- **ContactMe**: Contact form submissions

### Views Pattern (main/views.py)
The application follows a dual-interface pattern:
- **Template views**: Traditional Django views for web interface (home, about, projects, contact, etc.)
- **API views**: REST API endpoints using Django REST Framework for the same data

### URL Structure (main/urls.py)
- Root URLs serve both template views and API endpoints
- API endpoints mirror template functionality but return JSON
- Detail views available for both projects and certifications

## Environment Configuration

### Required Environment Variables (.env)
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode setting
- `DEFAULT_FROM_EMAIL`: Email address for outgoing emails
- `CONTACT_EMAIL`: Email address to receive contact form submissions
- `EMAIL_HOST_PASSWORD`: Gmail app password for SMTP (optional)

### Email Configuration
- If `EMAIL_HOST_PASSWORD` is provided: Uses Gmail SMTP
- If not provided: Uses console backend for development (emails printed to console)

## Database Schema Notes

### Key Relationships
- **Project.technologies_used**: Many-to-many relationship with Skill model
- **Skill.category**: Categorized skills (Programming Language, Framework, Cloud, etc.)
- **Project.featured**: Boolean flag for highlighting projects on home page
- **Certification.expiration_date**: Optional field with built-in expiration checking

### Unique Constraints
- **AboutMe**: Only one instance allowed per full_name
- **Skill.name**: Globally unique skill names

## Frontend Integration

### Template Structure
- **base.html**: Main template with common layout
- Page-specific templates in `main/templates/main/`
- Context data includes grouped skills by category for organized display

### Media Handling
- Profile photos: `media/profile/`
- Architecture diagrams: `media/architecture_diagrams/`
- Certification images: `media/certification/`
- Static files: configured for both development and production

## API Endpoints

All API endpoints are accessible at the same URLs as template views and return JSON:
- GET `/about/` - About me information
- GET `/skills/` - All skills
- GET `/projects/` - All projects
- GET `/projects/<id>/` - Project detail
- GET `/certifications/` - All certifications
- GET `/certifications/<id>/` - Certification detail
- POST `/contact/` - Submit contact form

## Development Notes

### CORS Configuration
- `CORS_ALLOW_ALL_ORIGINS = True` for development
- Should be restricted for production deployment

### Security Considerations
- Django admin available at `/admin/`
- CSRF protection enabled for forms
- Media files served during development only
- Email credentials loaded from environment variables
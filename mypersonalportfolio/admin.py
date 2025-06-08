from django.contrib import admin
from .models import Banner, skills, Projects, About, ContactMe, Resume, Experience, Services, PersonalInfo, blogs

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'github_link', 'live_link')
    search_fields = ('title', 'description')
    list_filter = ('technologies',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('timestamp',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'start_date', 'end_date')
    search_fields = ('job_title', 'company_name')
    list_filter = ('start_date', 'end_date')

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'location')
    search_fields = ('full_name', 'email')
    list_filter = ('location',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')
    list_filter = ('icon',)

@admin.register(blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'modified_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date', 'modified_date')
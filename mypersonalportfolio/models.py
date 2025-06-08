from django.db import models
from portfolio import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=settings.BANNER, null=True, blank=True)

    def __str__(self):
        return self.title


class skills(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Database', 'Database'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Other')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0)  # 0-100 scale

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.PROJECTS_IMAGES, null=True, blank=True)
    technologies = models.CharField(max_length=200, blank=True) 
    github_link = models.URLField(max_length=200, blank=True)
    live_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to=settings.PROFILE_IMAGES, null=True, blank=True)

    def __str__(self):
        return f"{self.description[:20]}"
    
class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
class Resume(models.Model):
    file = models.FileField(upload_to=settings.RESUME, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Resume uploaded at {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
    

class Experience(models.Model):
    job_title =models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.job_title
    
class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin_profile = models.URLField(max_length=200, blank=True)
    github_profile = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.full_name
    
class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)  # Assuming icon is a string (e.g., font-awesome class)

    def __str__(self):
        return self.title

class blogs(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to=settings.BLOGS_IMAGES, null=True, blank=True)
    author = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views import View
from portfolio import settings
from .models import About, Banner, PersonalInfo, Projects, skills, Resume, Experience, Services, blogs
from django.http import HttpResponseRedirect
from .forms import ContactMeForm
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

def portfolio_index(request):
    form = ContactMeForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your Details have been sent successfully! Thank you for reaching out.")
            return HttpResponseRedirect(reverse('home') + '#contact') 
        else:
            messages.error(request, "Please correct the errors below.")
    
    # Fetch all data
    banner = Banner.objects.first()
    about = About.objects.first()
    personal_info = PersonalInfo.objects.first()
    all_skills = skills.objects.all().order_by('category', 'name')

    from collections import defaultdict
    grouped_skills = defaultdict(list)
    for skill in all_skills:
        grouped_skills[skill.category].append(skill)
    sorted_grouped_skills = sorted(grouped_skills.items())

    context = {
        'form': form,
        'banner': banner,
        'grouped_skills': sorted_grouped_skills,
        'projects': Projects.objects.all(),
        'about': about,
        'resume_files': Resume.objects.first(),
        'experience': Experience.objects.all(),
        'personal_info': personal_info,
        'services': Services.objects.all(),
        'blogs': blogs.objects.all()[:3],
    }
    return render(request, 'home.html', context)


class BlogListView(ListView):
    model = blogs
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-published_date']

class BlogDetailView(DetailView):
    model = blogs
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

from django.urls import path
from .views import  portfolio_index
from mypersonalportfolio import views

urlpatterns = [
    path('', portfolio_index, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    path('blogs/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),

]

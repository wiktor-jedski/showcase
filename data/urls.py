from django.urls import path

from data import views

app_name = 'data'

urlpatterns = [
    path('', views.analysis_list, name='analysis_list'),
    path('programming_languages/', views.programming_languages, name='programming_languages'),
    path('google_analytics/', views.google_analytics, name='google_analytics'),
    path('lego_analysis/', views.lego_analysis, name='lego_analysis'),
]

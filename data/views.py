from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.shortcuts import render
from django.urls import reverse

from data import forms
from data.analysis_scripts.scripts import programming_languages_analysis
from data.models import Analysis


def analysis_list(request):
    # context = {'analyses': [
    #     {'link': 'data:programming_languages', 'photo': "data/languages.png",
    #      'title': 'Programming Languages', 'text': 'An analysis of number of threads in StackOverflow.'}
    # ]}
    context = {'analyses': Analysis.objects.all()}
    return render(request, 'data/analysis_list.html', context)


def programming_languages(request):
    """
    Renders a view for analysis of programming languages threads in StackOverflow.
    """
    if request.method == 'GET':
        context = programming_languages_analysis()
        context['form'] = forms.LanguagesForm()
        return render(request, 'data/programming_languages.html', context)
    elif request.method == 'POST':
        form = forms.LanguagesForm(request.POST)
        if form.is_valid():
            choices = form.cleaned_data['choices']
            print(choices)
            context = programming_languages_analysis(choices)
            context['form'] = forms.LanguagesForm()
            return render(request, 'data/programming_languages.html', context)
        else:
            return reverse('data:programming_languages')


def google_analytics(request):
    """
    Returns a file download containing analysis of Google Trends data regarding unemployment and Bitcoin prices.
    """
    file = finders.find('data/Google_Trends.zip')
    return FileResponse(open(file, 'rb'), as_attachment=True)


def lego_analysis(request):
    """
    Returns a file download containing analysis of LEGO sets and themes.
    """
    file = finders.find('data/Lego_Analysis.zip')
    return FileResponse(open(file, 'rb'), as_attachment=True)


def films_analysis(request):
    """
    Returns a file download containing analysis of films' budgets and revenues.
    """
    file = finders.find('data/Films_Budgets.zip')
    return FileResponse(open(file, 'rb'), as_attachment=True)


def nobel_analysis(request):
    """
    Returns a file download containing analysis of Nobel Prizes.
    """
    file = finders.find('data/Nobel_Prize_Analysis.zip')
    return FileResponse(open(file, 'rb'), as_attachment=True)

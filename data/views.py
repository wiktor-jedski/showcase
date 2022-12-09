from django.shortcuts import render

from data import forms
from data.analysis_scripts.scripts import programming_languages_analysis


def analysis_list(request):
    context = {'analyses': [
        {'link': 'data:programming_languages', 'photo': "data/languages.png",
         'title': 'Programming Languages', 'text': 'An analysis of number of threads in StackOverflow.'}
    ]}
    return render(request, 'data/analysis_list.html', context)


def programming_languages(request):
    """
    Renders a view for analysis of programming languages threads in StackOverflow.
    """
    form = forms.LanguagesForm()
    if request.method == 'GET':
        context = programming_languages_analysis()
        return render(request, 'data/programming_languages.html', context)
    elif request.method == 'POST':
        choices = form.cleaned_data['choices']
        context = programming_languages_analysis(choices)
        return render(request, 'data/programming_languages.html', context)

from django import forms


class LanguagesForm(forms.Form):
    choices = forms.MultipleChoiceField(choices=('assembly', 'c', 'c#', 'c++', 'delphi', 'go', 'java', 'javascript',
                                                 'perl', 'php', 'python', 'r', 'ruby', 'swift'))

from django import forms


class LanguagesForm(forms.Form):
    choices = forms.MultipleChoiceField(choices=(('assembly', 'assembly'),
                                                 ('c', 'c'),
                                                 ('c#', 'c#'),
                                                 ('c++', 'c++'),
                                                 ('delphi', 'delphi'),
                                                 ('go', 'go'),
                                                 ('java', 'java'),
                                                 ('javascript', 'javascript'),
                                                 ('perl', 'perl'),
                                                 ('php', 'php'),
                                                 ('python', 'python'),
                                                 ('r', 'r'),
                                                 ('ruby', 'ruby'),
                                                 ('swift', 'swift')))

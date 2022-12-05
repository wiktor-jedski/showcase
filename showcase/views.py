from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'

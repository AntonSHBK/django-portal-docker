from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'main_page/main_page.html'
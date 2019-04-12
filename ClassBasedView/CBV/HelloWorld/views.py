from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

'''# Create your views here.
def index(request):
    return render(request, 'index.html')
'''

'''class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")
'''

#Returning Templates
# Context dictionary with index view
class IndexView(TemplateView):
    template_name = 'index.html' # No subdicrectory

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC_INJECTION'
        return context

from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Art


# Create your views here.
class Personal_Page(View):

    def post(self, request, *args, **kwargs):
        context = dict()
        return render(request, 'personal_page.html', context)

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, 'personal_page.html', context)

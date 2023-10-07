from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView,ListView
from app.forms import SchoolForm
from django.http import HttpResponse
from app.models import School

#Inserting data by using FormView.
class SchoolInsertForm(FormView):
    form_class=SchoolForm
    template_name="SchoolInsertForm.html"

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data inserted successfully')
    
#Displaying data by using ListView.
class DisplaySchool(ListView):
    model=School
    template_name='DisplaySchool.html'
    context_object_name='sclist'

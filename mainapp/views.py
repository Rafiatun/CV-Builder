import os
from re import template
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse,FileResponse
from django.template import loader
from django.views.generic import View 
import pdfkit
from django.template.loader import render_to_string
import tempfile


# Create your views here.
def Home(request):
    return render(request ,'index.html')

def CVMaking(request):
    IntroForm= IntroductionForm()
    if request.method == "POST":
        IntroForm = IntroductionForm(request.POST)
        if IntroForm.is_valid():
            IntroForm.save()

            return redirect('home')
            
    else:

        IntroForm= IntroductionForm()

    context={
        'form1': IntroForm,
       

    }

    return render(request , 'generator.html', context)

def InfoList(request):
    Profile=Introduction.objects.all()
    context={
        
        'Profile': Profile

    }
    return render(request ,'list.html',context)

##generating cv

def Get_PDF(request,id):
    user_profile=Introduction.objects.get(pk=id)
    template=loader.get_template('resume.html')
    html=template.render({'user_profile': user_profile})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
        "enable-local-file-access": ""

    }
    pdf=pdfkit.from_string(html,False,options)
    response= HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] ="attachment"
    filename="resume.pdf"
    return response



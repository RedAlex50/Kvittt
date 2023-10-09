from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Case, CaseBlock, New
from transliterate import translit, get_available_language_codes
from .forms import NewForm, CaseForm
from pathlib import Path
import os

class Main(View):
    def get(self, request):
        return render(request, "main/main.html")

class Cases(View):
    def get(self, request):
        cases = Case.objects.all()
        
        i=0
        for el in cases:
            cases[i].titleForURL = translit(cases[i].title.replace(' ', '-'), language_code='ru', reversed=True)
            i += 1      
            
        data = {
            'cases': cases,
        }
        return render(request, "cases/cases.html", data)
    
class Blog(View):
    def get(self, request):
        news = New.objects.all()
        data = {
            'news': news,
        }

        return render(request, "blog/blog.html", data)
    
class Error(View):
    def get(self, request):
        return render(request, "error/errorPage.html")
        
class CasePage(View):
    def get(self, request, id, titleForURL):
        id = int(id)
        titleForURL = str(titleForURL)
        data = None


        if(id == None):
            return redirect('error')

        data = Case.objects.filter(id = id)
        caseBlocks = CaseBlock.objects.filter(fk = id)
        
        try:
            if(titleForURL != translit(data[0].title.replace(' ', '-'), language_code='ru', reversed=True)):
                return redirect('error')
        except:
            return redirect('error')   

        context = {
            'titleForURL': titleForURL,
            'data' : data,
            'caseBlocks': caseBlocks
        }
        return render(request, "cases/caseObject/caseObject.html", context=context)
    def post(self, request, id, titleForURL):
        id = int(id)
        titleForURL = str(titleForURL)
        data = None


        if(id == None):
            return redirect('error')

        data = Case.objects.filter(id = id)
        caseBlocks = CaseBlock.objects.filter(fk = id)
        
        try:
            if(titleForURL != translit(data[0].title.replace(' ', '-'), language_code='ru', reversed=True)):
                return redirect('error')
        except:
            return redirect('error')   

        context = {
            'titleForURL': titleForURL,
            'data' : data,
            'caseBlocks': caseBlocks
        }
        return render(request, "cases/caseObject/caseObject.html", context=context)
    
class CreateNew(View):
    def get(self, request):
        error = ''
        if request.method == 'POST':
            form = NewForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog')
            else:
                error = "Форма заполнена некорректно!"

        form = NewForm()

        data = {
            'form': form,
            'error': error,
        }
        return render(request, "blog/createNewForm/createNewForm.html", data)
    def post(self, request):
        error = ''
        if request.method == 'POST':
            form = NewForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog')
            else:
                error = "Форма заполнена некорректно!"

        form = NewForm()

        data = {
            'form': form,
            'error': error,
        }
        return render(request, "blog/createNewForm/createNewForm.html", data)
    
class CreateCase(View):
    def get(self, request):
        error = ''
        if request.method == 'POST':
            form = CaseForm(request.POST, request.FILES)            
            if form.is_valid():
                form.save()
                return redirect('cases')
            else:
                error = "Форма заполнена некорректно!"

        form = CaseForm()

        data = {
            'form': form,
            'error': error,
        }
        return render(request, "cases/createCaseForm/createCaseForm.html", data)
    def post(self, request):
        error = ''
        titleError = ''
        if request.method == 'POST':
            form = CaseForm(request.POST, request.FILES)
            if form.is_valid():
                if ('/' in str(form.cleaned_data['title'])) | ('(' in str(form.cleaned_data['title'])) | (')' in str(form.cleaned_data['title'])) | ('*' in str(form.cleaned_data['title'])) | ('^' in str(form.cleaned_data['title'])) | ('/' in str(form.cleaned_data['title'])) | ('+' in str(form.cleaned_data['title'])):
                    titleError = "Не используйте символы: /, (, ), *, ^, /, +"    
                else:
                    form.save()
                    return redirect('cases')
            else:
                error = "Форма заполнена некорректно!"

        form = CaseForm()

        data = {
            'titleError': titleError,
            'form': form,
            'error': error,
        }
        return render(request, "cases/createCaseForm/createCaseForm.html", data)
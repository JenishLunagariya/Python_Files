# I have created this file
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

params = {'name':'Jenish Lunagariya'}

def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html',params)

def analyze(request):
    # get the text
    djtext = request.GET.get('text','defualt')
    # check box value
    removepunc = request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    extraspaceremove = request.GET.get('extraspaceremove','off')
    # removepunc
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}

        return render(request,"analyze.html",params)
    # fullcaps
    elif fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose':'Full Caps','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    # extraspaceremove
    elif extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed+=djtext[index]
        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    # no check
    else:
        return HttpResponse("please check any of box")

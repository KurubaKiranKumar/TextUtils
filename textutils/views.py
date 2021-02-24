#This is created by me and it does not come via Django.
from django.http import HttpResponse
from django.shortcuts import render # this has to be done in order to use Templates in Django.

def index(request):
    dictio={'name':'Harry','place':'USA'}
    return render(request,'index.html',dictio)#render function helps in sending html file so that it gets rendered on Browser.

def analyze(request):
    djText = request.POST.get('text', 'default')
    print(djText)
    removePunc = request.POST.get('removePunc', 'off')
    cap = request.POST.get('capi', 'off')
    params = {'Purpose': '', 'Analyzed': ''}
    print(removePunc)
    print(cap)
    analyzed = ""
    punc = ".?,-"
    if removePunc == 'on':
        for c in djText:
            if c not in punc:
                analyzed = analyzed + c
        params = {'Purpose': 'To remove Punctuations', 'Analyzed': analyzed}
        return render(request, 'analyze.html', params)
    elif cap == 'on':
        for c in djText:
            analyzed = analyzed + c.upper()
        params = {'Purpose': 'To Capitalize Letters', 'Analyzed': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

def aboutUs(request):
    return render(request,'aboutUs.html')




from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index.html')


    # return HttpResponse("Home")



def analyze(request):

    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    # newlineremover = request.POST.get('newlineremover', 'off')
    # extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                djtext=analyzed
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if (fullcaps=="on"):

        analyzed = ""
        for char in djtext:
            analyzed= analyzed + char.upper()
            djtext = analyzed
        params = {'purpose': 'Remove lower case', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps!="on"):

       return HttpResponse("error")


    return render(request, 'analyze.html', params)



    # else:
    #     return HttpResponse("Error")
def about(request):

    return render(request,'about.html')
def contact(request):
    return render(request ,'contact us.html')


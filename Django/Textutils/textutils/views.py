#I made this
from django.http import HttpResponse
from django.shortcuts import render
import re
import string

def index(request):
    #return HttpResponse("<h1>Hello<h1><a href='https://www.analyticsvidhya.com/blog/2021/12/complete-nlp-landscape-from-1960-to-2020/'>NLP Landscape</a><br><a href="">CodewithHarry</a><br><a>GitHub</a>")
    #return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #print(djtext)
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    countchrs = request.GET.get('countchrs', 'off')
    analyzed = djtext
    purpose = ""
    if removepunc == "on":
        punctuations = string.punctuation
        analyzed = re.sub(r'[^\w\s]', '', djtext)
        purpose = purpose + "| Removed Punctuations |"
        #params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    
    if fullcaps == "on":
        temp = analyzed.upper()
        analyzed = temp
        purpose = purpose + "| converted str to uppercase |"
        #params = {'purpose': "converted str to uppercase", 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        temp = ""
        for char in analyzed:
            if char != '\n':
                temp = temp + char
        analyzed = temp
        purpose = purpose + "| Popped NewLine |"
        #params = {'purpose': "Popped NewLine", 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)    

    if extraspaceremover == "on":
        temp = re.sub(' +', ' ', analyzed)
        analyzed = temp
        purpose = purpose + "| Removed Extra Spaces |"
        #params = {'purpose': "Removed Extra Spaces", 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params) 
        #Alternate way to remove extra spaces
        '''
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        ''' 
    if countchrs == "on":
        txt_set = set(analyzed)
        if " " in txt_set:
            temp = len(txt_set)-1 #to remove count of space
        else:
            temp = len(txt_set)
        analyzed = analyzed + "\n" + temp
        purpose = purpose + "| count of unique chrs |"
        #params = {'purpose': "unique number of chr is-", 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    
    if removepunc == "on" or fullcaps == "on" or countchrs=="on" or newlineremover=="on" or extraspaceremover=="on":
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


def capitalizeFirst(request):
    return HttpResponse("capitalize")
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    data = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    removespaces = request.POST.get('spaceremover', "off")
    countchar = request.POST.get('counter','off')

    #
    # REMOVE PUNCTUATION MARKS
    #
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        data = analyzed
        # return render(request, "analyze.html", params)
    #
    # TO UPPERCASE THE GIVEN TEXT
    #
    if(fullcaps == "on"):
        analyzed = ""
        for char in data:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        data = analyzed
        # return render(request, "analyze.html", params)
    #
    # TO REMOVE NEW LINE CHARACTER FROM THE GIVEN STRING
    #
    if(newlineremover == "on"):
        analyzed = ""
        for char in data:
            if char != "\n" and char!= "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new Line characters.', 'analyzed_text': analyzed}
        data = analyzed
        # return render(request, "analyze.html", params)
    #
    # Remove Spaces
    #
    if(removespaces == "on"):
        analyzed = ""
        for char in data:
            if not char == " ":
                analyzed = analyzed + char

        params = {'purpose': 'Removed any spaces', 'analyzed_text': analyzed}
        data = analyzed
        # return render(request, "analyze.html", params)
    #
    # Count Characters
    #
    elif(countchar == "on"):
        counter = len(data)
        params = {'purpose': 'Counted characters', 'analyzed_text': counter}
        data = analyzed
        # return render(request, "analyze.html", params)

    return render(request, "analyze.html", params)

def about(request):
    return render(request, "about.html")
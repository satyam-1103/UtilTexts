from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    data = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    removespaces = request.GET.get('spaceremover', "off")
    countchar = request.GET.get('countchar','off')

    #
    # REMOVE PUNCTUATION MARKS
    #
    if removepunc == 'on':
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    #
    # TO UPPERCASE THE GIVEN TEXT
    #
    elif(fullcaps == "on"):
        analyzed = ""
        for char in data:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    #
    # TO REMOVE NEW LINE CHARACTER FROM THE GIVEN STRING
    #
    elif(newlineremover == "on"):
        analyzed = ""
        for char in data:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new Line characters.', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    #
    # Remove Spaces
    #
    elif(removespaces == "on"):
        analyzed = ""
        for char in data:
            if not char == " ":
                analyzed = analyzed + char

        params = {'purpose': 'Removed any spaces', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    #
    # Count Characters
    #
    elif(countchar == "on"):
        counter = len(data)
        params = {'purpose': 'Counted characters', 'analyzed_text': counter}
        return render(request, "analyze.html", params)

    else:
        return HttpResponse("ERROR ")

def about(request):
    return render(request, "about.html")
# I CREATED THIS VIEW FILE

from django.http import HttpResponse
from django.shortcuts import render

"""

def index(request):
    return HttpResponse('''<h1> Shreyash Bahi</h1> <a href="https://www.youtube.com/">YouTube</a> <br> <a href="https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjX6KejwK70AhUx7HMBHf7bAhcQPAgI"> Google</a> ''')

def about(request):
    return HttpResponse("<h1> about Shreyash Bahi</h1>")

"""


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lcase = request.GET.get('lcase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if lcase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and lcase != "on":
        return "Error"

    return render(request, 'analyze.html', params)

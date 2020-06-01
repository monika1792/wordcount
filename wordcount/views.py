from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hithere' : "This is me"})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict= {}
    for word in wordlist:
        if word in worddict:
            # increase
            worddict[word] += 1
        else:
            worddict[word] = 1

    sorted(worddict.items(), )
    return render(request, 'count.html', {'fulltext': fulltext , 'wordcount' : len(wordlist) , 'worddic': worddict.items()})


def aboutUs(request):
    return render(request, 'aboutus.html', {'aboutus' : "My name is Monika, This my first website"})
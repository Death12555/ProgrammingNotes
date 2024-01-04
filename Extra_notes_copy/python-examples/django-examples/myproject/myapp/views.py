from django.shortcuts import render
from django.http import HttpResponse


def word_counter(request):
    return render(request, 'word_counter.html')

def count(request):
    text= request.POST['text']
    number_of_words= len(text.split())
    return render(request, 'count.html', {'number': number_of_words})
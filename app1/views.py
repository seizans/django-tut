from django.shortcuts import render


def page1(request):
    return render(request, 'app1/page1.html')

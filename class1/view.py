from django.shortcuts import render


def page_not_found(request):
    return render(request, '404.html')
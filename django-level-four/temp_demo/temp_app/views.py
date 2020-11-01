from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'text': 'hello World',
        'number': 100
    }
    return render(request, 'temp_app/index.html', context)


def other(request):
    return render(request, 'temp_app/other.html')


def relative(request):
    return render(request, 'temp_app/relative.html')

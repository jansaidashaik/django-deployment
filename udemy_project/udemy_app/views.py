from django.shortcuts import render
from udemy_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    # print(webpages_list)
    context = {'access_records': webpages_list}
    return render(request, 'udemy_app/index.html', context)
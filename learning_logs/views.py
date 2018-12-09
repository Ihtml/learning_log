from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    all_topics = Topic.objects.order_by('date_added')
    context = {'topics': all_topics}
    return render(request, 'learning_logs/topics.html', context)


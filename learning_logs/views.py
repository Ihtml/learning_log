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


def topic(request, topic_id):
    a_topic = Topic.objects.get(id=topic_id)
    entries = a_topic.entry_set.order_by('-date_added')
    context = {'topic': a_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

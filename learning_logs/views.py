from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm


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


def new_topic(request):
    # 添加新主题
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

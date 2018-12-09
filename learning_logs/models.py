from django.db import models

# Create your models here.


class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    # 学到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 模型对象的复数名,如果不指定该选项，那么默认的复数名字是verbose_name加上‘s’
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."


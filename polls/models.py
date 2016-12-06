# coding=utf-8
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime


@python_2_unicode_compatible
class Question(models.Model):
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题集'

    question_text = models.CharField('问题文本', max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布?'


@python_2_unicode_compatible
class Choice(models.Model):
    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项集'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项文本', max_length=200)
    votes = models.IntegerField('投票', default=0)

    def __str__(self):
        return self.choice_text

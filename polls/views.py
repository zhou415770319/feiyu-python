# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Question,Choice
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    temlate = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)
    # return HttpResponse(temlate.render(context,request))#原始方式#

    # output = ', '.join(q.question_text for q in latest_question_list)
    # return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice."})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
    # return HttpResponse("You're voting on question %s." % question_id)


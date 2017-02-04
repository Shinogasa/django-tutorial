from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import mark_safe

from .models import Choice, Question
from .forms import MyForm

def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })

def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {
        'question': obj,
    })

def results(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {
        'question': obj,
    })

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('index')

def form_test(request):
    form = MyForm()
    return render(request, 'polls/form.html', {
        'form': form,
    })

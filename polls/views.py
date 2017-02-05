from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import mark_safe

from .models import Question
from .forms import MyForm, VoteForm

def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })

def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = VoteForm(question=obj, data=request.POST)
        if form.is_valid():
            form.vote()
            return redirect('polls:results', pk)
    else:
        form = VoteForm(question=obj)
    return render(request, 'polls/detail.html', {
        'form': form,
        'question': obj,
    })

def results(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {
        'question': obj,
    })

def form_test(request):
    if request.method == "POST":
        form = MyForm(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = MyForm()
    return render(request, 'polls/form.html', {
        'form': form,
    })

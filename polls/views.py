from django.shortcuts import get_object_or_404, render, resolve_url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Question
from .forms import MyForm, VoteForm

def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })

class Detail(SingleObjectMixin, FormView):
    model = Question
    form_class = VoteForm
    context_object_name = 'question'
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(requestm *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_from_kwargs(self):
        kwargs = super().get_from_kwargs()
        kwargs['question'] = self.object
        return kwargs

    def from_valid(self, form):
        form.vote()
        return super(),form_valid(form)

    def get_success_url(self):
        return resolve_url('polls:results', self.kwargs['pk'])

detail = Detail.as_view()
def results(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {
        'question': obj,
    })

class FormTest(FormView):
    form_class = MyForm
    template_name = 'polls/form.html'
    success_url = reverse_lazy('polls:index')

form_test = FormTest.as_view()

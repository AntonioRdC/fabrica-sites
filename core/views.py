from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from .forms import ContatoForm
from .models import Funcionario, Servico


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        context['servico'] = Servico.objects.all()
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o E-mail!')
        return super(IndexView, self).form_invalid(form)


class ServicosView(DetailView):
    template_name = 'detalhar_servicos.html'
    model = Servico
    context_object_name = 'servico'

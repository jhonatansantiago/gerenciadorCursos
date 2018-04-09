from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from turmaApp.models import Turma, Aluno, Professor
from django.views import generic
from django.core.urlresolvers import reverse_lazy

# Views da Turma =====================================================================================

class TurmaListView(generic.ListView):
	template_name = 'turmaApp/lista_turma.html'
	context_object_name = 'lista'

	def get_queryset(self):
        	return Turma.objects.all()


class TurmaSearchView(generic.ListView):
	template_name = 'turmaApp/lista_turma.html'
	context_object_name = 'lista'

	def get_queryset(self):
		pesquisa = self.request.REQUEST.get("pesquisa")
		return  Turma.objects.filter(nome__startswith=pesquisa)
		
		


class TurmaCreateView(generic.CreateView):
	template_name = 'turmaApp/form.html'
	model  = Turma
	success_url = 'saved'


class TurmaUpdateView(generic.UpdateView):
	template_name = 'turmaApp/form.html'
	model  = Turma
	success_url = 'saved'

class TurmaDeleteView(generic.DeleteView):
	template_name = 'turmaApp/remove.html'
	model = Turma
	success_url = 'saved'

class TurmaDetailView(generic.DetailView):
	template_name = 'turmaApp/detalhes_turma.html'
	model = Turma

#=========================================================================================================
# Views do Aluno



class AlunoListView(generic.ListView):
    template_name = 'turmaApp/lista_aluno.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Aluno.objects.all()

class AlunoSearchView(generic.ListView):
	template_name = 'turmaApp/lista_aluno.html'
	context_object_name = 'lista'

	def get_queryset(self):
		pesquisa = self.request.REQUEST.get("pesquisa")
		return  Aluno.objects.filter(nome__startswith=pesquisa)



class AlunoCreateView(generic.CreateView):
    template_name = 'turmaApp/form.html'
    model  = Aluno
    success_url = 'saved'


class AlunoUpdateView(generic.UpdateView):
    template_name = 'turmaApp/form.html'
    model  = Aluno
    success_url = 'saved'

class AlunoDeleteView(generic.DeleteView):
    template_name = 'turmaApp/remove.html'
    model = Aluno
    success_url = 'saved'



#=========================================================================================================
# Views do Professor

class ProfessorListView(generic.ListView):
    template_name = 'turmaApp/lista_professor.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Professor.objects.all()


class ProfessorSearchView(generic.ListView):
	template_name = 'turmaApp/lista_professor.html'
	context_object_name = 'lista'

	def get_queryset(self):
		pesquisa = self.request.REQUEST.get("pesquisa")
		return  Professor.objects.filter(nome__startswith=pesquisa)
		



class ProfessorCreateView(generic.CreateView):
    template_name = 'turmaApp/form.html'
    model  = Professor
    success_url = 'saved'


class ProfessorUpdateView(generic.UpdateView):
    template_name = 'turmaApp/form.html'
    model  = Professor
    success_url = 'saved'

class ProfessorDeleteView(generic.DeleteView):
    template_name = 'turmaApp/remove.html'
    model = Professor
    success_url = 'saved'


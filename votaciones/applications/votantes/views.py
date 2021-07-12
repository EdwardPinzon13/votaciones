from django.db import IntegrityError
from django.urls.base import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import  FormView
from django.views.generic import ListView,TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VerificarVotanteForm
# Create your views here.
from .models import Votantes
from applications.candidatos.models import Candidato,eleccion




class VerificarVotante(FormView):
    template_name = 'eleccion.html'
    form_class = VerificarVotanteForm
    success_url = 'candidatos.html'

    def post(self,request,*args, **kwargs):
        cedula_user =request.POST['cedula']
        try:
            user = Votantes.objects.get(cedula=cedula_user)
            if user:
                if user.estado_voto==True:
                    message = 'El usuario registrado con la cedula #'+ '   ' + user.cedula+ '  '+' ya ha realizado la votación'
                    return render(request,'error.html', {'message_error': message})
                else:
                    return HttpResponseRedirect(reverse('votante_app:eleccion-votante',kwargs={'cc':user.cedula}))
        except ObjectDoesNotExist:
                    return render(
                        request,
                        'error.html',
                        {'message_error': 'Lo sentimos el numero de cedula  no se encuntra registrado, comunicarse con correo@gmail.com para más información'}
                        )
        return super().post(request,*args,**kwargs)

    def form_valid(self, VerificarVotanteForm):
        return super().form_valid(VerificarVotanteForm)

class ErrorVotante(TemplateView):
    template_name='error.html'

class agradecimientoVotante(TemplateView):
    template_name='gracias.html'


class EleccionCandidato(ListView):
    template_name = 'candidatos.html'
    context_object_name = 'candidatos'
    queryset = Candidato.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
            context = super(EleccionCandidato,self).get_context_data(**kwargs)
            try:
                user = Votantes.objects.get(cedula=self.kwargs['cc'])
                if user:
                    context["candidatos"] = self.queryset
                    context["user"] = user
                else:
                    context["mensaje"] = "No cuenta con los privilegios para acceder"
            except ObjectDoesNotExist:
                context["mensaje"] = "No cuenta con los privilegios para acceder"
            return context

    """"def get_queryset(self):
        candidatos = Candidato.objects.all()
        try:
            user = Votantes.objects.get(cedula=self.kwargs['cc'])
            if user:
                voto = { 'candidatos':candidatos , 'user':user}
                return voto
            else:
                error = {'mensaje':"402"}
                print(error)
                return  error
        except ObjectDoesNotExist:
            return  HttpResponseRedirect(reverse('votante_app:error-votante')) """



    def post(self,request,*args,**kwargs):
        elector = request.POST['cc']
        elector = Votantes.objects.get(cedula=elector)
        elector.estado_voto=True
        elector.save()
        candidato_seleccionado = request.POST['candi']
        print('candi 1', candidato_seleccionado)
        candidato_elegido = Candidato.objects.get(id=candidato_seleccionado)
        print('candi 2', candidato_elegido)
        try:
            voto = eleccion.objects.create(
                candidato=candidato_elegido,
                votante=elector
            )
        except IntegrityError:
            return  HttpResponseRedirect(reverse('votante_app:error-votante'))
        return  HttpResponseRedirect(reverse('votante_app:agradecimiento-votante'))



class reporteVotacion(LoginRequiredMixin,TemplateView):
    template_name='jurados/reporte.html'
    login_url = reverse_lazy('users_app:login')
    def  get_votos_candidato(self):
        total_votos = eleccion.objects.values(
            'candidato_id'
        ).annotate(data=Count('candidato_id'))
        return total_votos


    def get_context_data(self, **kwargs):
        total_parcial = eleccion.objects.all().count()
        context = super().get_context_data(**kwargs)
        context ['panel'] = 'Panel de Administrador'
        lista_votos=[]
        porcentaje_votosPie=[]
        total_votos = self.get_votos_candidato()
        for i in range(len(total_votos)):
            nombre = total_votos[i]['candidato_id']=Candidato.objects.get(id=total_votos[i]['candidato_id']).nombre
            total_votos[i]['name']=total_votos[i].pop('candidato_id')
            total_votos[i]['data']=[total_votos[i]['data']]
            total_votos[i]['y']=((total_votos[i]['data'][0]*100)/total_parcial)
            porcentaje_votosPie.append([
                nombre,(total_votos[i]['data'][0]*100/total_parcial)
                ])
            lista_votos.append(total_votos[i])
        context ['graph_votos_candidato'] =lista_votos
        context ['pie_votos_candidato'] =porcentaje_votosPie
        return context
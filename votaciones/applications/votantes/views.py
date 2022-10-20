import datetime
import numpy as np
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
from .models import Votantes, tipo_candidato
from applications.candidatos.models import Candidato,eleccion




class VerificarVotante(FormView):
    template_name = 'eleccion.html'
    form_class = VerificarVotanteForm
    success_url = 'candidatos.html'

    def post(self,request,*args, **kwargs):
        cedula_user =request.POST['cedula']
        email_user = request.POST['email']
        try:
            user = Votantes.objects.get(cedula=cedula_user)
            if user:
                if user.estado_voto==True:
                    message = 'El usuario registrado con la cedula #'+ '   ' + user.cedula+ '  '+' ya ha realizado la votación, si no fuiste tú'
                    return render(request,'error.html', {'message_error': message})
                else:
                    if user.email.strip().lower()==email_user.strip().lower():
                        return HttpResponseRedirect(reverse('votante_app:eleccion-votante',kwargs={'cc':user.cedula}))
                    else:
                        message = 'Lo sentimos usted no brindo las credenciales correctas, verificar cédula y correo electrónico.'
                        return render(request,'error.html', {'message_error': message})
        except ObjectDoesNotExist:
                    return render(
                        request,
                        'error.html',
                        {'message_error': 'Lo sentimos el numero de cedula  no se encuntra registrado, comunicarse con votacionesContigo@gmail.com para más información'}
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
                    candidatos = Candidato.objects.filter(tipo_candidato_id=user.tipo_candidato.id)
                    context["candidatos"] = candidatos
                    context["user"] = user
                else:
                    context["mensaje"] = "No cuenta con los privilegios para acceder"
            except ObjectDoesNotExist:
                context["mensaje"] = "No cuenta con los privilegios para acceder"
            return context



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
    login_url = reverse_lazy('users_app:login-user')

    def  get_votos_candidato(self):
        total_votos = eleccion.objects.values(
            'candidato_id',
        ).annotate(data=Count('candidato_id')).filter(candidato__tipo_candidato=2).order_by('candidato_id')
        return total_votos

    def get_votos_candidate_for_hour(self):
        #fec='2021-07-11'
        #fecha = datetime.datetime.strptime(fec,"%Y-%m-%d").date()
        cantVotosHora=[]
        ArrayVotosCandidato1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato5=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato6=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato7=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato8=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato10=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato11=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato12=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato13=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato14=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato15=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato16=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato17=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato18=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato19=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato20=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato21=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato22=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato23=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato24=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato25=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato26=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato27=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato28=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato29=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato30=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidato31=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ArrayVotosCandidatosDocentes= np.zeros((30,24))
        #ArrayVotosCandidatosDocentes[29][23]=1

        for i in range(23):
            hora1=str(i)+':00:00'
            hora2=str(i)+':59:59'
            """votosHora= eleccion.objects.values('candidato_id').filter(
                created__time__range=(hora1,hora2),
                created__date=fecha).annotate(
                    data=Count('candidato_id'
                            )
                    )"""
            votosHora= eleccion.objects.values('candidato_id').filter(
            created__time__range=(hora1,hora2),candidato__tipo_candidato=2).annotate(
                data=Count('candidato_id')
                )
            if votosHora.exists():
                for j in range(len(votosHora)):
                    print(j, votosHora[j]['candidato_id'])
                    if votosHora[j]['candidato_id']>0:
                        ArrayVotosCandidatosDocentes[votosHora[j]['candidato_id']-1][i] = votosHora[j]['data']
                    else:
                        ArrayVotosCandidatosDocentes[votosHora[j]['candidato_id']][i] = votosHora[j]['data']
                    
                    """if votosHora[j]['candidato_id']==1:
                        ArrayVotosCandidato1[i]=votosHora[j]['data']
                    #if votosHora[j]['candidato_id']!=1:
                     #   ArrayVotosCandidato1.append(0)

                    if votosHora[j]['candidato_id']==2:
                        ArrayVotosCandidato2[i]=votosHora[j]['data']
                    #if votosHora[j]['candidato_id']!=2:
                    #    ArrayVotosCandidato2.append(0)

                    if votosHora[j]['candidato_id']==3:
                        ArrayVotosCandidato3[i]=votosHora[j]['data']
                        print('hola RRR')
                    #if votosHora[j]['candidato_id']!=3:
                    #    ArrayVotosCandidato3.append(0)

                    if votosHora[j]['candidato_id']==4:
                        ArrayVotosCandidato4[i]=votosHora[j]['data']
                    #if votosHora[j]['candidato_id']!=4:
                    #    ArrayVotosCandidato4.append(0)

                    if votosHora[j]['candidato_id']==5:
                        ArrayVotosCandidato5[i]=votosHora[j]['data']
                    #if votosHora[j]['candidato_id']!=5:
                    #    ArrayVotosCandidato5.append(0)
                    
            else:
                ArrayVotosCandidato1[i]=0
                ArrayVotosCandidato2[i]=0
                ArrayVotosCandidato3[i]=0
                ArrayVotosCandidato4[i]=0
                ArrayVotosCandidato5[i]=0
        print('lista 1 ', ArrayVotosCandidato1)
        print('lista 2 ', ArrayVotosCandidato2)
        print('lista 3 ', ArrayVotosCandidato3)
        print('lista 4 ', ArrayVotosCandidato4)
        print('lista 5 ', ArrayVotosCandidato5)
        print(ArrayVotosCandidatosDocentes,'\\\\\**&&&')
        print(ArrayVotosCandidatosDocentes[29][19],'\\\\\**&&&')
        """
        ListasVotosPorCandidato = [ArrayVotosCandidato1,ArrayVotosCandidato2,ArrayVotosCandidato3,ArrayVotosCandidato4,ArrayVotosCandidato5]
        return ArrayVotosCandidatosDocentes

    def get_context_data(self, **kwargs):
        total_parcial = eleccion.objects.all().count()
        context = super().get_context_data(**kwargs)
        context ['panel'] = 'Panel de Administrador'
        lista_votos=[]
        porcentaje_votosPie=[]
        serieVotoshora=[]
        votosHoraCandidato1=[]
        votosHoraCandidato2=[]
        votosHoraCandidato3=[]
        votosHoraCandidato4=[]
        votosHoraCandidato5=[]
        votosHoraCandidato6=[]
        votosHoraCandidato7=[]
        votosHoraCandidato8=[]
        votosHoraCandidato9=[]
        votosHoraCandidato10=[]
        votosHoraCandidato11=[]
        votosHoraCandidato12=[]
        votosHoraCandidato13=[]
        votosHoraCandidato14=[]
        votosHoraCandidato15=[]
        votosHoraCandidato16=[]
        votosHoraCandidato17=[]
        votosHoraCandidato18=[]
        votosHoraCandidato19=[]
        votosHoraCandidato20=[]
        votosHoraCandidato21=[]
        votosHoraCandidato22=[]
        votosHoraCandidato23=[]
        votosHoraCandidato24=[]
        votosHoraCandidato25=[]
        votosHoraCandidato26=[]
        votosHoraCandidato27=[]
        votosHoraCandidato28=[]
        votosHoraCandidato29=[]
        votosHoraCandidato30=[]
        listasVotosHora = self.get_votos_candidate_for_hour()
        total_votos = self.get_votos_candidato()
        for j in range(24):
            h=j
            if j==24:
                h=-1
            votosHoraCandidato1.append([str(j)+' - '+str(h+1),listasVotosHora[0][j]])
            votosHoraCandidato2.append([str(j)+' - '+str(h+1),listasVotosHora[1][j]])
            votosHoraCandidato3.append([str(j)+' - '+str(h+1),listasVotosHora[2][j]])
            votosHoraCandidato4.append([str(j)+' - '+str(h+1),listasVotosHora[3][j]])
            votosHoraCandidato5.append([str(j)+' - '+str(h+1),listasVotosHora[4][j]])
            votosHoraCandidato6.append([str(j)+' - '+str(h+1),listasVotosHora[5][j]])
            votosHoraCandidato7.append([str(j)+' - '+str(h+1),listasVotosHora[6][j]])
            votosHoraCandidato8.append([str(j)+' - '+str(h+1),listasVotosHora[7][j]])
            votosHoraCandidato9.append([str(j)+' - '+str(h+1),listasVotosHora[8][j]])
            votosHoraCandidato10.append([str(j)+' - '+str(h+1),listasVotosHora[9][j]])
            votosHoraCandidato11.append([str(j)+' - '+str(h+1),listasVotosHora[10][j]])
            votosHoraCandidato12.append([str(j)+' - '+str(h+1),listasVotosHora[11][j]])
            votosHoraCandidato13.append([str(j)+' - '+str(h+1),listasVotosHora[12][j]])
            votosHoraCandidato14.append([str(j)+' - '+str(h+1),listasVotosHora[13][j]])
            votosHoraCandidato15.append([str(j)+' - '+str(h+1),listasVotosHora[14][j]])
            votosHoraCandidato16.append([str(j)+' - '+str(h+1),listasVotosHora[15][j]])
            votosHoraCandidato17.append([str(j)+' - '+str(h+1),listasVotosHora[16][j]])
            votosHoraCandidato18.append([str(j)+' - '+str(h+1),listasVotosHora[17][j]])
            votosHoraCandidato19.append([str(j)+' - '+str(h+1),listasVotosHora[18][j]])
            votosHoraCandidato20.append([str(j)+' - '+str(h+1),listasVotosHora[19][j]])
            votosHoraCandidato21.append([str(j)+' - '+str(h+1),listasVotosHora[20][j]])
            votosHoraCandidato22.append([str(j)+' - '+str(h+1),listasVotosHora[21][j]])
            votosHoraCandidato23.append([str(j)+' - '+str(h+1),listasVotosHora[22][j]])
            votosHoraCandidato24.append([str(j)+' - '+str(h+1),listasVotosHora[23][j]])
            votosHoraCandidato25.append([str(j)+' - '+str(h+1),listasVotosHora[24][j]])
            votosHoraCandidato26.append([str(j)+' - '+str(h+1),listasVotosHora[25][j]])
            votosHoraCandidato27.append([str(j)+' - '+str(h+1),listasVotosHora[26][j]])
            votosHoraCandidato28.append([str(j)+' - '+str(h+1),listasVotosHora[27][j]])
            votosHoraCandidato29.append([str(j)+' - '+str(h+1),listasVotosHora[28][j]])
            votosHoraCandidato30.append([str(j)+' - '+str(h+1),listasVotosHora[29][j]])

        ArrayVotosHoraCandidato=[
            votosHoraCandidato1,
            votosHoraCandidato2,
            votosHoraCandidato3,
            votosHoraCandidato4,
            votosHoraCandidato5,
            votosHoraCandidato6,
            votosHoraCandidato7,
            votosHoraCandidato8,
            votosHoraCandidato9,
            votosHoraCandidato10,
            votosHoraCandidato11,
            votosHoraCandidato12,
            votosHoraCandidato13,
            votosHoraCandidato14,
            votosHoraCandidato15,
            votosHoraCandidato16,
            votosHoraCandidato17,
            votosHoraCandidato18,
            votosHoraCandidato19,
            votosHoraCandidato20,
            votosHoraCandidato21,
            votosHoraCandidato22,
            votosHoraCandidato23,
            votosHoraCandidato24,
            votosHoraCandidato25,
            votosHoraCandidato26,
            votosHoraCandidato27,
            votosHoraCandidato28,
            votosHoraCandidato29,
            votosHoraCandidato30
            ]
        for i in range(len(total_votos)):
            print('prueva votos',total_votos[i])
            dataHour= total_votos[i]['candidato_id']
            nombre = total_votos[i]['candidato_id']=Candidato.objects.get(id=total_votos[i]['candidato_id']).nombre
            total_votos[i]['name']=total_votos[i].pop('candidato_id')
            total_votos[i]['y']=total_votos[i]['data']
            total_votos[i]['data']=[total_votos[i]['data']]
            total_votos[i]['drilldown']=total_votos[i]['name']
            porcentaje_votosPie.append([
                nombre,(total_votos[i]['data'][0]*100/total_parcial)
                ])
            lista_votos.append(total_votos[i])
            serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[int(dataHour)-1]
            })
        print('viejaseria',lista_votos)
        print('nueva serie',serieVotoshora)
        context ['graph_votos_candidato'] =lista_votos
        context ['pie_votos_candidato'] =porcentaje_votosPie
        context ['graph_votos_hora_candidato'] =serieVotoshora

        return context

class TablaVotantesView(LoginRequiredMixin,TemplateView):
    template_name = "jurados/votantes.html"
    login_url = reverse_lazy('users_app:login-user')
    queryset = eleccion.objects.all().filter(votante__estado_voto=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(' query..',self.queryset)
        context["datos"] = eleccion.objects.all().filter(votante__estado_voto=True)
        total_votos_momento =eleccion.objects.count()
        porcentualMomento = "{0:.2f}".format(((total_votos_momento *100)/Votantes.objects.count()))
        context["data"] = [float(porcentualMomento)]
        return context

class IndexTemporal(TemplateView):
    template_name = "temporal.html"
    
    
class reporteVotacionDirectivo(LoginRequiredMixin,TemplateView):
    template_name='jurados/reporte.html'
    login_url = reverse_lazy('users_app:login-user')

    def  get_votos_candidato(self):
        total_votos = eleccion.objects.values(
            'candidato_id',
        ).annotate(data=Count('candidato_id')).filter(candidato__tipo_candidato=3).order_by('candidato_id')
        return total_votos

    def get_votos_candidate_for_hour(self):
        #fec='2021-07-11'
        #fecha = datetime.datetime.strptime(fec,"%Y-%m-%d").date()
        cantVotosHora=[]
        ArrayVotosCandidatosDocentes= np.zeros((7,24))
        #ArrayVotosCandidatosDocentes[29][23]=1

        for i in range(23):
            hora1=str(i)+':00:00'
            hora2=str(i)+':59:59'
            """votosHora= eleccion.objects.values('candidato_id').filter(
                created__time__range=(hora1,hora2),
                created__date=fecha).annotate(
                    data=Count('candidato_id'
                            )
                    )"""
            votosHora= eleccion.objects.values('candidato_id').filter(
            created__time__range=(hora1,hora2),candidato__tipo_candidato=3).annotate(
                data=Count('candidato_id')
                )
            if votosHora.exists():
                for j in range(len(votosHora)):
                    print(votosHora[j]['data'])
                    if votosHora[j]['candidato_id']==33:
                         ArrayVotosCandidatosDocentes[0][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==34:
                         ArrayVotosCandidatosDocentes[1][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==35:
                         ArrayVotosCandidatosDocentes[2][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==36:
                         ArrayVotosCandidatosDocentes[3][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==37:
                         ArrayVotosCandidatosDocentes[4][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==38:
                         ArrayVotosCandidatosDocentes[5][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==39:
                         ArrayVotosCandidatosDocentes[6][i] = votosHora[j]['data']
        print(ArrayVotosCandidatosDocentes)         
        return ArrayVotosCandidatosDocentes

    def get_context_data(self, **kwargs):
        total_parcial = eleccion.objects.all().count()
        context = super().get_context_data(**kwargs)
        context ['panel'] = 'Panel de Administrador'
        lista_votos=[]
        porcentaje_votosPie=[]
        serieVotoshora=[]
        votosHoraCandidato1=[]
        votosHoraCandidato2=[]
        votosHoraCandidato3=[]
        votosHoraCandidato4=[]
        votosHoraCandidato5=[]
        votosHoraCandidato6=[]
        votosHoraCandidato7=[]

        listasVotosHora = self.get_votos_candidate_for_hour()
        total_votos = self.get_votos_candidato()
        for j in range(24):
            h=j
            if j==24:
                h=-1
            votosHoraCandidato1.append([str(j)+' - '+str(h+1),listasVotosHora[0][j]])
            votosHoraCandidato2.append([str(j)+' - '+str(h+1),listasVotosHora[1][j]])
            votosHoraCandidato3.append([str(j)+' - '+str(h+1),listasVotosHora[2][j]])
            votosHoraCandidato4.append([str(j)+' - '+str(h+1),listasVotosHora[3][j]])
            votosHoraCandidato5.append([str(j)+' - '+str(h+1),listasVotosHora[4][j]])
            votosHoraCandidato6.append([str(j)+' - '+str(h+1),listasVotosHora[5][j]])
            votosHoraCandidato7.append([str(j)+' - '+str(h+1),listasVotosHora[6][j]])

        ArrayVotosHoraCandidato=[
            votosHoraCandidato1,
            votosHoraCandidato2,
            votosHoraCandidato3,
            votosHoraCandidato4,
            votosHoraCandidato5,
            votosHoraCandidato6,
            votosHoraCandidato7,
            ]
        for i in range(len(total_votos)):
            print('prueva votos',total_votos[i])
            dataHour= total_votos[i]['candidato_id']
            nombre = total_votos[i]['candidato_id']=Candidato.objects.get(id=total_votos[i]['candidato_id']).nombre
            total_votos[i]['name']=total_votos[i].pop('candidato_id')
            total_votos[i]['y']=total_votos[i]['data']
            total_votos[i]['data']=[total_votos[i]['data']]
            total_votos[i]['drilldown']=total_votos[i]['name']
            porcentaje_votosPie.append([
                nombre,(total_votos[i]['data'][0]*100/total_parcial)
                ])
            lista_votos.append(total_votos[i])
            if dataHour==33:
                 serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[0]
            })        
            if dataHour==34:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[1]
            })
            if dataHour==35:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[2]
            })
            if dataHour==36:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[3]
            })
            if dataHour==37:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[4]
            })
            if dataHour==38:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[5]
            }) 
            if dataHour==39:
                serieVotoshora.append({
                    'name':total_votos[i]['name'],
                    'id':total_votos[i]['name'],
                    'data':ArrayVotosHoraCandidato[6]
                })
        print('viejaseria',lista_votos)
        print('nueva serie',serieVotoshora)
        context ['graph_votos_candidato'] =lista_votos
        context ['pie_votos_candidato'] =porcentaje_votosPie
        context ['graph_votos_hora_candidato'] =serieVotoshora

        return context

class reporteVotacionAdministrativo(LoginRequiredMixin,TemplateView):
    template_name='jurados/reporte.html'
    login_url = reverse_lazy('users_app:login-user')

    def  get_votos_candidato(self):
        total_votos = eleccion.objects.values(
            'candidato_id',
        ).annotate(data=Count('candidato_id')).filter(candidato__tipo_candidato=1).order_by('candidato_id')
        return total_votos

    def get_votos_candidate_for_hour(self):
        cantVotosHora=[]
        ArrayVotosCandidatosDocentes= np.zeros((2,24))
        for i in range(23):
            hora1=str(i)+':00:00'
            hora2=str(i)+':59:59'
            votosHora= eleccion.objects.values('candidato_id').filter(
            created__time__range=(hora1,hora2),candidato__tipo_candidato=1).annotate(
                data=Count('candidato_id')
                )
            if votosHora.exists():
                for j in range(len(votosHora)):
                    print(votosHora[j]['data'])
                    if votosHora[j]['candidato_id']==31:
                         ArrayVotosCandidatosDocentes[0][i] = votosHora[j]['data']
                    if votosHora[j]['candidato_id']==32:
                         ArrayVotosCandidatosDocentes[1][i] = votosHora[j]['data']
        return ArrayVotosCandidatosDocentes

    def get_context_data(self, **kwargs):
        total_parcial = eleccion.objects.all().count()
        context = super().get_context_data(**kwargs)
        context ['panel'] = 'Panel de Administrador'
        lista_votos=[]
        porcentaje_votosPie=[]
        serieVotoshora=[]
        votosHoraCandidato1=[]
        votosHoraCandidato2=[]

        listasVotosHora = self.get_votos_candidate_for_hour()
        total_votos = self.get_votos_candidato()
        for j in range(24):
            h=j
            if j==24:
                h=-1
            votosHoraCandidato1.append([str(j)+' - '+str(h+1),listasVotosHora[0][j]])
            votosHoraCandidato2.append([str(j)+' - '+str(h+1),listasVotosHora[1][j]])

        ArrayVotosHoraCandidato=[
            votosHoraCandidato1,
            votosHoraCandidato2,
            ]
        for i in range(len(total_votos)):
            print('prueva votos',total_votos[i])
            dataHour= total_votos[i]['candidato_id']
            nombre = total_votos[i]['candidato_id']=Candidato.objects.get(id=total_votos[i]['candidato_id']).nombre
            total_votos[i]['name']=total_votos[i].pop('candidato_id')
            total_votos[i]['y']=total_votos[i]['data']
            total_votos[i]['data']=[total_votos[i]['data']]
            total_votos[i]['drilldown']=total_votos[i]['name']
            porcentaje_votosPie.append([
                nombre,(total_votos[i]['data'][0]*100/total_parcial)
                ])
            lista_votos.append(total_votos[i])
            if dataHour==31:
                 serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[0]
            })        
            if dataHour==32:
                serieVotoshora.append({
                'name':total_votos[i]['name'],
                'id':total_votos[i]['name'],
                'data':ArrayVotosHoraCandidato[1]
            })
        print('viejaseria',lista_votos)
        print('nueva serie',serieVotoshora)
        context ['graph_votos_candidato'] =lista_votos
        context ['pie_votos_candidato'] =porcentaje_votosPie
        context ['graph_votos_hora_candidato'] =serieVotoshora

        return context
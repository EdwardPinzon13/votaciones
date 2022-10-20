from datetime import datetime

from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache

from django.views.generic.base import View
from django.views.generic.edit import  FormView
from django.urls import reverse_lazy
from .forms import LoginForm



class LoginUser(FormView):
    template_name= 'jurados/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('votante_app:tabla-votos')


    def form_valid(self,form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        print('user', user)
        print('contexto request', self.request)
        all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
        """if all_sessions.exists():
            for session in all_sessions:
                print('sss',session.session_data)
                print('sss2',session.get_decoded())
                session_datas = session.get_decoded()
                print('sessiones',session_datas)
                if user.id == int(session_datas.get('_auth_user_id')):
                    session.delete()"""
        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class  LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users_app:login-user'))

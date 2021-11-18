
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from datetime import datetime

from django.urls.base import reverse_lazy
class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/forbidden')
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['date_now']= datetime.now()
        context['user']= 'gabot'
        return context

class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('')
        return self.url_redirect
    
    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.url_redirect())
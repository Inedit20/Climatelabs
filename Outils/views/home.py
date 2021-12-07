from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext
#from ..models import 
#from  stories.filters import CasesFilter
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm




def Introduction(request):
     template_name = 'Pages/Introduction.html'
     return render(request, template_name)





def Guide(request):
     template_name = 'Pages/guide.html'
     return render(request, template_name)






def documentation(request):
     template_name = 'Pages/doc.html'
     return render(request, template_name)

def roles(request):
     template_name = 'Pages/roles.html'
     return render(request, template_name)

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import os
from django.conf import settings
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.http import FileResponse
from django.http import Http404
# Create your views here.
from .models import Person
from datetime import datetime
#from pytz import timezone
from django.utils import timezone

#server_timezone = timezone('Europe/Moscow')


def download(request,file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    if os.path.exists(file_path):
        clientweb = request.META['HTTP_USER_AGENT']
        p = Person(client=clientweb)
        p.save()
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    raise  Http404





def index(request):
    clients =Person.objects.all().order_by('date')  #Person.objects.filter(date=timezone.now()).order_by('date')          #
    #clients = Person.objects.raw("SELECT id,client, date FROM posts_person order by id desc")

    clientsgroup = Person.objects.raw("SELECT id, client, count(*) count , date FROM posts_person group by client")

    data = {"clients": clients, "group":clientsgroup}
    return render(request, "index.html", context=data)




from django.conf.urls import url

from . import views

#app_name = 'riddles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^download/(?P<file_name>.+)$', views.download, name='download'),
    #url(r'^download/(?P<filename>[-\w_\\-\\.]+)$', views.download_pdf, name='download'),
    #url(r'^somefile/(?P<filename>[-\w_\\-\\.]+)$', views.SomeFileDownloadView.as_view(), name='somefile-download'),
]

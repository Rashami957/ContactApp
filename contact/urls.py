from django.template.context_processors import static
from django.urls import path

from myfirstcontactapp import settings
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contact'

urlpatterns = [
                  path('', views.contact_list, name='contact_list'),
                  path('person/<int:pk>', views.contact_detail, name='contact_detail'),
                  path('person/new', views.contact_new, name='contact_new'),
                  path('person/<int:pk>/edit', views.contact_edit, name='contact_edit'),
                  path('person/<int:pk>/delete', views.contact_delete, name='contact_delete'),
                  path('', views.contact_search, name='contact_list')

              ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


###### API REST ######
# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    model = User
#
#class GroupViewSet(viewsets.ModelViewSet):
#    model = Group
#
#    # Routers provide an easy way of automatically determining the URL conf.
#    router = routers.DefaultRouter()
#    router.register(r'users', UserViewSet)
#    router.register(r'groups', GroupViewSet)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musica.views.home', name='home'),
    # url(r'^musica/', include('musica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bodeapp/listamusicos', 'bodeapp.views.lista_musicos', name=u'lista_musicos'),
    url(r'^bodeapp/search', 'bodeapp.views.search', name=u'search'),

    ### API ###
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

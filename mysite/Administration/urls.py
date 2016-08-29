from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^createProject/$', views.createProject, name='createProject'),
    url(r'^createBD/$', views.createBD, name='createBD'),
    url(r'^showAtributes/$', views.showAtributes, name='showAtributes'),
    url(r'^showAtributes2/$', views.showAtributes2, name='showAtributes2'),
    url(r'^showAtributes3/(?P<database_name>[-\w]+)/$',views.showAtributes3, name='showAtributes3'),
    url(r'^showAtributes4/(?P<database_name>[-\w]+)/$',views.showAtributes4, name='showAtributes4'),
    url(r'^createAtribute/(?P<database_name>[-\w]+)/$', views.createAtribute, name='createAtribute'),
    url(r'^showData/$', views.showData, name='showData'),
    url(r'^showData2/$', views.showData2, name='showData2'),
    url(r'^deleteData/(?P<database_name>[-\w]+)/(?P<data>\w+)/$', views.deleteData, name='deleteData'),
    url(r'^createData/$', views.createData, name="createData"),
    url(r'^deleteProject/(?P<base>\w+)/$', views.deleteProject, name="deleteProject"),
    url(r'^deleteAtribute/(?P<database_name>[-\w]+)/(?P<atributo>\w+)/$', views.deleteAtribute, name="deleteAtribute"),
    url(r'^getCSVData/(?P<database_name>[-\w]+)/$', views.getCSVData, name="getCSVData"),
    url(r'^createData/(?P<database_name>[-\w]+)/$', views.createData, name="createData"),
    url(r'^createData2/(?P<database_name>[-\w]+)/$', views.createData2, name="createData2"),
    url(r'^modifyAtribute/(?P<database_name>[-\w]+)/(?P<atributo>\w+)/$', views.modifyAtribute, name="modifyAtribute"),
    url(r'^modifyAtribute2/(?P<database_name>[-\w]+)/(?P<atributoName>[-\w]+)/$', views.modifyAtribute2, name="modifyAtribute2"),
    url(r'^modifyData/(?P<database_name>[-\w]+)/(?P<data>\w+)/$', views.modifyData, name="modifyData"),
    url(r'^modifyData2/(?P<database_name>[-\w]+)/(?P<Id>\w+)/$', views.modifyData2, name="modifyData2"),
    url(r'^seleccionarAccion/(?P<database_name>[-\w]+)/$', views.seleccionarAccion, name='seleccionarAccion'),
    url(r'^showData3/(?P<database_name>[-\w]+)/$', views.showData3, name='showData3'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^chart2/(?P<database_name>[-\w]+)/$', views.chart2, name='chart2'),
    url(r'^chartM/$', views.chartM, name='chartM'),
    url(r'^chart2M/(?P<database_name>[-\w]+)/$', views.chart2M, name='chart2M'),
    url(r'^chartD/$', views.chartD, name='chartD'),
    url(r'^chart2D/(?P<database_name>[-\w]+)/$', views.chart2D, name='chart2D'),
]

#(?P<nombreProyecto>[a-z]+[A-Z]*[0-9]*)
#(?P<base>\d+)/

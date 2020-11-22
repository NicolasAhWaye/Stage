from django.conf.urls import url
from . import views  # import views so we can use them in urls.

app_name = 'inventaire'
urlpatterns = [
    url(r'^$', views.couverture, name='couverture'),
    url(r'^table/$', views.table, name='table'),
    url(r'^ajouter/$', views.ajouter, name='ajouter'),
]

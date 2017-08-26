from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^.*$', views.submit, name='else')
]
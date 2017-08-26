from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^submit/', views.submit, name='submit'),
    url(
    	r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
            permanent=False),
        name="favicon"
        ),
    url(r'^.*$', views.submit, name='else')
]
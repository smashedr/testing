from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django_config.settings import STATIC_URL

import home.views as home

urlpatterns = [
    url(r'^$', home.home, name='home'),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url=STATIC_URL + 'favicon.ico'
    )),
    url(r'^python/', home.python, name='python'),
    url(r'^django/', home.django, name='django'),
    url(r'^admin/', admin.site.urls, name="django_admin"),
]

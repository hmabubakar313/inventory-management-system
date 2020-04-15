from django.conf.urls import url
from .views import*

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_laptop$', display_laptop ,name='display_laptop'),
     url(r'^display_desktop$', desktop ,name='desktop'),
      url(r'^display_mobile$', mobile ,name='mobile'),
]

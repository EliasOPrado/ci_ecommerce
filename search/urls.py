from .views import do_search
from django.conf.urls import url

urlpatterns = [
    url(r'^$', do_search, name="search")
]

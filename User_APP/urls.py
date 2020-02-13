from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='UserApp/login.html')),
    url(r'^logout/$', LogoutView.as_view(template_name='UserApp/logout.html')),
    url(r'^register/$', views.register, name='register')
    ]









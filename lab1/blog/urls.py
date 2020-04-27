from django.contrib.auth import views as auth
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url( r'^login/$',auth.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', auth.LogoutView, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret1, name='secret'),
    path('secret2/', views.Secret2.as_view(), name='secret2'),

]
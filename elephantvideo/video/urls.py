from django.urls import path
from . import views


app_name = 'video'
urlpatterns = [
    # post views
    path('', views.lista_canais, name='lista_canais'),
    path('companies/', views.companies, name='companies'),
    path('channels/', views.channels, name='channels'),
    path('busca/', views.busca, name='busca'),
    path('<slug:channel>/<int:day>/<int:month>/<int:year>/<int:hour>/<int:minute>/', views.video, name='video'),

]

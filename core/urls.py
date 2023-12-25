from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('screener/<str:title>/<str:clause>', views.screener, name='screener'),
    path('pricing/', views.pricing, name='pricing'),
    path('pay/<int:price>', views.pay, name='pay'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
	path('get_data/<str:title>/<str:clause>', views.get_data, name='get_data'),
    path('market_is_open/<str:date>', views.market_is_open, name="market_is_open"),
    #path('options/', views.options, name='options')
]

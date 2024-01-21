from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('charts/', views.charts_view, name='charts'),
    path('tables/', views.tables_view, name='tables'),
    path('insert/', views.insert, name='insert'),
    
    path('create_company/', views.create_company, name='create_company'),

    path('create_product/', views.create_product, name='create_product'),
    
    path('create_sales/', views.create_sales, name='create_sales'),

    # path('create_stores/', views.create_stores, name='create_stores'),

]
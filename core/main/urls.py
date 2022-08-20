from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('<int:id>', views.BrandListView.as_view(), name='brand'),
    path('prod/<int:id>', views.ProdListView.as_view(), name='prod'),


]
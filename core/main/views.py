from django.shortcuts import render
from .models import Category, Brand, Prod
from django.views.generic import ListView
# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cat = Category.objects.all()
        return render(request, self.template_name, {'cat':cat})


class BrandListView(ListView):
    template_name = 'brand.html'

    def get(self, request, id):
        brand = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'brand':brand})



class ProdListView(ListView):
    template_name = 'prod.html'

    def get(self, request, id):
        prod = Brand.objects.filter(pk=id)
        return render(request, self.template_name, {'prod':prod})
from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class BaseView(View):
    views = {}

    views['category'] = category.objects.all()
    views['brand'] = brand.objects.all()
    views['contact'] = contactinfo.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = slider.objects.all()
        self.views['ad'] = ad.objects.all()
        self.views['product'] = product.objects.all()
        return render(request,'index.html',self.views)
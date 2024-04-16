from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from django.views.generic import CreateView

from .forms import shippingDetailsForm
from rest_framework import viewsets
from .models import ShippingDetail
from .serializers import ShippingDetailSerializer

class ShippingCreateView(CreateView):
 model = ShippingDetail
 form_class = shippingDetailsForm
 template_name = "shipping_form.html"
 success_url = "/" # change this to your desired url


class ShippingDetailViewSet(viewsets.ModelViewSet):
 queryset = ShippingDetail.objects.all()
 serializer_class = ShippingDetailSerializer
 





# @api_view(["GET"])
# def product_list(request):
#   products = Product.objects.all()
#   serializer = ProductSerializer(products, many=True)
#   return Response(serializer.data)
# def create_product(request):
   
#  if request.method == "POST":
#     form = ProductForm(request.POST, request.FILES)
#     if form.is_valid():
#      form.save()
#      return redirect("/products/productslist/")
#  else:
#       form = ProductForm()
#  return render(request, "products/create_product.html", {"form": form})



# def product_create_API(request):
#    serializer = ProductSerializer(data=request.data)
#    if serializer.is_valid():
#       product = serializer.save()
#       return Response(serializer.data, status=201)
#    return Response(serializer.errors, status=400)




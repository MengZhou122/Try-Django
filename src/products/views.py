from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import ProductForm, RawProductForm

from .models import Product

def product_update_view(request, my_id):
    # initial_data = {
    #     'title': "My this awesome title"
    # }
    obj = get_object_or_404(Product, id=my_id)
    print(id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             #add ** to turn the date to arguments
#         else:
#             print(my_form.errors)
#     context = {'form': my_form}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print(request.GET['title'])
#     #print(request.POST)
#     if (request.method == 'POST'):
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         #Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}
    return render(request, "products/product_create.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     #get the product object by id/change manually

#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = {'object': obj}
#     return render(request, "products/product_detail.html", context)

def product_detail_view(request,my_id):
    #obj = Product.objects.get(id=my_id) #if the object with my_id is not exist, will raise DoesNotExist error  
    obj = get_object_or_404(Product, id=my_id) #handle set exception, equivalent to the try block below

    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    
    context = {'object': obj}
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    #POST request
    if request.method == "POST": #comfirming delete
        obj.delete()
        return redirect('../../')
    context = {'object': obj}
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)
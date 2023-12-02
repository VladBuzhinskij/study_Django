from django.shortcuts import render, get_object_or_404
from itertools import chain
from .models import Category, SubCategory, Product
from cart.forms import CartAddProductForm

def product_list(request, subcategory_slug=None):
    category= None
    categories = Category.objects.all()
    subcategory = None
    subcategories = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    # print(type(products))
    cate = Category.objects.filter(slug=subcategory_slug)
    if subcategory_slug:
        productss=products
        if len(cate)>0:

            category = get_object_or_404(Category, slug=subcategory_slug)
            subcategorys = SubCategory.objects.filter(available=True)
            subcategorys = list(subcategorys.filter(category=category))
            products = productss.filter(subcategory=subcategorys[0])
            print(products)
            for i in range(1,len(subcategorys)):
                print()
                
                products = productss.filter(subcategory=subcategorys[i]) | products
                print(products)
        else:
            print("tut")
            subcategorys = get_object_or_404(SubCategory, slug=subcategory_slug)
            products = products.filter(subcategory=subcategorys)
            # print(subcategorys)
        # print(category)
        # print(subcategorys)
        
        
        
        
        
        # print((subcategorys))
        # subcategorys = subcategorys.filter(category=category)
        # print(list(subcategorys)[0])
        # subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        print("3111")
        
        # products = products.filter(subcategory=list(subcategorys)[0])
    # if subcategory_slug:
    #     
    #     # print(subcategory)
    #     products = products.filter(subcategory=subcategory)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'subcategory': subcategory,
                   'subcategories': subcategories,
                   'products': products})

def product_listCAT(request,category_slug=None):
    category= None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
      
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

# Create your views here.

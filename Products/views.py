from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Products
#from category.models import Category
#from carts.models import CartItem
#from Carts.views import_cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def Products(request, category_slug=None):
    Categories = None
    products = None
    
if Category_Slug !=None:
    Categories = get_object_or_404(Category, slug = Category_slug)
    products = Products.objects.filter(Category=Categories, status=True)
    paginator = Paginator(products, 3)
    pages = request.GET.get('page')
    page_products = paginator.get_page(page)
    Product_count = len(paged_products)

else:
    products= Products.objects.all().filter(Status=True).order_by('id')
    paginator = Paginator(products, 3)
    pages = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = len(paged_products)
    
context = {
    'products': paged_products,
    "product_count": product_count
}
def Product_list(request):
    all_Products = Products.objects.all()  # Capital P
    return render(request, 'products/products.html', {'products': all_Products})

def Product_detail(request, category_slug, product_slug):
    try:
        products =Products.objects.get(category__slug=category_slug, slug=product_slug)
        
        #in_cart = CartItem.objects.filter(cart__cart_id=cart_id(request), products=products).exists()
    except Products.DoesNotExist:
        raise Http404("product not found")
    
Context ={
    'products': products,
    # 'in_cart': in_cart
}
return render(request, 'Products_detail.html',context)


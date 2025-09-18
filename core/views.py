from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    search_query = request.GET.get('search_query','').strip()

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if search_query:
        products = products.filter(name__icontains=search_query)
        category = None

    sort_option = request.GET.get('sort', '')
    if sort_option:
        products = apply_sort(products, sort_option)

    return render(request, 'core/product/list.html',
                  {'products': products,
                   'category': category,
                   'categories': categories,
                   'search_query': search_query,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    return render(request, 'core/product/detail.html',
                  {'product': product,
                   'related_products': related_products,
    })

def apply_sort(products, sort_option):
    if sort_option == 'price_asc':
        return products.order_by('price')
    elif sort_option == 'price_desc':
        return products.order_by('-price')
    elif sort_option == 'name_asc':
        return products.order_by('name')
    elif sort_option == 'name_desc':
        return products.order_by('-name')
    return products
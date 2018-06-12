import re
import json
from pprint import pprint
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
from .models import Product
from posts.models import Post
from .smartapps.search import google_search



# Create your views here.
def home(request):
    products = Product.objects.order_by('vote_score').reverse()
    return render(request, 'products/home.html', {'products': products})

@login_required
def create(request):
    return render(request, 'products/create.html')

@login_required
def create_info(request):

    search_term = request.POST['title']
    g_results = google_search(search_term)

    return render(request, 'products/create_info.html', {'gresults':g_results})

@login_required
def create_detail(request):
    product = Product()
    post = Post()

    selected_resto = dict()
    selected_resto['name'] = request.POST['name']
    selected_resto['formatted_address'] = request.POST['formatted_address']
    selected_resto['place_id'] = request.POST['place_id']
    selected_resto['geometry'] = request.POST['geometry']
    selected_resto['rating'] = request.POST['rating']
    selected_resto['types'] = re.findall(r"'(.*?)'", request.POST['types'])

    product.name = request.POST['name']
    product.product_id = request.POST['place_id']
    product.coordinates = request.POST['geometry']
    product.body = ''
    product.address = request.POST['formatted_address']
    product.rating = request.POST['rating']
    product.types = request.POST['types']
    product.url = ''
    product.save()

    post.hunter = request.user
    post.pub_date = timezone.datetime.now()
    post.product = product
    post.type = 'product'
    post.save()
    product.votes.up(request.user.id)

    subject = 'Product Added'
    message = 'message'
    from_email = settings.EMAIL_HOST_USER
    to_list = ['gcasajusrey@gmail.com']
    send_mail(subject, message, from_email, to_list, fail_silently=False)

    return render(request, 'products/create_detail.html', {'selected':selected_resto})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})

@login_required
def vote_up(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if not product.votes.exists(request.user.id):
            product.votes.up(request.user.id)
        return redirect('home')
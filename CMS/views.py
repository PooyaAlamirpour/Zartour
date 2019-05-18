#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.views.generic import ListView

from CMS.models import *
from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import Http404, redirect
import datetime

from hotels.models import Hotel
from master.models import Country
from tickets.models import Airport
from tours.models import Tour, TourType


def home(request):
    sliders = Slider.objects.all().order_by('order_no')
    posts=Article.objects.all()[0:8]
    services = Service.objects.all()[0:8]
    products = Product.objects.all().reverse()[0:3]
    projects=Project.objects.all().reverse()[0:3]
    brands = Brand.objects.all().reverse()[0:3]
    airports = Airport.objects.all().order_by('-order')
    countries = Country.objects.all()
    try:
        domestic_type = TourType.objects.get(id=1)
        domestic_tours = domestic_type.tour_set.all()[:9]
    except:
        pass

    try:
        nondomestic_type = TourType.objects.get(id=2)
        nondomestic_tours = nondomestic_type.tour_set.all()[:9]
    except:
        pass
    hotels = Hotel.objects.all()[:8]
    template = "bilit360/index.html"
    return render(request, template, locals())

def order(request):
    if(request.POST):
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        content = request.POST.get('content')
        template = "reservation/order.html"
        Order.objects.create(name=name,email=email,mobile=mobile,content=content)
    return render(
        request,
        "reservation/order.html",
        {}
    )

def get_projects(request):
    projects = Project.objects.all()
    return render(
        request,
        "reservation/projects.html",
        {
        "projects" : projects,
        }
    )

def get_project_by_slug(request, projects_slug):
    projectItem = Project.objects.get(slug=projects_slug)
    projectList = Project.objects.all().order_by('publish_date').reverse()[0:10]
    if (request.POST):
        email = request.POST.get('email')
        name = request.POST.get('fname')
        name = name + " " +request.POST.get('lname')
        message = request.POST.get('message')
        if name and message:
            comment = Comment.objects.create(commenter=name,
                                  commenter_email=email,
                                  comment_date=datetime.datetime.now(),
                                  content=message)
            comment.project=projectItem
            comment.save()
        is_post_back = True
    return render(
        request,
        "reservation/project.html",
        {
            'projectItem':projectItem,
            'projectList':projectList,
        }
    )

def get_brands(request):
    brands = Brand.objects.all()
    return render(
        request,
        "reservation/brands.html",
        {
        "brands" : brands,
        }
    )

def brand(request):
    brands = Brand.objects.all()
    brandList = Brand.objects.all()[0:10]
    context = locals()
    template = "reservation/brand.html"
    return render(
        request,
        "reservation/brand.html",
        {
            'brands':brands,
            'brandList':brandList,
        }
    )


def get_services(request):
    services = Service.objects.all()
    return render(
        request,
        "reservation/services.html",
        {
        "services" : services,
        }
    )
def get_service_by_slug(request, service_slug):
    service = Service.objects.get(slug=service_slug)
    serviceList = Service.objects.all()
    return render(
        request,
        "reservation/serviceItem.html",
        {
            "service" : service,
            'serviceList' : serviceList,
        }
    )


def about(request):
    template = "reservation/about.html"
    return render(request, template, locals())

def gallery(request):
    portfolio_items=Portfolio_item.objects.all()
    template = "reservation/gallery.html"
    return render(request,
                  template,
                  {
                      'portfolio_items':portfolio_items,
                  })

def gallery_tag(request, tag_slug, tag_id):
    tag=Tag.objects.get(id=tag_id)
    if tag.slug != tag_slug:
        return redirect('portfolio/tag/'+tag.slug+'/'+str(tag.id))
    Po = tag.Portfolio_set.all().order_by('publish_date').reverse()
    return render(
        request,
        "reservation/gallery.html",
        {

            'Portfolio_tag':Po,
            'tag':tag
        }
    )

def contact(request):
    if(request.POST):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        feedback_type = ''
        if request.POST.get('feedback_type_shekayat'):
            feedback_type += '|شکایت|'
        if request.POST.get('feedback_type_enteghad'):
            feedback_type += '|انتقاد|'
        if request.POST.get('feedback_type_pishnahad'):
            feedback_type += '|پیشنهاد|'
        Feedback.objects.create(name=name, phone=phone, content=content, subject=subject, feedback_type=feedback_type)
        is_post_back = True
    else:
        is_post_back = False
    contact_details = Setting.objects.get(is_active=True)
    return render(
        request,
        "bilit360/contact.html",
        {
            'contact_details':contact_details,
            'is_post_back':is_post_back
        }
    )


def aparat_video_proxy(request):
    data = {}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.get('https://www.aparat.com/etc/api/videoByUser/username/zarafshanseir_travel/perpage/10',json=data, verify=False, headers=headers)
    request_obj = json.loads(response.content)
    return JsonResponse(request_obj, safe=False)


def charity(request):
    charity = CharityPage.objects.all()[0]
    return render(
        request,
        "loyalsteel/charity.html",
        {
            "charity" : charity,
        }
    )


def show_video(request):
    link = request.GET.get('link')
    link = link.replace('/vt/frame','')
    return render(
        request,
        "bilit360/frame.html",
        {
            "link" : link,
        }
    )


def faq(request):
    return render(
        request,
        "reservation/faq.html",
        {
            "settings" : Setting.objects.get(is_active=True),
        }
    )


def why(request):
    return render(
        request,
        "loyalsteel/why.html",
        {

        }
    )


def laws(request):
    return render(
        request,
        "loyalsteel/laws.html",
        {
        }
    )

def testimonials(request):
    return render(
        request,
        "loyalsteel/testimonials.html",
        {
        }
    )
def events(request):
    events = Event.objects.all().order_by('date')
    return render(
        request,
        "events.html",
        {
            'events':events,
        }
    )

def get_event_by_slug(request, event_slug, event_id):
    event = Event.objects.get(id = event_id)
    return render(
        request,
        'event.html',
        {
            'event':event,
        }
    )


class ArticleSearchListView(ListView):
    model = Article
    context_object_name = 'news'
    template_name = "bilit360/blog/post_list.html"
    profiles = []

    def get_queryset(self):
        query = self.request.GET.get('q')
        if len(query) > 0:
            return Article.objects.filter(title__icontains=query)
        else:
            return Article.objects.filter()



def blog_list(request):
    news = Article.objects.all()
    newsList = Article.objects.all()[0:10]
    count = news.count()
    context = locals()
    template = "bilit360/blog/post_list.html"
    return render(
        request,
        template,
        {
            'news':news,
            'newsList':newsList,
        }
    )



def blog_item(request, blog_id):
    blog = Article.objects.get(id=blog_id)
    context = locals()
    template = "bilit360/blog/post_single.html"
    return render(
        request,
        template,
        {
            'blog': blog,
        }
    )

def get_news_by_tag(request, tag_slug, tag_id):
    tag=Tag.objects.get(id=tag_id)
    count = Article.objects.count()

    if tag.slug != tag_slug:
        return redirect('article/tag/'+tag.slug+'/'+str(tag.id))
    news = tag.article_set.all().order_by('publish_date').reverse()
    return render(
        request,
        "reservation/article.html",
        {
            'news':news,
            'tag':tag,

        }
    )


def get_news_by_cat(request, cat_id):
    cat = Catagory.objects.get(id=cat_id)
    count = Article.objects.count()
    # if cat.slug != cat_slug:
    #     return redirect('/article/cat/'+cat.slug+'/'+str(cat.id))
    news = cat.article_set.all().order_by('publish_date').reverse()
    return render(
        request,
        "bilit360/blog/post_list.html",
        {
            'news':news,
            'cat':cat,

        }
    )



def get_news_by_slug(request, news_slug):
    newsItem = Article.objects.get(slug=news_slug)
    newsList = Article.objects.all().order_by('publish_date').reverse()[0:10]
    tags = newsItem.tags.all()
    catagories = Catagory.objects.all()
    if (request.POST):
        email = request.POST.get('email')
        name = request.POST.get('fname')
        name = name + " " +request.POST.get('lname')
        message = request.POST.get('message')
        if name and message:
            comment = Comment.objects.create(commenter=name,
                                  commenter_email=email,
                                  comment_date=datetime.datetime.now(),
                                  content=message)
            comment.article=newsItem
            comment.save()
        is_post_back = True
    return render(
        request,
        "reservation/article-item.html",
        {
            'newsItem':newsItem,
            'newsList':newsList,
        }
    )

def page(request, page_link):
    page=Page.objects.get(link_address=page_link)
    return render(
        request,
        "reservation/page.html",
        {
            "page":page,
        }
    )

def get_products_all(request):
    products = Product.objects.all()
    return render(
        request,
        "reservation/products.html",
        {
            "products":products
        }
    )

def get_products_by_catagory(request, cat_slug, cat_id):
    cat = Product_Catagory.objects.get(id = cat_id )
    products=cat.product_set.all()
    if (request.POST):
        email = request.POST.get('email')
        name = request.POST.get('fname')
        name = name + " " +request.POST.get('lname')
        message = request.POST.get('message')
        if name and message:
            comment = Comment.objects.create(commenter=name,
                                  commenter_email=email,
                                  comment_date=datetime.datetime.now(),
                                  content=message)
            comment.product_cat=cat
            comment.save()
        is_post_back = True
    return render(
        request,
        "reservation/product-cat.html",
        {
            "products":products,
            "catagory":cat
        }
    )

def get_product_by_id(request, product_slug, product_id):
        productItem = None
        context = {}
        try:
            productItem = Product.objects.get(id=product_id)
            if productItem.slug != product_slug:
                return redirect('/product/'+productItem.slug+"/"+str(productItem.id))
            else:
                context['product'] = productItem
        except Product.DoesNotExist:
            raise Http404("Product does not exist")
        if (request.POST):
            email = request.POST.get('email')
            name = request.POST.get('fname')
            name = name + " " + request.POST.get('lname')
            message = request.POST.get('message')
            if name and message:
                comment = Comment.objects.create(commenter=name,
                                                 commenter_email=email,
                                                 comment_date=datetime.datetime.now(),
                                                 content=message)
                comment.product = productItem
                comment.save()
            is_post_back = True
        return render(
                request,
                "reservation/product-item.html",
                context)
def get_products_json(request):
    try:
        catagory_name = request.GET['catagory']
        catagory = Product_Catagory.objects.get(name=catagory_name)
        products = Product.objects.all().filter(product_catagory = catagory)
    except:
        return render(request, 'table_body.html', {})
    return render(request, 'table_body.html', {'product_list':products,})


def get_product_json(request):
    try:
        product_id = request.GET['productID']
        product = Product.objects.get(id=product_id)
        alternative_names = ProductAlternativeName.objects.filter(product=product)
    except:
        return render(request, 'fancy_product.html', {})
    return render(request, 'fancy_product.html', {'product':product, 'alternative_names':alternative_names})
def all_products_json(request):
    try:
        products = Product.objects.all()
    except:
        return render(request, 'table_body.html', {})
    return render(request, 'table_body.html', {'product_list':products,})

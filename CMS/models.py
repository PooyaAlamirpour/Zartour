from __future__ import unicode_literals
from django import forms
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from userprofile.models import UserProfile

# Create your models here.
class Slider(models.Model):
    order_no = models.IntegerField()
    image = models.ImageField()
    caption = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return "Slider image no "+str(self.order_no)+" : "+ self.caption[0:20] + "..."


class Service(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Catagory(models.Model):
    name = models.CharField(max_length = 60)
    parent = models.ForeignKey("Catagory", null=True, blank=True, default=None)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
    # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(Catagory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'


class Tag(models.Model):
    keyword = models.CharField(max_length = 60)
    slug = models.SlugField()
    def __unicode__(self):
        return self.keyword


class Article(models.Model):
    author = models.ForeignKey(UserProfile)
    creation_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    content = RichTextField()
    catagory = models.ForeignKey(Catagory,null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True)
    slug = models.CharField(max_length=150)
    image_alt = models.CharField(max_length=150, null=True, blank=True)
    def __unicode__(self):
        return self.title
    def get_comments(self):
        return Comment.objects.filter(article=self)
    def get_tags(self):
        return self.tags.all()

class Project(models.Model):
    creation_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    content = RichTextField()
    catagory = models.ForeignKey(Catagory,null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True)
    slug = models.CharField(max_length=150)
    image_alt = models.CharField(max_length=150, null=True, blank=True)
    def __unicode__(self):
        return self.title
    def get_comments(self):
        return Comment.objects.filter(project=self)
    def get_tags(self):
        return self.tags.all()


class Portfolio_item(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=150, null=True, blank=True)
    catagory = models.ForeignKey('Portfolio_category',null=True, blank=True, default=None)
    tags = models.ManyToManyField('Portfolio_tag', null=True, blank=True, default=None)

    def __unicode__(self):
        return self.title


class Portfolio_category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description_title = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    slug = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name



class Portfolio_image(models.Model):
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=150, null=True, blank=True)
    portfolio_item = models.ForeignKey(Portfolio_item,null=True, blank=True, default=None)

    def __unicode__(self):
        return self.image_alt


class Portfolio_tag(models.Model):
    keyword = models.CharField(max_length = 60)
    slug = models.CharField(max_length = 60)

    def __unicode__(self):
        return self.keyword


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    email = models.EmailField(max_length=100, null=True, blank=True, default=None)
    mobile = models.CharField(max_length=100, null=True, blank=True, default=None)
    content = models.TextField()

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, null=True, blank=True)
    project = models.ForeignKey(Project, null=True, blank=True)
    product = models.ForeignKey("Product", null=True, blank=True)
    product_cat = models.ForeignKey("Product_Catagory", null=True, blank=True)
    content = models.CharField(max_length=300)
    commenter = models.CharField(max_length=100, null=True, blank=True)
    commenter_email = models.EmailField(null=True, blank=True, default=None)
    commenter_website = models.URLField(null=True, blank=True, default=None)
    comment_date = models.DateTimeField(null=True, blank=True)
    reply = models.CharField(max_length=300,null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content[0:25]+"..."


class Page(models.Model):
    author = models.ForeignKey(UserProfile)
    creation_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    title = models.CharField(max_length=80)
    is_in_navbar = models.BooleanField(verbose_name="Has a menu link")
    navbar_name = models.CharField(max_length=50)
    link_address = models.CharField(max_length=50)
    content = RichTextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.title

    def get_tags(self):
        return self.tags.all()


class Product_Catagory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("Product_Catagory", null=True, blank=True, default=None)
    image = models.ImageField(null = True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    description_title = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    slug = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
    # Newly created object, so set slug
            self.slug = self.name.replace('&nbsp;', '-').replace('\n', '-').replace('\r', '-').replace(' ','-')
        super(Product_Catagory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Catagory'
        verbose_name_plural = 'Product Catagories'

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_catagory = models.ForeignKey(Product_Catagory)
    description = RichTextField()
    icon = models.ImageField(null=True, blank=True)
    image = models.ImageField()
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=70, null=True, blank=True)
    slug = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class ProductAlternativeName(models.Model):
    alternative_name = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=3)
    product = models.ForeignKey(Product)


class Setting(models.Model):
    is_active = models.BooleanField()
    website_icon = models.ImageField(null=True, blank=True)
    website_logo = models.ImageField(null=True, blank=True)
    website_name = models.CharField(max_length=100)
    website_slogan = models.CharField(max_length=500, null=True, blank=True)
    brief_description = RichTextField(null=True, blank=True)
    long_descriptioon = RichTextField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    info_email = models.EmailField()
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, null=True, blank=True)
    phone_number_3 = models.CharField(max_length=20, null=True, blank=True)
    phone_number_4 = models.CharField(max_length=20, null=True, blank=True)
    header_phone = models.CharField(max_length=20, null=True, blank=True)
    googlemap_lan = models.CharField(max_length=50,  null=True, blank=True)
    googlemap_lat = models.CharField(max_length=50,  null=True, blank=True)
    facebook_link = models.CharField(max_length=100,  null=True, blank=True)
    gplus_link = models.CharField(max_length=100,  null=True, blank=True)
    telegram_link = models.CharField(max_length=100,  null=True, blank=True)
    instagram_link = models.CharField(max_length=100,  null=True, blank=True)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
    def __unicode__(self):
        return self.website_name+" Settings"
class SpecialContent(models.Model):
    charity = RichTextField()
class CharityPage(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    donated_amount = models.BigIntegerField(null=True, blank=True)
    charity_title1=models.CharField(max_length=200, null=True, blank=True)
    charity_text1=RichTextField(null=True, blank=True)
    charity_image1=models.ImageField(null=True, blank=True)
    charity_title2=models.CharField(max_length=200, null=True, blank=True)
    charity_text2=RichTextField(null=True, blank=True)
    charity_image2=models.ImageField(null=True, blank=True)
    charity_title3=models.CharField(max_length=200, null=True, blank=True)
    charity_text3=RichTextField(null=True, blank=True)
    charity_image3=models.ImageField(null=True, blank=True)
    charity_title4=models.CharField(max_length=200, null=True, blank=True)
    charity_text4=RichTextField(null=True, blank=True)
    charity_image4=models.ImageField(null=True, blank=True)
class Offer(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    def __unicode__(self):
        return self.title
class TeamMember(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    linkedin_link = models.CharField(max_length=100,  null=True, blank=True)
    facebook_link = models.CharField(max_length=100,  null=True, blank=True)
    instagram_link = models.CharField(max_length=100,  null=True, blank=True)
    def __unicode__(self):
        return self.name
class Customer(models.Model):
    logo = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    def __unicode__(self):
        return self.name
class Event(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = RichTextField()
    slug = models.SlugField()
    def __unicode__(self):
        return self.title
class FAQCatagory(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
class QandA(models.Model):
    question = models.CharField(max_length=500)
    answer = RichTextField()
    catagory = models.ForeignKey(FAQCatagory)
    def __unicode__(self):
        return self.question[0:20]+"..."


class Province(models.Model):
    name = models.CharField(max_length=90)


class City(models.Model):
    #id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=90)


class Feedback(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=200,null=True, blank=True)
    subject = models.CharField(max_length=200,null=True, blank=True)
    feedback_type = models.CharField(max_length=200,null=True, blank=True)
    content = RichTextField(null=True, blank=True)


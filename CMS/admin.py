from django.contrib import admin
from CMS.models import *
# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order_no', 'image')
    def get_ordering(self, request):
        return ['order_no']
admin.site.register(Slider, SliderAdmin)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
admin.site.register(Catagory, CatagoryAdmin)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('keyword',), }
admin.site.register(Tag, TagAdmin)
#admin.site.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'publish_date', 'author')
    prepopulated_fields = {'slug': ('title',), }
admin.site.register(Article, ArticleAdmin)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_address', 'is_in_navbar')
admin.site.register(Page, PageAdmin)
admin.site.register(SpecialContent)
admin.site.register(CharityPage)
admin.site.register(TeamMember)
admin.site.register(Customer)
admin.site.register(FAQCatagory)
admin.site.register(QandA)
class ProductCatagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',), }
admin.site.register(Product_Catagory, ProductCatagoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_catagory', 'image','slug','id')
    prepopulated_fields = {'slug': ('name',), }
admin.site.register(Product, ProductAdmin)
admin.site.register(Setting)
admin.site.register(ProductAlternativeName)
admin.site.register(Offer)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Event, EventAdmin)
admin.site.register(Portfolio_item)
admin.site.register(Portfolio_tag)
admin.site.register(Portfolio_image)
admin.site.register(Portfolio_category)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(Feedback)


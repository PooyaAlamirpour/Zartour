from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import blog_item, blog_list, contact, get_news_by_tag, get_news_by_cat, ArticleSearchListView, aparat_video_proxy, show_video

urlpatterns = [
    url(r'^$', blog_list, name="blog_list"),
    url(r'^blog/(?P<blog_id>\d+)$', blog_item, name="blog_item"),
    url(r'^cat/(?P<cat_id>\d+)$', get_news_by_cat, name="cat"),
    url(r'^cat/(?P<tag_id>\d+)$', get_news_by_tag, name="tag"),
    url(r'^contact$', contact, name="contact"),
    url(r'^search/$', ArticleSearchListView.as_view(), name="blog_search"),
    url(r'^videos/$', aparat_video_proxy, name="videos"),
    url(r'^videos/details/$', show_video, name="videos_item"),

]
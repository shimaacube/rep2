from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.comments.models import Comment
     
admin.autodiscover()
     
urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        # url(r'^$', 'blog.views.index'),
        url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
        url(r'', include('blog.urls')),
        # url('', include('social.apps.django_app.urls', namespace='social')),
        # url('', include('django.contrib.auth.urls', namespace='auth')),
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^comments/', include('django.contrib.comments.urls')),
        # (r'^accounts/', include('registration.backends.default.urls')),
        
    )
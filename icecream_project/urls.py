from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

        # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^modern-business', include('cms.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),

    # Examples:
    # url(r'^$', 'icecream_project.views.home', name='home'),
    # url(r'^icecream_project/', include('icecream_project.foo.urls')),


    #url(r'^modern-business', TemplateView.as_view(template_name='index_modern_business.html')),
    url(r'^about', TemplateView.as_view(template_name='about.html')),
    url(r'^blog-home-1', TemplateView.as_view(template_name='blog-home-1.html')),
    url(r'^blog-home-2', TemplateView.as_view(template_name='blog-home-2.html')),
    url(r'^blog-post', TemplateView.as_view(template_name='blog-post.html')),
    url(r'^404', TemplateView.as_view(template_name='404.html')),
    url(r'^faq', TemplateView.as_view(template_name='faq.html')),
    url(r'^full-width', TemplateView.as_view(template_name='full-width.html')),
    url(r'^portfolio-1-col', TemplateView.as_view(template_name='portfolio-1-col.html')),
    url(r'^portfolio-2-col', TemplateView.as_view(template_name='portfolio-2-col.html')),
    url(r'^portfolio-3-col', TemplateView.as_view(template_name='portfolio-3-col.html')),
    url(r'^portfolio-4-col', TemplateView.as_view(template_name='portfolio-4-col.html')),
    url(r'^portfolio-item', TemplateView.as_view(template_name='portfolio-item.html')),
    url(r'^pricing', TemplateView.as_view(template_name='pricing.html')),
    url(r'^services', TemplateView.as_view(template_name='services.html')),
    url(r'^sidebar', TemplateView.as_view(template_name='sidebar.html')),

    #INFMOUS
    url(r'^infhome$', TemplateView.as_view(template_name='home.html')),
    url(r'^infindex$', TemplateView.as_view(template_name='index.html')),
    url(r'^infindex0$', TemplateView.as_view(template_name='index0.html')),

    url(r'^roster$', TemplateView.as_view(template_name='roster.html')),
    url(r'^source$', TemplateView.as_view(template_name='source.html')),
    url(r'^joetic$', TemplateView.as_view(template_name='joetic.html')),
    url(r'^bam$', TemplateView.as_view(template_name='bam.html')),

    #url(r'^artists/source/$', views.source),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('',
#                            url(r'^__debug__/', include(debug_toolbar.urls)),
#                            )

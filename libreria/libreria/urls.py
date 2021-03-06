from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from libreria.main import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.index),
    (r'^books/$', views.booksView),
    (r'^book/$', views.book_manageView),
    (r'^book/(?P<id>\d+)/', views.book_manageView),
    (r'^book/delete/(?P<id>\d+)/', views.delete_book),
    
    (r'^search/$','views.xhr_test'),

    

    #(r'^appusers/$', views.users),
    #(r'^Appuser/$', views.appuser_manageView),
    #(r'^Appuser/(?P<id>\d+)/$', views.appuser_manageView),

    (r'^users/$', views.usersView),
    (r'^user/$', views.user_manageView),
    (r'^user/(?P<id>\d+)/', views.user_manageView),
    (r'^user/delete/(?P<id>\d+)/', views.delete_user),

    (r'^guarantors/$', views.guarantorsView),
    (r'^guarantor/$', views.guarantor_manageView),
    (r'^guarantor/(?P<id>\d+)/', views.guarantor_manageView),
    (r'^guarantor/delete/(?P<id>\d+)/', views.delete_guarantor),

    (r'^bookclassifications/$', views.bookclassificationsView),
    (r'^bookclassification/$', views.bookclassification_manageView),
    (r'^bookclassification/(?P<id>\d+)/', views.bookclassification_manageView),
    (r'^bookclassification/delete/(?P<id>\d+)/', views.delete_bookclassification),
    (r'^booksubclassifications/$', views.booksubclassificationsView),
    (r'^booksubclassification/$', views.booksubclassification_manageView),
    (r'^booksubclassification/(?P<id>\d+)/', views.booksubclassification_manageView),
    (r'^booksubclassification/delete/(?P<id>\d+)/', views.delete_booksubclassification),

    (r'^loans/$', views.loansView),
    (r'^loan/$', views.loan_manage_inlineView),
    (r'^loan/(?P<id>\d+)/', views.loan_manage_inlineView),
    (r'^loan/delete/(?P<id>\d+)/', views.delete_loan),
    
    (r'^loansReport/$', views.loansReportView),
    (r'^loansReportR/$', views.loansReportRView),
    (r'^generalloansReport/$', views.generalloansReportView),

    url(r'^login/$',views.ingresar),
    url(r'^logout/$', views.logoutUser),
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
    # Examples:
    # url(r'^$', 'libreria.views.home', name='home'),
    # url(r'^libreria/', include('libreria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
)

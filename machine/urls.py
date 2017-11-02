from django.conf.urls import  url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index' ),
   url(r'index.html', views.detail, name='detail' ),
   url(r'indexs.html', views.detail1, name='detail1' ),
   url(r'plan.html', views.detail2, name='detail2' ),
   url(r'popup.html', views.detail3, name='detail3' ),
   url(r'login.html', views.detail4, name = 'detail4'),
   url(r'logout.html', views.detail5, name = 'detail5'),
   url(r'signup.html', views.detail6, name = 'detail6'),
   url(r'Fixed deposit.html', views.detail7, name = 'detail7'),
   url(r'gold.html', views.detail8, name = 'detail8'),
   url(r'insurance.html', views.detail9, name = 'detail9'),
   url(r'mutual fund.html', views.detail10, name = 'detail10'),
   url(r'Real estate.html', views.detail11, name = 'detail11'),
   url(r'stock market.html', views.detail12, name = 'detail12'),
   #url(r'^(?P<page_name>about|faq|press|whatever)/$', 'myapp.staticpage', name='static-pages'),
    #url(r'^(?P<page>.+\.html)$', StaticView.as_view()),

]

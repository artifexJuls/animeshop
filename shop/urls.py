from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import add_to_cart

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes, name='clothes'),
    path('search/', views.search, name='search'),
    path('signup/', views.create_user, name='signup'),
    path('profile/', views.view_profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='edit'),
    path('login/', LoginView.as_view(template_name='shop/profile_not_found.html'), name='blog_login'),
    path('logout/', LogoutView.as_view(template_name='shop/index.html'), name='blog_logout'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/', views.orders, name='order'),
    path('delete_card/', views.delete_card, name='delete_card'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

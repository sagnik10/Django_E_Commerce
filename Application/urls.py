from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('login/',views.login),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout),
    path('main_page/', views.main_page),
    path('products/<int:id>', views.details_page),
    path('laptop/<int:id>', views.laptops_details_page),
    path('mens/<int:id>', views.mens_details_page),
    path('womens/<int:id>', views.womens_details_page),
    path('furnitures/<int:id>', views.furnitures_details_page),
    path('checkout_page/', views.checkout_page),

]
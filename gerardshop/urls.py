from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.all_products, name="products"),
   path('product/<int:prodid>/', views.product_individual, name="individual_product"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('feedback/', views.feedback_form, name='feedback'),
   path('basket/', views.show_basket, name="show_basket"),
   path('removeitem/<int:sbi>', views.remove_item, name="remove_basket"),
   path('additem/<int:sbi>', views.add_item, name="add_basket"),
   path('addbasket/<int:prodid>/', views.add_to_basket, name="add_basket"),
] 

# this for adding indivudal products, above is to add all products to home pagepath('products/', views.all_products, name="products"),
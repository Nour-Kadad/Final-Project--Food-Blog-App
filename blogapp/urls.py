
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('all_blogs', views.all_blogs, name="all_blogs"),
    path('blog_details/<int:pk>', views.blog_details, name="blog_details"),
    path('search_blog', views.search_blog, name="search_blog"),
    path('get_in_touch_url', views.get_in_touch_url, name="get_in_touch_url"),
    path('last_2_blogs', views.last_2_blogs, name="last_2_blogs"),
    path('signup_login', views.signup_login, name="signup_login"),
    path('signup_form', views.signup_form, name="signup_form"),
    path('logout_func', views.logout_func, name="logout_func"),
    path('login_func', views.login_func, name="login_func"),
    path('submit_comments', views.submit_comments, name="submit_comments"),
    path('shop', views.shop, name="shop"),
    path('product_detail/<int:pk>', views.product_detail, name="product_detail"),
    path('mycart_checkout', views.mycart_checkout, name="mycart_checkout"),
    path('checkout_products', views.checkout_products, name="checkout_products"),
    path('my_account', views.my_account, name="my_account"),
    path('lifestyle', views.lifestyle, name="lifestyle"),
    path('lifestyle_details/<int:pk>', views.lifestyle_details, name="lifestyle_details"),
    path('travel_adventure', views.travel_adventure, name="travel_adventure"),
]
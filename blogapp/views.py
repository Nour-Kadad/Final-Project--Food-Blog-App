from django.shortcuts import render, redirect, HttpResponse
from .models import blog_post, get_in_touch, Blogs_Comments, Product_Category, Product, Orders, Lifestyle
# Create your views here.
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    all_latest_pst = blog_post.objects.order_by('-time')
    context = {'all_latest_pst':all_latest_pst}
    return render(request, 'index.html', context)


def all_blogs(request, template='all_blogs.html', page_template='all_blogs_new.html'):
    all_latest_pst = blog_post.objects.order_by('-time')
    context = {'all_latest_pst': all_latest_pst, 'page_template': page_template,}
    if request.is_ajax():
        template = page_template
    return render(request, template, context)



def lifestyle(request, template='lifestyle.html', page_template='lifestyle_new.html'):
    all_latest_pst = Lifestyle.objects.order_by('-time')
    context = {'all_latest_pst': all_latest_pst, 'page_template': page_template,}
    if request.is_ajax():
        template = page_template
    return render(request, template, context)



def blog_details(request, pk):
    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    gett_pst = blog_post.objects.get(id=pk)
    print(gett_pst)

    all_comments = Blogs_Comments.objects.filter(Blog=gett_pst)
    all_commnt_count = all_comments.count()

    context = {'gett_pst': gett_pst, 'all_latest_pst':all_latest_pst, 'all_commnt_count':all_commnt_count, 'all_comments':all_comments}
    return render(request, 'blog_details.html', context)


def lifestyle_details(request, pk):
    all_latest_pst = Lifestyle.objects.order_by('-time')[:6]
    gett_pst = Lifestyle.objects.get(id=pk)
    print(gett_pst)


    context = {'gett_pst': gett_pst, 'all_latest_pst':all_latest_pst}
    return render(request, 'lifestyle_details.html', context)


def search_blog(request, template='all_blogs.html', page_template='all_blogs_new.html'):
    search_value = request.GET.get('search_value')
    print(search_value)
    all_latest_pst = blog_post.objects.filter(Q(title__icontains = search_value) |  Q(discription__icontains = search_value))
    context = {'all_latest_pst': all_latest_pst, 'page_template': page_template, }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)


def get_in_touch_url(request):
    get_email_touch = request.POST.get('get_email_touch')
    print(get_email_touch)

    savee_get_in_touch = get_in_touch(user_email=get_email_touch)
    savee_get_in_touch.save()
    messages.success(request, "We Got Your Email Address. We Will Contact You Soon !")
    return redirect('index')


@csrf_exempt
def last_2_blogs(request):
    all_cats = blog_post.objects.order_by('-time')[:2]
    get_cat_seri = serializers.serialize('json', all_cats)
    return JsonResponse(get_cat_seri, safe=False)



def signup_login(request):
    return render(request, 'userpage.html')


def signup_form(request):
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    r_email = request.POST.get('r_email')
    passwrd = request.POST.get('passwrd')
    c_pass = request.POST.get('c_pass')

    user_username_info = User.objects.filter(username=r_email)

    erorr_message = ""

    if user_username_info:
        erorr_message = "Email Already Exist !"

    elif passwrd != c_pass:
        erorr_message = "Passwords are not match !!"

    elif len(passwrd) < 8:
        erorr_message = "Passwords Must be Al least 8 Digits!"



    if not erorr_message:
        # create user
        myuser = User.objects.create_user(r_email, r_email, passwrd)
        myuser.first_name = f_name
        myuser.last_name = l_name
        myuser.is_active = True
        myuser.save()

        user = authenticate(username=r_email, password=passwrd)
        if user is not None:
            login(request, user)

        messages.success(request, f'Account Registered Successfully. Now Your Logged as {f_name} {l_name}')
        return redirect('index')

    else:
        value_dic = {'erorr_message': erorr_message, 'f_name':f_name, 'l_name':l_name, 'r_email':r_email}
        return render(request, 'userpage.html', value_dic)





def logout_func(request):
    logout(request)
    messages.success(request, "Successfully Logged OUT !!")
    return redirect('signup_login')




def login_func(request):
    log_email = request.POST.get('log_email')
    log_password = request.POST.get('pass_log')
    # this is for authenticate username and password for login
    user = authenticate(username=log_email, password=log_password)

    erorr_message_2 = ""

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In !!")
        return redirect('index')
    else:
        erorr_message_2 = "Invalid Credentials, Please Try Again !!"

        value_func2 = {'erorr_message_2': erorr_message_2, 'log_email': log_email}
        return render(request, 'userpage.html', value_func2)





def submit_comments(request):
    if request.user.is_authenticated:
        subject = request.POST.get('text_comments')
        text_comments = request.POST.get('text_comments')
        post_id = request.POST.get('post_id')

        b_p = blog_post.objects.get(id=post_id)

        sav_commnt =Blogs_Comments(User=request.user, Blog=b_p, comment_subject=subject, comment_text=text_comments)
        sav_commnt.save()
        messages.success(request, "Your Comment Is Posted !!")
        return redirect('blog_details', post_id)
    else:
        messages.success(request, "You Have to Login for submitting Comments !!")
        return redirect('signup_login')


def shop(request):
    all_products = Product.objects.order_by('-time')
    context={'all_products':all_products}
    return render(request, 'shop.html', context)



def product_detail(request, pk):
    get_prod = Product.objects.get(id=pk)
    latest_prod = Product.objects.order_by('-time')[:6]
    context = {'get_prod':get_prod, 'latest_prod':latest_prod}
    return render(request, 'product_details_page.html', context)


def mycart_checkout(request):
    context = {}
    return render(request, 'mycart_checkout.html', context)



@csrf_exempt
def checkout_products(request):
    frs_nam = request.POST.get('frs_nam')
    ls_nam = request.POST.get('ls_nam')
    ch_eml = request.POST.get('ch_eml')
    phn_num = request.POST.get('phn_num')
    addrss_ch = request.POST.get('addrss_ch')
    ch_pss = request.POST.get('ch_pss')
    json_all_prds_ids = request.POST.get('json_all_prds_ids')
    sho_total_price = request.POST.get('sho_total_price')

    py_jsn_all_prds_id = json.loads(json_all_prds_ids)

    print(frs_nam, ls_nam, ch_eml, phn_num, addrss_ch, ch_pss,
                json_all_prds_ids, py_jsn_all_prds_id)



    if request.user.is_authenticated:
        myuser = request.user
    else:
        if User.objects.filter(username=ch_eml):
            return HttpResponse('1')
        myuser = User.objects.create_user(ch_eml, ch_eml, ch_pss)
        myuser.first_name = frs_nam
        myuser.last_name = ls_nam
        myuser.is_active = True
        myuser.save()

        user = authenticate(username=ch_eml, password=ch_pss)
        if user is not None:
            login(request, user)

    print(myuser)

    save_Orders = Orders(customer=myuser, total_price=sho_total_price, customer_first_name=frs_nam, customer_last_name=ls_nam, customer_email=ch_eml,  customer_phone_number=phn_num, customer_address=addrss_ch)
    save_Orders.save()
    for i in py_jsn_all_prds_id:
        save_Orders.products.add(i)

    return HttpResponse(save_Orders.id)


def my_account(request):
    if request.user.is_authenticated:
        all_odrs = Orders.objects.filter(customer=request.user).order_by('-time')
        context={'all_odrs':all_odrs}
        return render(request, 'my_account.html', context)
    else:
        return redirect('signup_login')



def travel_adventure(request):
    return render(request, 'travel_adventure.html')
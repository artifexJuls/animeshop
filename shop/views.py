import datetime
import time
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from shop.forms import UserProfileForm, RegistrationForm, OrderForm
from shop.models import Clothes, Tags, UserProfile, ShopCard, Registration, Order


def index(request):
    global todaysDay
    day = time.localtime().tm_wday
    if day == 1:
            todaysDay = "понеділок"
    elif day == 2:
            todaysDay = "вівторок"
    elif day == 3:
            todaysDay = "середа"
    elif day == 4:
            todaysDay = "четвер"
    elif day == 5:
            todaysDay = "п'ятниця"
    elif day == 6:
            todaysDay = "субота"
    elif day == 7:
        todaysDay = "неділя"
    date = datetime.date.today()
    context = {'time':todaysDay,'day':time.strftime("%Y-%m-%d")}
    return render(request, 'shop/index.html', context = context)


def about(request):
    context = {}
    return render(request, 'shop/about.html', context = context)


def contacts(request):
    context = {}
    return render(request, 'shop/contacts.html', context = context)


def get_categories():
    all_categories = Tags.objects.all()
    count = all_categories.count()
    return {'cat1': all_categories[:count / 2 + count % 2], 'cat2': all_categories[count / 2 + count % 2:]}


def clothes(request):
    clothes = Clothes.objects.all()
    tags = Tags.objects.filter(posts__in=clothes).distinct()
    context = {'clothes': clothes, 'tags': tags}
    context.update(get_categories())
    return render(request, 'shop/clothes.html', context=context)


def search(request):
    clothes = Clothes.objects.all()
    tags = Tags.objects.filter(posts__in=clothes).distinct()
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            clothes = Clothes.objects.filter(Q(description__icontains=query) | Q(tags__tagName__icontains=query)).order_by('-id').distinct()
            context = {'clothes': clothes, 'tags': tags}
            context.update(get_categories())
            return render(request, 'shop/clothes.html', context=context)
    return render(request, 'shop/clothes.html')


def create_user(request):
    print("*")
    try:
        print(request)
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['nickname']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password=password)
                    print("form.cleaned_data['phone']: ", form.cleaned_data['phone'])
                except Exception as e:
                    print(f"Errors {e}")
                    print(form.cleaned_data['nickname'])

                user_profile = user.profile
                user_profile.phone = form.cleaned_data['phone']
                user_profile.email = form.cleaned_data['email']

                user_profile.save()
            else:
                print(form.errors)

    except IntegrityError:
        return render(request, 'shop/profile_not_found.html', {'success': False})
    return render(request, 'shop/signup.html', {'success': True})


def signup(request):
    return render(request, 'shop/signup.html', {'success': True})


@login_required
def view_profile(request):
    try:
        user_profile = request.user.profile
        us_pr = UserProfile.email
        orders = Order.objects.all()
        try:
            shop_card = ShopCard.objects.filter(customer_profile=user_profile)
        except ShopCard.DoesNotExist:
            shop_card = None

        context = {'user_profile': user_profile, 'orders': orders, 'shop_card': shop_card}
        return render(request, 'shop/profile.html', context)
    except UserProfile.DoesNotExist:
        return render(request, 'shop/profile.html')


@login_required
def profile_edit(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return render(request, 'shop/index.html', {'success': True})
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'shop/update_profile.html', {'form': form})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Clothes, pk=product_id)
        user_profile = request.user.profile
        shop_card, created = ShopCard.objects.get_or_create(
            customer_profile=user_profile,
            product_name=product.title,
            defaults={'product_price': product.price, 'product_amount': 1}
        )

        if not created:
            shop_card.product_amount += 1
            shop_card.save()

        return redirect('profile')

    return redirect('profile_not_found')


@login_required
def create_order(request):
    user_profile = request.user.profile
    order_form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if order_form.is_valid():
            product_amount = order_form.cleaned_data['product_amount']
            order = order_form.save(commit=False)
            order.user_profile = user_profile

            shop_card_id = request.POST.get('shop_card_id')
            shop_card = get_object_or_404(ShopCard, id=shop_card_id, customer_profile=user_profile)

            order.total_price = shop_card.product_price * product_amount
            order.item_names = shop_card.product_name
            order.address = order_form.cleaned_data['address']
            order.save()

            shop_card.delete()

            return redirect('order')

    return render(request, 'shop/profile.html', {'order_form': order_form, 'user_profile': user_profile})


@login_required
def orders(request):
    return render(request, 'shop/order.html', {'success': True})


@login_required
def delete_card(request):
    if request.method == 'POST':
        shop_card_id = request.POST.get('shop_card_id')
        shop_card = get_object_or_404(ShopCard, id=shop_card_id, customer_profile=request.user.profile)
        shop_card.delete()

    return redirect('profile')


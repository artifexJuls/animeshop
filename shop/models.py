from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



class Tags(models.Model):
    tagName = models.TextField(max_length=20, verbose_name='Tag')

    def __str__(self):
        return self.tagName

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Clothes(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(verbose_name='description')
    poster = models.ImageField(upload_to='media', default="http://placehold.it/600x400", verbose_name='Poster')
    tags = models.ManyToManyField(Tags, blank=True, related_name='posts', verbose_name="Hashtag")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    product_amount = models.IntegerField(verbose_name='Amount')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', verbose_name='user')
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Last Name')
    email = models.EmailField(max_length=500, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Phone')
    password = models.CharField(max_length=30, blank=True, null=True, verbose_name='Password')
    birth_date = models.DateField(verbose_name='Date of Birth', default='2020-10-10')
    avatar = models.ImageField(upload_to='media', default="http://placehold.it/600x400", verbose_name='Avatar')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Registration(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='registration', verbose_name='user')
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='nickname')
    email = models.EmailField(max_length=500, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Phone')
    password = models.CharField(max_length=30, blank=True, null=True, verbose_name='Password')
    birth_date = models.DateField(verbose_name='Date of Birth', default='2020-10-10')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'registration'
        verbose_name_plural = 'registrations'


class ShopCard(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_amount = models.IntegerField()
    customer_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='shop_cards', verbose_name='Customer Profile')
    items = models.OneToOneField(Clothes, related_name='shop_cards', verbose_name='Items in ShopCard', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Shop Card'
        verbose_name_plural = 'Shop Cards'


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders', verbose_name='User Profile')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Total Price')
    is_completed = models.BooleanField(default=False, verbose_name='In Progress')
    item_names = models.TextField(blank=True, verbose_name='Item Names')
    address = models.TextField(blank=True, verbose_name='Address')
    product_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Order #{self.pk} - {self.user_profile.user.username}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'



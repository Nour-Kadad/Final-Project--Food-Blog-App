from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
import uuid

class blog_post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='post_img')
    img2 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img3 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img4 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img5 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img6 = models.ImageField(blank=True, null=True, upload_to='post_img')
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title


class Blogs_Comments(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    comment_subject = models.CharField(max_length=255)
    comment_text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.User.email + " - "+ self.Blog.title


class Product_Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.IntegerField(default='0', blank=True, null=True)
    Category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='product/')
    img2 = models.ImageField(blank=True, null=True, upload_to='product/')
    img3 = models.ImageField(blank=True, null=True, upload_to='product/')
    img4 = models.ImageField(blank=True, null=True, upload_to='product/')
    img5 = models.ImageField(blank=True, null=True, upload_to='product/')
    img6 = models.ImageField(blank=True, null=True, upload_to='product/')
    time = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.Name


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, null=True)
    total_price = models.CharField(max_length=255, blank=True, null=True)
    customer_first_name = models.CharField(max_length=255, blank=True, null=True)
    customer_last_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_phone_number = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    status = (
        ("Processing", "Processing"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
    )
    Order_status = models.CharField(max_length=20, choices=status, default="Processing")
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.customer.email



class get_in_touch(models.Model):
    user_email = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.user_email




class Lifestyle(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='post_img')
    img2 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img3 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img4 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img5 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img6 = models.ImageField(blank=True, null=True, upload_to='post_img')
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

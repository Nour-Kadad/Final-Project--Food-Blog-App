from django.contrib import admin

# Register your models here.
from .models import blog_post, get_in_touch, Blogs_Comments, Product_Category,Product, Orders, Lifestyle


admin.site.register(blog_post)
admin.site.register(get_in_touch)
admin.site.register(Blogs_Comments)
admin.site.register(Product_Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Lifestyle)
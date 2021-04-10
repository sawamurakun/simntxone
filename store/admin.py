from django.contrib import admin
from .models.product import Product
from .models.user import User
from .models.driver import Driver
from .models.store import Store
from .models.advertising import Advertising
from .models.category import Category
from .models.subcategory import Subcategory
from .models.shopcategory import Shopcategory
from .models.order import Order
from .models.like import Like
from .models.notification import Notification
from .models.chat import Chat
from .models.coupon  import Coupon
# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Store)
admin.site.register(Advertising)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Shopcategory)
admin.site.register(Order)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(Chat)
admin.site.register(Coupon)
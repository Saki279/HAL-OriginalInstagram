from django.contrib import admin
from .models import Account
from .models import Post

admin.site.register(Account)

admin.site.register(Post)
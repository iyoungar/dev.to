from django.contrib import admin

from home.models import UserPost
from home.models import Post
# Register your mod(els here.
admin.site.register(UserPost)

admin.site.register(Post)
from django.contrib import admin
from base.models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog)

admin.site.register(Comment)




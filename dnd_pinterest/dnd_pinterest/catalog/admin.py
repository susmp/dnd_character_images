from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]

admin.site.register(Image, ImageAdmin)

#admin.site.register(Tags)

class TagsAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
#admin.site.register(Tags, TagsAdmin)



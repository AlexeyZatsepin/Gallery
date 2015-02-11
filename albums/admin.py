from django.contrib import admin

admin.AdminSite.site_header = '1 admin - 1 project'

from albums.models import Album, Photo , Comment,Avatar


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'album_user','slug', 'img']})
    ]
    list_display = ['title', 'slug','album_date']
    prepopulated_fields = {'slug': ['title']}
    ordering = ['title']
    list_filter=['album_date']

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'album', 'img']})
    ]
    list_display = ['title', 'album']
    ordering = ['title']
    list_filter=['photo_date']
	
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment)
admin.site.register(Avatar)
from django.contrib import admin
from .models import Artist, Album, Track, ArtistImage

# I register my models in my admin so I am able to inspect in my django admin interface


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "artist_id"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "album_id", "artist"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["track_id", "name", "album", "milliseconds"]


class ArtistImageAdmin(admin.ModelAdmin):
    list_display = ["image", "name"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(ArtistImage, ArtistImageAdmin)
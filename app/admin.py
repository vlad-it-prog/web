from django.contrib import admin
from .models import Band, Cash, Images, Client, ExportFileName, ExportFolderName, OtherTrackList, Person, \
    Song, Track

# Register your models here.


class BandInline(admin.StackedInline):
    model = Track
    model = Band
    extra = 1


class BandInline(admin.TabularInline):
    model = Band
    extra = 1


@admin.register(Band)
# admin.site.register(Band, BandAdmin)
class BandAdmin(admin.ModelAdmin):
    list_display = ("id", "band_name",)
    list_display_links = ("id", "band_name",)
    search_fields = ("band_name",)
    list_editable = ()
    # inlines = [BandInline]
    save_on_top = True
    save_as = True
    # list_editable = ("band_name",)
    # fields = ((),)
    # fieldsets = (
    #     (None, {
    #         "fields": (("", ""),)
    #     }),
    # )


@admin.register(Cash)
# admin.site.register(Cash, CashAdmin)
class CashAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)


@admin.register(Images)
# admin.site.register(Images, ImagesAdmin)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo",)
    list_display_links = ("id", "name", "photo",)


@admin.register(Client)
# admin.site.register(Client, ClientAdmin)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "address",)
    list_display_links = ("id", "user", "address", )
    search_fields = ("address", "user",)
    readonly_fields = ("user",)


@admin.register(ExportFileName)
# admin.site.register(ExportFileName, ExportFileNameAdmin)
class ExportFileNameAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)


@admin.register(ExportFolderName)
# admin.site.register(ExportFolderName, ExportFolderNameAdmin)
class ExportFolderNameAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject",)
    list_display_links = ("id", "name", "subject",)


# @admin.register(History)
# # admin.site.register(History, HistoryAdmin)
# class HistoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "time",)
#     list_display_links = ("id", "time",)
#     readonly_fields = ("time",)


@admin.register(OtherTrackList)
# admin.site.register(OtherTrackList, OtherTrackListAdmin)
class OtherTrackListAdmin(admin.ModelAdmin):
    list_display = ("id", "artist_name", "song_name",)
    list_display_links = ("id", "artist_name", "song_name",)


@admin.register(Person)
# admin.site.register(Person, PersonAdmin)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "credit_card_number",)
    list_display_links = ("id", "name", "credit_card_number",)


@admin.register(Song)
# admin.site.register(Song, SongAdmin)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "audio_file",)
    list_display_links = ("id", "name", "audio_file",)


@admin.register(Track)
# admin.site.register(Track, TrackAdmin)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "artist_name", "song_name",)
    list_display_links = ("id", "artist_name", "song_name",)
    list_filter = ("artist_name", "band__band_name")
    search_fields = ("artist_name", "song_name",)


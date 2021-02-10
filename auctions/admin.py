from django.contrib import admin

from .models import  User, Bid, Comment, AuctionListing

# Register your models here.
class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "description", "category", "sold", "price", "image", "itemAdded")

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(AuctionListing, AuctionListingAdmin)

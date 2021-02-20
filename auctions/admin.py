from django.contrib import admin

from .models import  User, Bid, Comment, AuctionListing, WishList, Comment

# Register your models here.
class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "description", "category", "sold", "price", "image", "itemAdded", "startingBid", "bidWinner", "createdBy")
    list_editable = ("item", "description", "category", "sold", "price", "image", "bidWinner", "createdBy")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "currentBid", "nextBid", "bidTime", "item", "user")
    list_editable = ("currentBid", "nextBid")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "time", "item", "user")
    list_editable = ("comment",)

class WishListAdmin(admin.ModelAdmin):
    list_display = ("id", "timeStamp", "item", "user")

    

admin.site.register(User)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(WishList, WishListAdmin)

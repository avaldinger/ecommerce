from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("details/<int:item_id>", views.details, name="details"),
    path("comment/<int:item_id>", views.addComment, name="comment"),
    path("addToWishlist/<int:item_id>", views.addToWishlist, name="addToWishlist"),
    path("removeFromWishlist/<int:item_id>", views.removeFromWishlist, name="removeFromWishlist"),
    path("wishlist", views.wishList, name="wishlist"),
    path("addBid/<int:item_id>", views.addBid, name="addBid"),
    path("endBidding/<int:item_id>", views.endBidding, name="endBidding"),
    path("purchased", views.wonAuctions, name="purchased"),
    path("categories", views.getAllCategories, name="categories"),
    path("categoryitems/<str:category>", views.getCategoryListing, name="categoryitems")  
]

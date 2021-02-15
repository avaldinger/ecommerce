from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import ModelForm, Textarea
from datetime import datetime
from django.db.models import Q

from .models import User, AuctionListing, Comment, WishList


class AuctionForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AuctionListing
        exclude = ['itemAdded', 'bid', 'comments', 'sold']
        widgets = {
            'description': Textarea(attrs={'cols': 100, 'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["item"].widget.attrs["placeholder"] = "Item"
        self.fields["item"].widget.attrs["autocomplete"] = "off"
        self.fields["price"].widget.attrs["placeholder"] = "Price €"
        self.fields["price"].widget.attrs["autocomplete"] = "off"
        self.fields['price'].widget.attrs['min'] = 0
        self.fields["category"].widget.attrs["placeholder"] = "Category"
        self.fields['category'].required = True
        self.fields['category'].empty_label = None
        self.fields['category'].initial = False
        self.fields["description"].widget.attrs["placeholder"] = "Here goes the description"
        self.fields["description"].widget.attrs["autocomplete"] = "off"
        self.fields["image"].widget.attrs["placeholder"] = "Image URL"
        self.fields["image"].widget.attrs["autocomplete"] = "off"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('item', css_class='form-group col-md-3 mb-0'),
                Column('price', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('category', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
            'description', css_class='form-group col-md-7 mb-0',
            ),
            Row(
                Column('image', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['time']
        widgets = {
            'comment': Textarea(attrs={'cols': 100, 'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = True
        self.fields["comment"].widget.attrs["placeholder"] = "Here goes your comment..."
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
            'comment', css_class='form-group col-md-7 mb-0',
            ),
            Submit('submit', 'Save comment')
        )


def index(request):
    # Return active items
    auction_list = AuctionListing.objects.filter(sold=False)
    return render(request, "auctions/index.html", {
        "auction_list": auction_list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createListing(request):
    if request.method == "POST":
        form = AuctionForm(request.POST)
        # Check form and save entry to the DataBase
        if form.is_valid():
            item = form.cleaned_data["item"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            category = form.cleaned_data["category"]
            newItem = AuctionListing(item=item, price=price, description=description, image=image, category=category, itemAdded=datetime.now(), sold=False)
            newItem.save()
    form = AuctionForm()
    return render(request, "auctions/create.html", {
        "form": form
    })

def details(request, item_id):
    # Return details of the selected item
    item = AuctionListing.objects.get(pk=item_id)
    form = CommentForm()
    user = request.user
    wish = WishList.objects.filter(Q(item=item_id)&Q(user=user))
    comments = Comment.objects.filter(item=item_id)
    return render(request, "auctions/details.html", {
        "item": item, "form": form, "comments": comments, "wish": wish
    })

def addComment(request, item_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data["comment"]
        user = request.user
        item = AuctionListing.objects.get(pk=item_id)
        print(user)
        print(item_id)
        print(item)
        newItem = Comment(comment=comment, item=item, time=datetime.now(), user=user)
        newItem.save()
    return HttpResponseRedirect(reverse("details", args=(item_id,)))

def addToWishlist(request, item_id):
    item = AuctionListing.objects.get(pk=item_id)
    user = request.user
    newItem = WishList(item=item, timeStamp=datetime.now(), user=user)
    newItem.save()
    return HttpResponseRedirect(reverse("details", args=(item_id,)))

def removeFromWishlist(request, item_id):
    user = request.user
    wishItem = WishList.objects.filter(Q(item=item_id)&Q(user=user))
    wishItem.delete()
    return HttpResponseRedirect(reverse("details", args=(item_id,)))

def wishList(request):
    user = request.user
    wishes = WishList.objects.filter(user=user)
    return render(request, "auctions/wishlist.html", {
        "wishes": wishes
    })



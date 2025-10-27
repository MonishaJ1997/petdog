from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("login",views.login,name="login"),
    path("cart",views.cart,name="cart"),
    path("dog",views.dog,name="dog"),
    path("cat",views.cat,name="cat"),
    path("smallpets",views.smallpets,name="smallpets"),
    path("buycart",views.buycart,name="buycart"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("petservice", views.petservice, name="petservice"),
     path("vetdoctor", views.vetdoctor, name="vetdoctor"),
     path("consultdoctor", views.consultdoctor, name="consultdoctor"),
     path("final", views.final, name="final"),
]

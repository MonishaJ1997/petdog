# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


from django.shortcuts import render
from .models import DogBanner, Product
from .models import Pet
from .models import PromoImage
from .models import BannerImage
from .models import CenterImage
from .models import PetService
from .models import Banner

def home(request):
    banner = DogBanner.objects.first()  # only one banner
    products = Product.objects.all()[:6]
    pets = Pet.objects.all()
    promo_image = PromoImage.objects.first()
    banners = BannerImage.objects.all()
    image = CenterImage.objects.first() 
    services = PetService.objects.all() 
    banners = Banner.objects.all().order_by("order")
   
    return render(request, 'home.html', {
        "banner": banner, 
        "products": products,
        'pets':pets,
        'promo_image': promo_image,  
        "banners": banners,
        "image": image,
        "services": services,
        "banners": banners,
        
        
        })



from django.shortcuts import render
from .models import Background
from .models import Aboutcontent
from .models import Card
from .models import PetSmartHighlight

def about(request):
    # Fetch the latest background image
    background = Background.objects.last()
    about_content = Aboutcontent.objects.first()
    cards = Card.objects.all() 
    image_obj = PetSmartHighlight.objects.last()
    return render(request, 'about.html', {
        
        'background': background,
        'aboutcontent': about_content,
        'cards': cards,
        'image_obj': image_obj
        })



from django.shortcuts import render
from .models import QuickLink, BrowseTopic

def contact(request):
    quick_links = QuickLink.objects.all().order_by('order')
    browse_topics = BrowseTopic.objects.all().order_by('order')
    return render(request, 'contact.html', {
        'quick_links': quick_links,
        'browse_topics': browse_topics,
    })


from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

from django.shortcuts import render
from decimal import Decimal
from .models import Productmain, PaymentMethod, FooterIcon

def cart(request):
    # Example: fetch all products (later you can filter by user cart/session)
    cart_items = Productmain.objects.all()

    subtotal = sum(item.price for item in cart_items)
    shipping = Decimal("99.00")
    total = subtotal + shipping
    tax = subtotal * Decimal("0.265")  # Example calculation

    payment_methods = PaymentMethod.objects.all()
    footer_icons = FooterIcon.objects.all()

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "shipping": shipping,
        "total": total,
        "tax": tax,
        "payment_methods": payment_methods,
        "footer_icons": footer_icons,
    }
    return render(request, "cart.html", context)


from django.shortcuts import render
from .models import PromoBanner, DogProduct
from .models import DogCardGreen

def dog(request):
    sort_by = request.GET.get("sort", "bestsellers")

    products = DogProduct.objects.all()

    # Sorting logic
    if sort_by == "price_low":
        products = products.order_by("price")
    elif sort_by == "price_high":
        products = products.order_by("-price")
    elif sort_by == "top_rated":
        products = products.order_by("-rating")
    elif sort_by == "new":
        products = products.order_by("-id")  # newest first

    banners = PromoBanner.objects.all()[:5]
    card = DogCardGreen.objects.first()  # show 5 promos

    return render(request, "dog.html", {
        "products": products,
        "banners": banners,
        "sort_by": sort_by,
        "card": card
    })






from django.shortcuts import render
from .models import PromoBanner, CatProduct

def cat(request):
    sort_by = request.GET.get("sort", "bestsellers")

    products = CatProduct.objects.all()

    # Sorting logic
    if sort_by == "price_low":
        products = products.order_by("price")
    elif sort_by == "price_high":
        products = products.order_by("-price")
    elif sort_by == "top_rated":
        products = products.order_by("-rating")
    elif sort_by == "new":
        products = products.order_by("-id")  # newest first

    banners = PromoBanner.objects.all()[:5]  # show 5 promos

    return render(request, "cat.html", {
        "products": products,
        "banners": banners,
        "sort_by": sort_by,
    })

from django.shortcuts import render
from .models import LargeImage,BackgroundImage,SlideImage,Product


def product_detail(request, pk):
    product = LargeImage.objects.get(pk=pk)
    background = BackgroundImage.objects.last()
    productsed = SlideImage.objects.all()
    products = Product.objects.all()[:6]
    images = [
        product.thumb1,
        product.thumb2,
        product.thumb3,
        product.thumb4,
        product.thumb5,
    ]
    # Remove None images
    images = [img for img in images if img]

    context = {
        "product": product,
        "images": images,
        "background": background,
        "productsed": productsed,
        "products": products,
        
    }
    return render(request, "product_detail.html", context)


from django.shortcuts import render

def buycart(request):
    return render(request, 'buycart.html')



from django.shortcuts import render, redirect
from .forms import OrderFormModel
from .models import OrderImage, PaymentIcon, PaymentMethod

def buycart(request):
    order_image = OrderImage.objects.first()
    payment_icons = PaymentIcon.objects.all()
    payment_methods = PaymentMethod.objects.all()

    if request.method == 'POST':
        form = OrderFormModel(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_image = order_image
            order.save()
            # redirect to final page after placing order
            return redirect('final')
    else:
        form = OrderFormModel()

    context = {
        'form': form,
        'order_image': order_image,
        'payment_icons': payment_icons,
        'payment_methods': payment_methods,
    }
    return render(request, 'buycart.html', context)



from django.shortcuts import render

def final(request):
    return render(request, 'final.html')




# views.py
# views.py
# views.py

from django.shortcuts import render
from .models import DogPet,DogPetServiceImage

def petservice(request):
    pet = DogPet.objects.first()
    center_image = DogPetServiceImage.objects.last()
    service_cards = [
        {"icon": "fa-scissors", "title": "Grooming"},
        {"icon": "fa-hotel", "title": "PetsHotel"},
        {"icon": "fa-bone", "title": "Doggie Day Camp"},
        {"icon": "fa-graduation-cap", "title": "Training"},
        {"icon": "fa-medkit", "title": "Veterinary Care"},
        {"icon": "fa-heart", "title": "Adoption"},
    ]
    return render(request, 'petservice.html', 
                  {'pet': pet,
                 'service_cards': service_cards,
                 'center_image': center_image
                 })




from django.shortcuts import render
from .models import SmallBanner, SmallProduct

def smallpets(request):
    sort_by = request.GET.get("sort", "bestsellers")

    products = SmallProduct.objects.all()

    # Sorting logic
    if sort_by == "price_low":
        products = products.order_by("price")
    elif sort_by == "price_high":
        products = products.order_by("-price")
    elif sort_by == "top_rated":
        products = products.order_by("-rating")
    elif sort_by == "new":
        products = products.order_by("-id")  # newest first

    banners = SmallBanner.objects.all()[:5]  # show 5 promos

    return render(request, "smallpets.html", {
        "products": products,
        "banners": banners,
        "sort_by": sort_by,
    })


# views.py
from django.shortcuts import render
from .models import VetDoctor
from .models import Consult
from .models import DogWomen
from .models import Doctors

def vetdoctor(request):
    vetdoctor = VetDoctor.objects.first()
    consults = Consult.objects.all()
    dogwomen = DogWomen.objects.first()
    doctors = Doctors.objects.all()  # Fetch the first i
    return render(request, 'vetdoctor.html', {
        'vetdoctor': vetdoctor,
        "consults": consults,
        "dogwomen": dogwomen,
         "doctors": doctors
        })

from django.shortcuts import render
from .models import DogSleep

def consultdoctor(request):
    dog = DogSleep.objects.first()  # fetch first uploaded image
    return render(request, "consultdoctor.html", {"dog": dog})



# views.py

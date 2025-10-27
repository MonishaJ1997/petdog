# models.py
from django.db import models

class SiteLogo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100, default="Site Logo")

    def __str__(self):
        return self.alt_text


from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pets/')  # uploaded images stored in MEDIA_ROOT/pets/

    def __str__(self):
        return self.name


from django.db import models

class DogBanner(models.Model):
    title = models.CharField(max_length=200, default="Stress-Free Summer")
    subtitle = models.CharField(max_length=255, default="Keep your pup calm along all season")
    image = models.ImageField(upload_to="dog_banner/")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    rating = models.PositiveIntegerField(default=0)  # 0–5 stars
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title





        

from django.db import models

class PromoImage(models.Model):
    image = models.ImageField(upload_to='promo_images/')

from django.db import models

class Background(models.Model):
    title = models.CharField(max_length=200, default="Our Mission")
    description = models.TextField(default="Every day with every connection, Petpalooza passionate associates help bring pet parents closer to their pets so they can live more fulfilled life")
    image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.title


from django.db import models

class Aboutcontent(models.Model):
    title = models.CharField(max_length=200, default="ANYTHING for PETS®")
    content = models.TextField(default="""
We love pets, and we believe loving pets makes us better people. That’s one of the many reasons we do Anything for Pets – because they will do anything for us. Anything for Pets is our commitment to pet parents, it’s how we do business and who we are as pet lovers. As the leader in pet care, we make our decisions based on how we can bring pet parents closer to their pets. From dressing in matching costumes, to finding the perfect treats and toys, we innovate solutions and unique, must-have products to create more ways for pets to be a part of our everyday lives. Our trusted and skilled associates share the same passion for pets as the pet parents we serve, helping pet parents choose from our offering of the largest variety of pet products and services in one convenient place – in your neighborhood or the palm of your hand. With more than 1,660 locations in North America, we pride ourselves on our unrivaled variety of pet food, treats, toys, and apparel, as well as our services including training, grooming, boarding and more.
""")

    def __str__(self):
        return self.title
    

    from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return self.title


from django.db import models

class PetSmartHighlight(models.Model):
    image = models.ImageField(upload_to='highlights/')

    def __str__(self):
        return f"Highlight {self.id}"


from django.db import models

class QuickLink(models.Model):
    """
    Stores information for a 'Quick Link' card including:
    - icon: an image file used as an icon on the card.
    - title: the main title text for the link.
    - description: a short descriptive text below the title.
    - order: an integer to determine display order.
    """
    icon = models.ImageField(upload_to='icons/quick_links/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0, help_text="Order for sorting display")

    def __str__(self):
        return self.title

class BrowseTopic(models.Model):
    """
    Stores 'Browse Topic' card info including:
    - icon: an image file used as an icon on the card.
    - title: the title text for the topic.
    - order: an integer to determine display order.
    """
    icon = models.ImageField(upload_to='icons/browse_topics/')
    title = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0, help_text="Order for sorting display")

    def __str__(self):
        return self.title
    
 
from django.db import models

# Product model
class Productcart(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Cart Item
class CartItem(models.Model):
    product = models.ForeignKey(Productcart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


# Icons model (for bottom section)
class InfoIcon(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to="icons/")

    def __str__(self):
        return self.title


from django.db import models

class BannerImage(models.Model):
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return f"Banner {self.id}"

from django.db import models

class CenterImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="center_images/")

    def __str__(self):
        return self.title if self.title else "Center Image"



from django.db import models

class PetService(models.Model):
    title = models.CharField(max_length=100)   # e.g. Grooming, Training
    description = models.TextField()           # e.g. Summer Salon Special...
    image = models.ImageField(upload_to="pet_services/")
    button_text = models.CharField(max_length=50, default="Learn More")

    def __str__(self):
        return self.title


from django.db import models

class FooterContent(models.Model):
    logo = models.ImageField(upload_to="footer_logo/", blank=True, null=True)

    def __str__(self):
        return "Footer Content"


class SocialIcon(models.Model):
    name = models.CharField(max_length=50)  # Facebook, Instagram, etc.
    icon = models.ImageField(upload_to="social_icons/")  # just image

    def __str__(self):
        return self.name


from django.db import models

# For left-side promotional banners
class PromoBanner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="promo_banners/")

    def __str__(self):
        return self.title

# For dog products
class DogProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="dog_products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=50, blank=True, null=True)  # e.g. "2 kg", "100gm"
    rating = models.FloatField(default=0.0)  # store avg rating e.g. 4.2
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name







from django.db import models

# For left-side promotional banners
class CatBanner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="promo_banners/")

    def __str__(self):
        return self.title

# For dog products
class CatProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="cat_products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=50, blank=True, null=True)  # e.g. "2 kg", "100gm"
    rating = models.FloatField(default=0.0)  # store avg rating e.g. 4.2
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name




from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="banners/")   # Dog image or main image
    extra_image1 = models.ImageField(upload_to="banners/", blank=True, null=True) # optional (icons, etc.)
    extra_image2 = models.ImageField(upload_to="banners/", blank=True, null=True) # optional (icons, etc.)
    offer_text = models.CharField(max_length=100, blank=True, null=True)  # e.g. "Only @ 399"
    button_text = models.CharField(max_length=50, default="Shop Now")
    button_link = models.URLField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)   # To control sequence

    def __str__(self):
        return self.title or f"Banner {self.id}"



from django.db import models

class ProductDetail(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductImageDetail(models.Model):
    product = models.ForeignKey(
        ProductDetail,                # ✅ FIXED
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"{self.product.title} image"



        # models.py
from django.db import models

class BackgroundImage(models.Model):
    title = models.CharField(max_length=100, default="Dog Food Background")
    image = models.ImageField(upload_to="backgrounds/")  # stores uploaded image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





from django.db import models

class SlideImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="slide_images/")
    rating = models.IntegerField(default=0)   # out of 5
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=50, default="")  # e.g., "60g", "90 Soft Chews"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


    from django.db import models

class PaymentIcon(models.Model):
    name = models.CharField(max_length=50)
    icon_image = models.ImageField(upload_to='payment_icons/')

    def __str__(self):
        return self.name

class OrderImage(models.Model):
    image = models.ImageField(upload_to='order_images/')
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title or "Order Image"

class OrderForm(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    pincode = models.CharField(max_length=12)
    phone = models.CharField(max_length=20)
    save_for_next = models.BooleanField(default=False)
    PAYMENT_CHOICES = [
        ("online", "Secure transaction (UPI, Cards, Wallets, Net banking)"),
        ("cod", "Cash on Delivery")
    ]
    payment_method = models.CharField(max_length=12, choices=PAYMENT_CHOICES)
    order_image = models.ForeignKey(OrderImage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order by {self.email}"




from django.db import models

class ProductCartItems(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class TotalItems(models.Model):
    product = models.ForeignKey(ProductCartItems, on_delete=models.CASCADE, related_name='total_items')
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"



from django.db import models
from decimal import Decimal

# Product model (for products shown in cart)
class Productmain(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Payment method logos
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="payment_icons/")

    def __str__(self):
        return self.name


# Footer icons (question, secure shopping, privacy, etc.)
class FooterIcon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="footer_icons/")

    def __str__(self):
        return self.title



from django.db import models

class DogCardGreen(models.Model):
    title = models.CharField(max_length=255)
    left_image = models.ImageField(upload_to='dogcardgreen/')
    right_image = models.ImageField(upload_to='dogcardgreen/')

    def __str__(self):
        return self.title


from django.db import models

class LargeImage(models.Model):
    title = models.CharField(max_length=200, default="Product Image")
    main_image = models.ImageField(upload_to="products/main/")   # Big image
    thumb1 = models.ImageField(upload_to="products/thumbs/", blank=True, null=True)
    thumb2 = models.ImageField(upload_to="products/thumbs/", blank=True, null=True)
    thumb3 = models.ImageField(upload_to="products/thumbs/", blank=True, null=True)
    thumb4 = models.ImageField(upload_to="products/thumbs/", blank=True, null=True)
    thumb5 = models.ImageField(upload_to="products/thumbs/", blank=True, null=True)

    def __str__(self):
        return self.title


# models.py

# models.py

# models.py

from django.db import models

class DogPet(models.Model):
    name = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)

    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

       

# models.py
from django.db import models

class DogPetServiceImage(models.Model):
    image = models.ImageField(upload_to='petservices/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Dog Pet Service Image {self.id}"




from django.db import models

# For left-side promotional banners
class SmallBanner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="small_banners/")

    def __str__(self):
        return self.title

# For dog products
class SmallProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="small_products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=50, blank=True, null=True)  # e.g. "2 kg", "100gm"
    rating = models.FloatField(default=0.0)  # store avg rating e.g. 4.2
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


from django.db import models

class VetDoctor(models.Model):
    title = models.CharField(max_length=255, default='Instant and complete vet care')
    description = models.TextField(default='Wherever you are At only 299 , get end-to-end support from our vets')
    button_text = models.CharField(max_length=50, default='Consult Now')
    image = models.ImageField(upload_to='vetdoctor_images/')

    def __str__(self):
        return self.title


from django.db import models

class Consult(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="consult_icons/")

    def __str__(self):
        return self.title


from django.db import models

class DogWomen(models.Model):
    image = models.ImageField(upload_to="dogwomen/")

    def __str__(self):
        return f"Dog & Woman Image {self.id}"

from django.db import models

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    experience = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="doctors/")

    def __str__(self):
        return self.name


from django.db import models

class DogSleep(models.Model):
    image = models.ImageField(upload_to='dogsleep/')

    def __str__(self):
        return f"DogSleep {self.id}"


from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_images/')

    def __str__(self):
        return self.name

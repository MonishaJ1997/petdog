from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SiteLogo

@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image')  # Columns shown in the admin list view
    search_fields = ('alt_text',)         # Search bar in admin

from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
from django.contrib import admin
from .models import DogBanner, Product

@admin.register(DogBanner)
class DogBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "rating")
    list_filter = ("rating",)
    search_fields = ("title",)


from django.contrib import admin
from .models import PromoImage

admin.site.register(PromoImage)


from django.contrib import admin
from .models import Background

@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('title',)

from django.contrib import admin
from .models import Aboutcontent

@admin.register(Aboutcontent)
class AboutcontentAdmin(admin.ModelAdmin):
    list_display = ('title',)


from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

from django.contrib import admin
from .models import PetSmartHighlight

@admin.register(PetSmartHighlight)
class PetSmartHighlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']





from django.contrib import admin
from django.utils.html import format_html
from .models import QuickLink, BrowseTopic

@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order')
    ordering = ['order']
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: contain;" />', obj.icon.url)
        return ""
    icon_preview.short_description = 'Icon Preview'

@admin.register(BrowseTopic)
class BrowseTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ['order']
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: contain;" />', obj.icon.url)
        return ""
    icon_preview.short_description = 'Icon Preview'



from django.contrib import admin
from .models import Productcart, CartItem, InfoIcon

@admin.register(Productcart)
class ProductcartAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "subtotal")

@admin.register(InfoIcon)
class InfoIconAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")


from django.contrib import admin
from .models import BannerImage

@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


from django.contrib import admin
from .models import CenterImage

@admin.register(CenterImage)
class CenterImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


from django.contrib import admin
from .models import PetService

@admin.register(PetService)
class PetServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image")


from django.contrib import admin
from .models import FooterContent, SocialIcon

@admin.register(FooterContent)
class FooterContentAdmin(admin.ModelAdmin):
    list_display = ("id", "logo",)

@admin.register(SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "icon")



from django.contrib import admin
from .models import PromoBanner, DogProduct

@admin.register(PromoBanner)
class PromoBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(DogProduct)
class DogProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rating", "reviews_count")




from django.contrib import admin
from .models import CatBanner, CatProduct

@admin.register(CatBanner)
class PromoBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(CatProduct)
class DogProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rating", "reviews_count")



from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order",)



from django.contrib import admin
from .models import ProductDetail, ProductImageDetail

class ProductImageInline(admin.TabularInline):   # Inline images
    model = ProductImageDetail
    extra = 1   # show 1 extra empty field by default


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "price", "coupon_code")
    search_fields = ("title", "brand")
    inlines = [ProductImageInline]


@admin.register(ProductImageDetail)
class ProductImageDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "image")


# admin.py
from django.contrib import admin
from .models import BackgroundImage

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")



from django.contrib import admin
from .models import SlideImage

@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ("title", "rating", "price", "quantity", "created_at")
    list_filter = ("rating",)
    search_fields = ("title",)


from django.contrib import admin
from .models import LargeImage

@admin.register(LargeImage)
class LargeImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title")






from django.contrib import admin
from .models import Productmain, PaymentMethod, FooterIcon

@admin.register(Productmain)
class ProductmainAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")

@admin.register(FooterIcon)
class FooterIconAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "icon")


from django.contrib import admin
from .models import DogCardGreen

@admin.register(DogCardGreen)
class DogCardGreenAdmin(admin.ModelAdmin):
    list_display = ('title', 'left_image_tag', 'right_image_tag')

    readonly_fields = ('left_image_tag', 'right_image_tag')

    def left_image_tag(self, obj):
        if obj.left_image:
            return format_html('<img src="{}" style="height:80px;"/>', obj.left_image.url)
        return "-"
    left_image_tag.short_description = 'Left Image'

    def right_image_tag(self, obj):
        if obj.right_image:
            return format_html('<img src="{}" style="height:80px;"/>', obj.right_image.url)
        return "-"
    right_image_tag.short_description = 'Right Image'


# admin.py
# admin.py
# admin.py

from django.contrib import admin
from .models import DogPet

admin.site.register(DogPet)



# admin.py
from django.contrib import admin
from .models import DogPetServiceImage

@admin.register(DogPetServiceImage)
class PetServiceImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at']



    
from django.contrib import admin
from .models import SmallBanner, SmallProduct

@admin.register(SmallBanner)
class SmallBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(SmallProduct)
class SmallProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rating", "reviews_count")



from django.contrib import admin
from .models import VetDoctor

@admin.register(VetDoctor)
class VetDoctorAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')


from django.contrib import admin
from .models import Consult

@admin.register(Consult)
class ConsultAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')


from django.contrib import admin
from .models import DogWomen

@admin.register(DogWomen)
class DogWomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

    from django.contrib import admin
from .models import Doctors

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'qualification')



from django.contrib import admin
from .models import DogSleep

@admin.register(DogSleep)
class DogSleepAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

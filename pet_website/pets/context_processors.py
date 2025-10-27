from .models import SiteLogo


def site_logo(request):
    logo = SiteLogo.objects.first()
    return {"site_logo": logo}

from .models import FooterContent, SocialIcon

def footer_context(request):
    footer_logo = FooterContent.objects.first()
    social_icons = SocialIcon.objects.all()
    return {
        "footer_logo": footer_logo,
        "social_icons": social_icons,
    }

from .models import Brand
def brand(request):
     brands = Brand.objects.all()
     return{
         "brands":brands
     }
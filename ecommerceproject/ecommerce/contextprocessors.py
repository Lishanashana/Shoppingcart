# to set all links
from .models import Product,Category

def menulinks(request):
    links=Category.objects.all()
    return dict(links=links)
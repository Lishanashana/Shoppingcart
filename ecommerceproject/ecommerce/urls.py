from .import views
from django.urls import path
app_name='ecommerce'




urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:cslug>/',views.allProductCat,name='productbycategory'),
    path('<slug:cslug>/<slug:productslug>/',views.productDetail,name='productcatDetail'),
]
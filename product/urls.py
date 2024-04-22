from django.urls import path
from product import views as v
urlpatterns = [
    path('', v.index, name='index'),
    path('product/about/', v.about, name='about'),
    path('product/',v.product,name='product'),
    path('testimonial/',v.testimonial,name='testimonial'),
    path('whyus',v.whyus,name='whyus')
]
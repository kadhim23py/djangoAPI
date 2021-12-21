from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4
from django.contrib.auth import get_user_model

from account.authorization import GlobalAuth
from commerce.models import Product, Label,artist, Category
from commerce.schemas import ProductOut,  LabelOut, MessageOut, CategoryOut, ArtistOut

commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])
User = get_user_model()



@commerce_controller.get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products


@commerce_controller.get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)






@commerce_controller.get('Label', response={
    200: List[LabelOut],
})
def list_label(request):
    label = Label.objects.all()
    # label = Label.filter(name='tshirt')
    return label


@commerce_controller.get('Label/{id}', response={
    200: LabelOut
})
def retrieve_Label(request, id):
    return get_object_or_404(Label, id=id)








def list_Artists(request):
    Artists = artist.objects.all()
    return Artists


@commerce_controller.get('Artists/{id}', response={
    200: ArtistOut
})
def retrieve_Artist(request, id):
    return get_object_or_404(artist, id=id)




# create all crud operations for Label, Merchant, Artist, Category

@commerce_controller.get('Categorys', response={
    200: List[CategoryOut],
})
def list_Categorys(request):
    categorys = Category.objects.all()

    return categorys


@commerce_controller.get('Categorys/{id}', response={
    200: CategoryOut
})
def retrieve_Category(request, id):
    return get_object_or_404(Category, id=id)




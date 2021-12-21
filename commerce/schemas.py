import datetime
from typing import List

from ninja import Schema
from pydantic import UUID4


class MessageOut(Schema):
    detail: str


class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str

class LabelOut(Schema):
    id: UUID4
    name: str



class ArtistOut(Schema):
    id: UUID4
    name: str
    image: str


class ProductImage(Schema):
    image:str
    is_default_image:bool



class ProductOut(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category: CategoryOut
    artist: ArtistOut
    label: LabelOut
    images: List[ProductImage]


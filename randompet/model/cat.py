from marshmallow import post_load, fields

from .pet import Pet, PetSchema
from .pet_type import PetType

class Cat(Pet):
    def __init__(self, file, source_url):
        super().__init__(PetType.CAT, file, source_url)

    #__tablename__ = None 
    __mapper_args__ = {
        'polymorphic_identity': 'cat'
    }

    def __repr__(self):
        return '<Cat [{}]>'.format(self.file)


class CatSchema(PetSchema):
    type = None

    class Meta:
        model = Cat
        fields = ['file', 'source_url', 'created_at']
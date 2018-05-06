from marshmallow import post_load, fields

from .pet import Pet, PetSchema
from .pet_type import PetType

class Dog(Pet):
    def __init__(self, file, source_url):
        super().__init__(PetType.DOG, file, source_url)

    #__tablename__ = None 
    __mapper_args__ = {
        'polymorphic_identity': 'dog'
    }

    def __repr__(self):
        return '<Dog [{}]>'.format(self.file)


class DogSchema(PetSchema):
    type = None

    class Meta:
        model = Dog
        fields = ['file', 'source_url', 'created_at']
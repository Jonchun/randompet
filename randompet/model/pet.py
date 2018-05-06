import datetime as dt

from marshmallow import fields

from randompet import db, ma

BASE_URL = 'http://localhost:5000/'

class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    source_url = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    __mapper_args__ = {
        'polymorphic_identity': 'pet',
        'polymorphic_on': type,
    }

    def __init__(self, type, file, source_url):
        self.type = type.value
        self.file = file
        self.source_url = source_url
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Pet ({}) [{}]>'.format(self.type, self.file)

    @property
    def full_url(self):
        return BASE_URL + self.file

class PetSchema(ma.ModelSchema):
    type = fields.Str(required=True)
    file = fields.Str(required=True)
    source_url = fields.Str(required=True)
    created_at = fields.Date()

    class Meta:
        model = Pet
        fields = ['file', 'source_url', 'created_at']
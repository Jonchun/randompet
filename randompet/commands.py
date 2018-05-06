from randompet import db
from randompet.app import app
from randompet.helpers import random_string

from randompet.model.cat import Cat
from randompet.model.dog import Dog

@app.cli.command('seed_db', short_help='Seeds database with demo content.')
def seed_db():
    for i in range(1,10):
        dog = Dog('dog{}.png'.format(i), 'https://imgur.com/{}'.format(random_string(5)))
        db.session.add(dog)

    for i in range(1,10):
        cat = Cat('cat{}.png'.format(i), 'https://imgur.com/{}'.format(random_string(5)))
        db.session.add(cat)

    db.session.commit()
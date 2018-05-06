from flask import jsonify, request
from sqlalchemy.sql import func

from randompet import app, db
from randompet.model.dog import Dog, DogSchema

@app.route('/dog', methods=["GET"])
def get_dog():
    dog_schema = DogSchema()
    all_dogs = Dog.query.order_by(func.random()).first()
    return dog_schema.jsonify(all_dogs)

@app.route('/dog', methods=["POST"])
def create_dog():
    dog_schema = DogSchema()
    dog, errors = dog_schema.load(request.form)

    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(dog)
    db.session.commit()

    resp = jsonify({"message": "created"})
    resp.status_code = 201
    return resp

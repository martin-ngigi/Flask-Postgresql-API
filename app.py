from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://martin:1234@localhost/pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        # call your method here
        app.run(debug=True)

#MODEL

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_type = db.Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return "<Pet %r>" % self.pet_name

with app.app_context():
  # call your method here
  db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Hello. Its Wainaina"})


@cross_origin()
@app.route('/pets', methods = ['POST'])
def create_pet():
    pet_data = request.json

    pet_name = pet_data['pet_name']
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_description = pet_data['pet_description']

    pet = Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_description =pet_description )
    db.session.add(pet)
    db.session.commit()
    

    return jsonify({"success": True,"response":"Pet added successfully", "pet": pet_data})
from flask import Flask, request, jsonify
from models import db, Person

# Flask Application
app = Flask(__name__)

# Configure the database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to my Webpage"})


@app.route('/persons', methods=['POST'])

def create_person():
    try:        
        # Extract data from the request
        data = request.json
        name = data['name']
        age = data.get('age')
        email = data.get('email')


        # Create a new person
        person = Person(name=name, age=age, email=email)
        db.session.add(person)
        db.session.commit()

        return jsonify({'message': 'Person created successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/persons/<int:id>', methods=['GET'])

def get_person(id):
    try:
        person = Person.query.get(id)
        if person:
            return jsonify(person.serialize()), 200
        else:
            return jsonify({'message': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/persons/<int:id>', methods=['PUT'])

def update_person(id):
    try:
        data = request.json
        person = Person.query.get(id)


        if person:
            if 'name' in data:
                person.name = data['name']
            if 'age' in data:
                person.age = data['age']

            if 'email' in data:
                person.email = data['email']

            db.session.commit()
            return jsonify({'message': 'Person updated successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@app.route('/persons/<int:id>', methods=['DELETE'])

def delete_person(id):
    try:
        
        person = Person.query.get(id)

        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Person deleted successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
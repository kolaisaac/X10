from flask import Flask, request, jsonify
from main import db, Person

# Flask Application
app = Flask(__name__)

# Configure the database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
db.init_app(app)

@app.route('/persons', methods=['POST'])

def create_person():
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

if __name__ == '__main__':
    app.run(debug=True)
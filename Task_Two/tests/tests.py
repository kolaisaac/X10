import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db, Person

class TestPersonAPI(unittest.TestCase):

    # SetUp

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_create_person(self):
        data = {'name': 'Musk', 'age': 32, 'email': 'musk@example.com'}
        response = self.app.post('/persons', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_person(self):
        # Create a person
        person = Person(name='Blest', age=30, email='blest@example.com')
        db.session.add(person)
        db.session.commit()

        response = self.app.get(f'/persons/{person.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Blest')

    def test_update_person(self):
        # Create a person
        person = Person(name='Mark', age=35, email = 'mark@example.com')
        db.session.add(person)
        db.session.commit()

        # Update
        updated_data = {'name': 'Markson', 'age': 45, 'email': 'markson@example.com'}
        response = self.app.put(f'/persons/{person.id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Check if the person was updated
        updated_person = Person.query.get(person.id)
        self.assertEqual(updated_person.name, 'Markson')

    def test_delete_person(self):
        # Create a person
        person = Person(name='Peter', age=42, email = 'peter@example.com')
        db.session.add(person)
        db.session.commit()

        # Response
        response = self.app.delete(f'/persons/{person.id}')
        self.assertEqual(response.status_code, 200)

        # Check if the person was deleted
        deleted_person = Person.query.get(person.id)
        self.assertEqual(deleted_person)


if __name__ == '__main__':
    unittest.main()
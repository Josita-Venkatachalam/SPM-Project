import unittest
import flask_testing
import json
from app import app, db, Skill,Course,Role,Role_Skill,Course_Skill,LearningJourney,Learning_Journey_Courses,registration

#logic differs , but the assertions and lib we are using for both unit and integration tests is the same
#only the implementation will vary 
class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateLearningJourney(TestApp):
    def test_create_learning_Journey(self):
        lj1 = LearningJourney(Completion_Status="In progress" ,Roles_id=2 ,Staff_ID=130001)
        db.session.add(lj1)
        db.session.commit()

        request_body = {
            'Completion_Status': lj1.Completion_Status,
            'Roles_id': lj1.Roles_id,
            'Staff_ID': lj1.Staff_ID
        }

        response = self.client.post("/createLJ",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json, {
            
            "data": {
                "Completion_Status": "In Progress",
                "Roles_id": 2,
                "Staff_ID": 130001,
                "id": 2
            },
            "message": "Learning Journey Created!"
            
        })

class TestCreateRole(TestApp):
    def test_create_role(self):
        role1 = Role(name='Project Manager' ,description='A Project Manager manages a team of people.')
        db.session.add(role1)
        db.session.commit()

        request_body = {
            'name': role1.name,
            'description': role1.description
        }

        response = self.client.post("/createRole",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json, {
            
            "data": {
                'id': 1,
                'name': 'Project Manager',
                'desciption': 'A Project Manager manages a team of people.'

            },
            "message": "Role Created!"
            
        })
    def test_reject_create_role(self):
        role1 = Role(name='Project Manager' ,description='A Project Manager manages a team of people.')
        db.session.add(role1)
        db.session.commit()

        request_body = {
            'id': role1.id,
            'name': role1.name,
            'description': role1.description
        }
        response = self.client.post("/createRole",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "code": 400,
            "message": "Role already exists"
        })

    def test_reject_create_empty_role(self):

        request_body = {
            'id': 1,
            'name': '',
            'description': ''
        }
        response = self.client.post("/createRole",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "code": 400,
            "message": "There are empty fields, please enter the Role Name and Role Description."
        })
    # def test_create_consultation_invalid_doctor(self):
    #     p1 = Patient(name='Hyacinth Bucket', title='Mrs',
    #                  contact_num='+65 8888 8888', ewallet_balance=15)
    #     db.session.add(p1)
    #     db.session.commit()

    #     request_body = {
    #         'doctor_id': p1.id,
    #         'patient_id': p1.id,
    #         'diagnosis': 'Itchy armpits',
    #         'prescription': 'Better deodrant',
    #         'length': 15
    #     }

    #     response = self.client.post("/consultations",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 500)
    #     self.assertEqual(response.json, {
    #         'message': 'Doctor not valid.'
    #     })

    # def test_create_consultation_invalid_patient(self):
    #     d1 = Doctor(name='Imran', title='Dr',
    #                 reg_num='UKM123', hourly_rate=30)
    #     db.session.add(d1)
    #     db.session.commit()

    #     request_body = {
    #         'doctor_id': d1.id,
    #         'patient_id': d1.id,
    #         'diagnosis': 'Itchy armpits',
    #         'prescription': 'Better deodrant',
    #         'length': 15
    #     }

    #     response = self.client.post("/consultations",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 500)
    #     self.assertEqual(response.json, {
    #         'message': 'Patient not valid.'
    #     })

    # def test_create_consultation_insufficient_balance(self):
    #     d1 = Doctor(name='Imran', title='Dr',
    #                 reg_num='UKM123', hourly_rate=30)
    #     p1 = Patient(name='Hyacinth Bucket', title='Mrs',
    #                  contact_num='+65 8888 8888', ewallet_balance=15)
    #     db.session.add(d1)
    #     db.session.add(p1)
    #     db.session.commit()

    #     request_body = {
    #         'doctor_id': d1.id,
    #         'patient_id': p1.id,
    #         'diagnosis': 'Itchy armpits',
    #         'prescription': 'Better deodrant',
    #         'length': 60
    #     }

    #     response = self.client.post("/consultations",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 500)
    #     self.assertEqual(response.json, {
    #         'message': 'Patient does not have enough e-wallet funds.'
    #     })


if __name__ == '__main__':
    unittest.main()

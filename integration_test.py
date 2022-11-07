import unittest
import flask_testing
import json
from app import app, db, Skill,Course,Role,Role_Skill,Course_Skill,LearningJourney,Learning_Journey_Courses,Registration

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
        lj1 = LearningJourney(Completion_Status="In Progress" ,Roles_id=2 ,Staff_ID=130001)
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
        #print("LJ response.json")
        #print(response.json)
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
        role1 = Role(name='Marketing Director' ,description='A Marketing Director is in charge of managing any given campaign.')
        # db.session.add(role1)
        # db.session.commit()

        request_body = {
            'name': role1.name,
            'description': role1.description,
        }
        print('response body below')
        print(request_body)

        response = self.client.post("/roles_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print('create role response.json below')
        print(response.json)
        self.assertEqual(response.json, {
            
            "data": {
                'description': 'A Marketing Director is in charge of managing any given campaign.', 
                'id': 1, 
                'isDeleted': 0, 
                'name': 'Marketing Director'
            },
            "message": "Role Created!"
            
        })
    # def test_reject_create_role(self):
    #     role1 = Role(name='Project Manager' ,description='A Project Manager manages a team of people.')
    #     db.session.add(role1)
    #     db.session.commit()

    #     request_body = {
    #         'name': role1.name,
    #         'description': role1.description
    #     }
    #     response = self.client.post("/roles_add",
    #                                 data= json.dumps(request_body),
    #                                 content_type='application/json')
        
    #     self.assertEqual(response.json, {
    #         "code": 400,
    #         "message": "Role already exists"
    #     })

    def test_reject_create_empty_role_name(self):

        request_body = {
            'name': '',
            'description': 'A Marketing Director is in charge of managing any given campaign.'
        }
        response = self.client.post("/roles_add",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Please fill in the Role name."
        })

    def test_reject_create_empty_role_desc(self):

        request_body = {
            'name': 'Marketing Director',
            'description': ''
        }
        response = self.client.post("/roles_add",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Please fill in the Role description."
        })

    def test_reject_create_duplicate_role(self):
        role_1 = Role(name = 'Marketing Director', description = 'A Marketing Director is in charge of managing any given campaign.')
        role_2 = Role(name = 'Marketing Director', description = 'A Marketing Director is in charge of managing any given campaign.')
        db.session.add(role_1)
        db.session.add(role_2)
        db.session.commit()

        request_body_1 = {
            'name': role_1.name,
            'description': role_1.description,
        }

        response1 = self.client.post("/roles_add",
                                    data= json.dumps(request_body_1),
                                    content_type='application/json')

        request_body_2 = {
            'name': role_2.name,
            'description': role_2.description,
        }

        response = self.client.post("/roles_add",
                                    data= json.dumps(request_body_2),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Role name already exists. Please enter unique role name."
        })

    # class TestUpdateSkill(TestApp):
#     def test_update_skill(self):
#         existing_skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
#         updated_skill = Skill(name = 'Communication', description = 'Learn to communicate well in a team.')
#         db.session.add(existing_skill)
#         db.session.add(updated_skill)
#         db.session.commit()

#         request_body = {
#             'name': existing_skill.name,
#             'description': existing_skill.description,
#         }

#         response = self.client.post("/skills_add",
#                             data=json.dumps(request_body),
#                             content_type='application/json')

#         print("RESPONSE")
#         print(response.json)
#         skill_id = "0"

#         request_body_existing = {
#             'name': existing_skill.name,
#             'description': existing_skill.description,
#         }

#         self.client.post("/skills_update/" + skill_id,
#                                 content_type='application/json')
        
#         self.assertEqual(response.json, {
            
#             "data": {
#                     'description': 'Learn to communicate well in a team.',
#                     'id': 2,
#                     'isDeleted' : 0,
#                     'name': 'Communication'
#             },
#             "message": "Skill Created!"
            
#         })

class TestCreateSkill(TestApp):
    def test_create_skill(self):
        skill_1 = Skill(name = 'Test Skill Name', description = 'Test Skill Description')
        #db.session.add(skill_1)
        #db.session.commit()

        request_body = {
            'name': skill_1.name,
            'description': skill_1.description,
        }

        #print(request_body)

        response = self.client.post("/skills_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        #print(response.json)
        self.assertEqual(response.json, {
            "data": {
                    'description': 'Test Skill Description',
                    'id': 1,
                    'isDeleted' : 0,
                    'name': 'Test Skill Name'
            },
            "message": "Skill Created!"
        })

    def test_reject_create_empty_skill_name(self):
        request_body = {
            'name': '',
            'description': 'Learn to communicate well in a team.'
        }
        response = self.client.post("/skills_add",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Please fill in the Skill name."
        })

    def test_reject_create_empty_skill_desc(self):
        request_body = {
            'name': 'Communication',
            'description': ''
        }
        response = self.client.post("/skills_add",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Please fill in the Skill description."
        })

    def test_reject_create_duplicate_skill(self):
        skill = Skill(name = 'Communication', description = 'Learn to communicate well in a team.')
        db.session.add(skill)
        db.session.commit()

        request_body = {
            'name': skill.name,
            'description': skill.description,
        }

        response = self.client.post("/skills_add",
                                    data= json.dumps(request_body),
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Skill name already exists. Please enter unique skill name."
        })

class TestUpdateSkill(TestApp):
    def test_update_skill(self):
        #print ("update skill")
        existing_skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
        updated_skill = Skill(name = 'Communication', description = 'Learn to communicate well in a team.')

        request_body = {
            'name': existing_skill.name,
            'description': existing_skill.description
        }

        response = self.client.post("/skills_add",
                            data=json.dumps(request_body),
                            content_type='application/json')

        #print("RESPONSE ID: " + str(response.json['data']['id']))

        skill_id = str(response.json['data']['id'])
        skill_name = updated_skill.name
        skill_description = updated_skill.description

        response_2 = self.client.put("/skills_update/" + skill_id + "/" + skill_name + "/" + skill_description,
                                content_type='application/json')
        
        self.assertEqual(response_2.json, {
            "message": "Successfully updated!"          
        })

    #when valid_update is commented out
    #self.client.put just not routing to our app.py update function when skill name is empty

    #when valid_update is NOT commented out
    #self.client.put takes its input rather than the new input
    # def test_reject_update_empty_skill_name(self):
    #     #print ("update skill")
    #     existing_skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
    #     updated_skill = Skill(name = '', description = 'Test desc')

    #     request_body = {
    #         'name': existing_skill.name,
    #         'description': existing_skill.description
    #     }

    #     response = self.client.post("/skills_add",
    #                         data=json.dumps(request_body),
    #                         content_type='application/json')

    #     skill_id = str(response.json['data']['id'])
    #     skill_name = updated_skill.name
    #     skill_description = updated_skill.description

    #     #print("Skill ID: " + skill_id)
    #     #print("Skill Name: " + skill_name)
    #     #print("Skill Desc: " + skill_description)

    #     response_2 = self.client.put("/skills_update/" + skill_id + "/" + skill_name + "/" + skill_description,
    #                         content_type='application/json')
        
    #     self.assertEqual(response_2.json, {
    #         "message": "There are empty fields, please enter the Skill Name."          
    #     })


    #when valid_update is commented out
    #self.client.put just not routing to our app.py update function when skill name is empty

    #when valid_update is NOT commented out
    #self.client.put takes its input rather than the new input
    # def test_reject_update_empty_skill_desc(self):
    #     print ("update skill")
    #     existing_skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
    #     updated_skill = Skill(name = 'Test name', description = '')

    #     request_body = {
    #         'name': existing_skill.name,
    #         'description': existing_skill.description
    #     }

    #     response = self.client.post("/skills_add",
    #                         data=json.dumps(request_body),
    #                         content_type='application/json')

    #     skill_id = str(response.json['data']['id'])
    #     skill_name = updated_skill.name
    #     skill_description = updated_skill.description

    #     print("Skill ID: " + skill_id)
    #     print("Skill Name: " + skill_name)
    #     print("Skill Desc: " + skill_description)

    #     response_2 = self.client.put("/skills_update/" + skill_id + "/" + skill_name + "/" + skill_description,
    #                         content_type='application/json')
        
    #     self.assertEqual(response_2.json, {
    #         "message": "There are empty fields, please enter the Skill Description."          
    #     })

    def test_reject_update_duplicate_skill(self):
        skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')

        request_body = {
            'name': skill.name,
            'description': skill.description
        }

        response = self.client.post("/skills_add",
                            data=json.dumps(request_body),
                            content_type='application/json')

        #print("RESPONSE ID: " + str(response.json['data']['id']))

        skill_id = str(response.json['data']['id'])
        skill_name = skill.name
        skill_description = skill.description

        response_2 = self.client.put("/skills_update/" + skill_id + "/" + skill_name + "/" + skill_description,
                                content_type='application/json')
        
        self.assertEqual(response_2.json, {
            "message": "Skill name already exists. Please enter unique skill name."        
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

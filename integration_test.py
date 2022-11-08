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

class TestGetLearningJourney(TestApp):
    def test_get_lj_by_staffID(self):
        lj_1 = LearningJourney(Completion_Status="In progress", Roles_id=2 , Staff_ID = 130001)
        lj_2 = LearningJourney(Completion_Status="In progress", Roles_id=3 , Staff_ID = 130001)
        db.session.add(lj_1)
        db.session.add(lj_2)
        db.session.commit()
        
        Staff_ID = 130001

        response = self.client.get("/LearningJourney_Test/" + str(Staff_ID),
                                    content_type='application/json')
        print("Hi I am here!!")
        print(response.json)
        self.assertEqual(response.json, {
           
            "data": [
                    {
                    "Completion_Status": "In progress", 
                    "Roles_id": 2, 
                    "Staff_ID": 130001, 
                    "id": 1
                    }, 
                    {
                    "Completion_Status": "In progress", 
                    "Roles_id": 3, 
                    "Staff_ID": 130001, 
                    "id": 2
                    }
            ]
            
        })
    def test_get_lj_by_ljID(self):
        
        learningjourney = LearningJourney(Completion_Status="In progress", Roles_id=2 , Staff_ID = 140002)

        db.session.add(learningjourney)
        db.session.commit()

        request_body = {
            'Completion_Status': learningjourney.Completion_Status,
            'Roles_id': learningjourney.Roles_id,
            'Staff_ID': learningjourney.Staff_ID
        }

        response = self.client.post("/createLJ",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        lj_id = str(response.json['data']['id'])

        response_2 = self.client.get("/LearningJourney/" + lj_id,
                                    content_type='application/json')
        print("LOOK HERE!")
        print(response_2)
        self.assertEqual(response_2.json, {
                    
            "data": {
                "Completion_Status": "In progress", 
                "Roles_id": 2, 
                "Staff_ID": 140002, 
                "id": 2
            }
                
        })
            
class TestDeleteLearningJourney(TestApp):
    def test_delete_lj(self):
        learningjourney = LearningJourney(Completion_Status="In progress", Roles_id=3 , Staff_ID = 140002)

        db.session.add(learningjourney)
        db.session.commit()

        request_body = {
            'Completion_Status': learningjourney.Completion_Status,
            'Roles_id': learningjourney.Roles_id,
            'Staff_ID': learningjourney.Staff_ID
        }

        response = self.client.post("/createLJ",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        lj_id = str(response.json['data']['id'])

        response_2 = self.client.delete("/deleteLJ/" + lj_id, content_type='application/json') 

        self.assertEqual(response_2.json, {
            
            "Completion_Status": "In progress",
            "Roles_id": 3,
            "Staff_ID": 140002,
            "id": 2
            
                      
        }) 

class TestcreateCourseInLJ(TestApp):
    def test_create_course_LJ(self):
        ljc1 = Learning_Journey_Courses(Course_id="FIN003" ,Skill_id = 3 ,Learning_Journey_Id=1)
        db.session.add(ljc1)
        db.session.commit()

        request_body = {
            'Course_id': ljc1.Course_id,
            'Skill_id': ljc1.Skill_id,
            'Learning_Journey_Id': ljc1.Learning_Journey_Id
        }

        response = self.client.post("/create_LJ_course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        #print(response.json)
        self.assertEqual(response.json, {
            
            "data": 
                {
                    "Course_id": "FIN003",
                    "Learning_Journey_Id": 1,
                    "Skill_id": 3,
                    "id": 2
                }
            ,
            "message": "Successfully Created!"
            
        })
class TestdeleteCoursesLearningJourney(TestApp):
    def test_delete_Course_In_lj(self):
        ljc1 = Learning_Journey_Courses(Course_id="COR006" ,Skill_id = 1 ,Learning_Journey_Id=1)
       
        db.session.add(ljc1)
        db.session.commit()

        request_body = {
            'Course_id': ljc1.Course_id,
            'Skill_id': ljc1.Skill_id,
            'Learning_Journey_Id': ljc1.Learning_Journey_Id    
        }
        

        response = self.client.post("/create_LJ_course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        lj_id = str(response.json['data']['Learning_Journey_Id'])
        skill_id=str(response.json['data']['Skill_id'])
        course_id=str(response.json['data']['Course_id'])

        response_2 = self.client.delete("/delete_LJ_course/" + lj_id + "/" + skill_id+ "/" + course_id, content_type='application/json') 

        self.assertEqual(response_2.json, {
            
           "Course_id": "COR006",
           "Learning_Journey_Id": 1,
           "Skill_id": 1,
           "id": 1
                      
        }) 
    def test_delete_ALL_Courses_In_lj(self):
        ljc1 = Learning_Journey_Courses(Course_id="COR006" ,Skill_id = 1 ,Learning_Journey_Id=1)
        ljc2 = Learning_Journey_Courses(Course_id="FIN003" ,Skill_id = 3 ,Learning_Journey_Id=1)
        db.session.add(ljc1)
        db.session.add(ljc2)
        db.session.commit()

        request_body = {
            'Course_id': ljc1.Course_id,
            'Skill_id': ljc1.Skill_id,
            'Learning_Journey_Id': ljc1.Learning_Journey_Id    
        }
        
        request_body_2 = {
            'Course_id': ljc2.Course_id,
            'Skill_id': ljc2.Skill_id,
            'Learning_Journey_Id': ljc2.Learning_Journey_Id    
        }
        

        response = self.client.post("/create_LJ_course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        response_2 = self.client.post("/create_LJ_course",
                                    data=json.dumps(request_body_2),
                                    content_type='application/json')
        
        
        lj_id = str(response.json['data']['Learning_Journey_Id'])

        response_3 = self.client.delete("/delete_All_LJ_Courses/" + lj_id , content_type='application/json') 

        self.assertEqual(response_3.json, {
            
          "Message":"deleted"
                      
        }) 
  
       
       
class TestGetRole(TestApp):
    def test_get_all_roles(self):
        role_1 = Role(name = 'Project Manager', description = 'A Project Manager manages a team of people.')
        role_2 = Role(name = 'Data Analyst', description = 'A Data Analyst reviews data to identify key insights.')
        role_3 = Role(name = 'Data Scientist', description = 'A Data Scientist analyze data for actionable insights.')
        db.session.add(role_1)
        db.session.add(role_2)
        db.session.add(role_3)
        db.session.commit()

        response = self.client.get("/roles",
                                    content_type='application/json')

        self.assertEqual(response.json, {
            "data": [
                        {
                            'description': 'A Project Manager manages a team of people.',
                            'id': 1,
                            'isDeleted' : 0,
                            'name': 'Project Manager'
                        },
                        {
                            'description': 'A Data Analyst reviews data to identify key insights.',
                            'id': 2,
                            'isDeleted' : 0,
                            'name': 'Data Analyst'
                        },
                        {
                            'description': 'A Data Scientist analyze data for actionable insights.',
                            'id': 3,
                            'isDeleted' : 0,
                            'name': 'Data Scientist'
                        }
                    ]
        })

    def test_get_role_by_id(self):
        role = Role(name = 'Project Manager', description = 'A Project Manager manages a team of people.')

        request_body = {
            'name': role.name,
            'description': role.description,
        }

        response = self.client.post("/roles_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        role_id = str(response.json['data']['id'])

        response_2 = self.client.get("/roles/" + role_id,
                                    content_type='application/json')
        
        self.assertEqual(response_2.json, {
            "data": {
                        'description': 'A Project Manager manages a team of people.',
                        'id': 1,
                        'isDeleted' : 0,
                        'name': 'Project Manager'
                    }         
        })

    def test_reject_invalid_get_role_by_id(self):
        role = Role(name = 'Project Manager', description = 'A Project Manager manages a team of people.')
        db.session.add(role)
        db.session.commit()

        role_id = "99"

        response = self.client.get("/roles/" + role_id,
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Role not found."        
        })

class TestCreateRole(TestApp):
    def test_create_role(self):
        role1 = Role(name='Marketing Director' ,description='A Marketing Director is in charge of managing any given campaign.')

        request_body = {
            'name': role1.name,
            'description': role1.description,
        }
        #print('response body below')
        #print(request_body)

        response = self.client.post("/roles_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        #print('create role response.json below')
        #print(response.json)
        self.assertEqual(response.json, {
            
            "data": {
                'description': 'A Marketing Director is in charge of managing any given campaign.', 
                'id': 1, 
                'isDeleted': 0, 
                'name': 'Marketing Director'
            },
            "message": "Role Created!"
            
        })

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
        db.session.add(role_1)
        db.session.commit()

        request_body_1 = {
            'name': role_1.name,
            'description': role_1.description,
        }

        response1 = self.client.post("/roles_add",
                                    data= json.dumps(request_body_1),
                                    content_type='application/json')

        
        self.assertEqual(response1.json, {
            "message": "Role name already exists. Please enter unique role name."
        })

class TestUpdateRole(TestApp):
    def test_update_role(self):
        #print ("update role")
        existing_role = Role(name = 'Marketing Director', description = 'A Marketing Director is in charge of managing any given campaign.')
        updated_role = Role(name = 'Associate Marketing Director', description = 'An associate Marketing Director is in charge of assisting any given campaign.')

        request_body = {
            'name': existing_role.name,
            'description': existing_role.description
        }

        response = self.client.post("/roles_add",
                            data=json.dumps(request_body),
                            content_type='application/json')

        #print("RESPONSE ID: " + str(response.json['data']['id']))

        role_id = str(response.json['data']['id'])
        role_name = updated_role.name
        role_description = updated_role.description

        response_2 = self.client.put("/roles_update/" + role_id + "/" + role_name + "/" + role_description,
                                content_type='application/json')
        
        self.assertEqual(response_2.json, {
            "message": "Successfully updated!"          
        })

    def test_reject_update_duplicate_role(self):
            role = Role(name = 'Marketing Director', description = 'A Marketing Director is in charge of managing any given campaign.')

            request_body = {
                'name': role.name,
                'description': role.description
            }

            response = self.client.post("/roles_add",
                                data=json.dumps(request_body),
                                content_type='application/json')

            #print('responseid below:')
            #print("RESPONSE ID: " + str(response.json['data']['id']))

            role_id = str(response.json['data']['id'])
            role_name = role.name
            role_description = role.description

            response_2 = self.client.put("/roles_update/" + role_id + "/" + role_name + "/" + role_description,
                                    content_type='application/json')
            
            #print('response_2 below:')
            #print(response_2)
            self.assertEqual(response_2.json, {
                "message": "Role name already exists. Please enter unique role name."        
            })

class TestDeleteRole(TestApp):
    def test_delete_role(self):
        role = Role(name = 'Marketing Director', description = 'A Marketing Director is in charge of managing any given campaign.')

        request_body = {
            'name': role.name,
            'description': role.description
        }

        response = self.client.post("/roles_add",
                            data=json.dumps(request_body),
                            content_type='application/json')

        role_id = str(response.json['data']['id'])

        response_2 = self.client.delete("/role_delete/" + role_id, content_type='application/json') 

        self.assertEqual(response_2.json, {
                'data': {
                    'description': 'A Marketing Director is in charge of managing any given campaign.',
                    'id': 1,
                    'isDeleted': 1,
                    'name': 'Marketing Director'
            },
                'message': "Role successfully deleted."       
        }) 

class TestGetSkill(TestApp):
    def test_get_all_skills(self):
        skill_1 = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
        skill_2 = Skill(name = 'Communication', description = 'Learn to communicate well in a team.')
        skill_3 = Skill(name = 'Project Management', description = 'Learn to manage projects well')
        db.session.add(skill_1)
        db.session.add(skill_2)
        db.session.add(skill_3)
        db.session.commit()

        response = self.client.get("/skills/",
                                    content_type='application/json')

        self.assertEqual(response.json, {
            "data": [
                        {
                            'description': 'The key to successful leadership today is influence, not authority',
                            'id': 1,
                            'isDeleted' : 0,
                            'name': 'Leadership'
                        },
                        {
                            'description': 'Learn to communicate well in a team.',
                            'id': 2,
                            'isDeleted' : 0,
                            'name': 'Communication'
                        },
                        {
                            'description': 'Learn to manage projects well',
                            'id': 3,
                            'isDeleted' : 0,
                            'name': 'Project Management'
                        }
                    ]
        })

    def test_get_skill_by_id(self):
        skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')

        request_body = {
            'name': skill.name,
            'description': skill.description,
        }

        response = self.client.post("/skills_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        skill_id = str(response.json['data']['id'])

        response_2 = self.client.get("/skills/" + skill_id,
                                    content_type='application/json')
        
        self.assertEqual(response_2.json, {
            "data": {
                        'description': 'The key to successful leadership today is influence, not authority',
                        'id': 1,
                        'isDeleted' : 0,
                        'name': 'Leadership'
                    }         
        })

    def test_reject_invalid_get_skill_by_id(self):
        skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')
        db.session.add(skill)
        db.session.commit()

        skill_id = "99"

        response = self.client.get("/skills/" + skill_id,
                                    content_type='application/json')
        
        self.assertEqual(response.json, {
            "message": "Skill not found."        
        })

class TestCreateSkill(TestApp):
    def test_create_skill(self):
        skill = Skill(name = 'Leadership', description = 'The key to successful leadership today is influence, not authority')

        request_body = {
            'name': skill.name,
            'description': skill.description,
        }

        response = self.client.post("/skills_add",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.json, {
            "data": {
                    'description': 'The key to successful leadership today is influence, not authority',
                    'id': 1,
                    'isDeleted' : 0,
                    'name': 'Leadership'
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
    

    #when valid_update is commented out
    #self.client.put just not routing to our app.py update function when skill name is empty

    #when valid_update is NOT commented out
    #self.client.put takes its input rather than the new input
    # def test_reject_update_empty_skill_name(self):
    #     print ("update skill")
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

    #     print("Skill ID: " + skill_id)
    #     print("Skill Name: " + skill_name)
    #     print("Skill Desc: " + skill_description)

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

class TestDeleteSkill(TestApp):
    def test_delete_skill(self):
        skill = Skill(name = 'Communication', description = 'Learn to communicate well in a team.')

        request_body = {
            'name': skill.name,
            'description': skill.description
        }

        response = self.client.post("/skills_add",
                            data=json.dumps(request_body),
                            content_type='application/json')

        print ("Response: " + str(response.json))

        skill_id = str(response.json['data']['id'])
        print("Skill ID: " + skill_id)

        response_2 = self.client.delete("/skill_delete/" + skill_id, content_type='application/json') 

        self.assertEqual(response_2.json, {
                'data': {
                    'description': 'Learn to communicate well in a team.',
                    'id': 1,
                    'isDeleted': 1,
                    'name': 'Communication'
            },
                'message': "Skill successfully deleted."       
        })       



        # "data": {
        #             'description': 'Test Skill Description',
        #             'id': 1,
        #             'isDeleted' : 0,
        #             'name': 'Test Skill Name'
        #     },
        #     "message": "Skill Created!"


if __name__ == '__main__':
    unittest.main()

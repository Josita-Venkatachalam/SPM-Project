import unittest

from app import Skill,Course,Role,Role_Skill,Course_Skill,LearningJourney,Learning_Journey_Courses,Registration
#Unit tests doesn't consider database 
#but for this applcation , it involves validating doctor , adding records to db etc , hence we need integration tests too

class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill(name='Problem Solving',description='Solve the problems well!' )
        self.assertEqual(s1.to_dict(), {
            'id': None,
            'name': 'Problem Solving',
            'description': 'Solve the problems well!',
            'isDeleted' : None
            }
        )

class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(name='Problem Solving',description='Solve the problems well by learning this coruse!', status='Active',type='Internal' ,category='Core')
        self.assertEqual(c1.to_dict(), {
            'id': None,
            'category': 'Core',
            'name': 'Problem Solving',
            'description': 'Solve the problems well by learning this coruse!',
            'status': 'Active',
            'type': 'Internal',
            'category': 'Core'
            }
        )
        
class TestRole(unittest.TestCase):
    def test_to_dict(self):
        r1 = Role(name='Data Sicentist',description='A data scientist turns raw data into valuable insights that an organisation needs in order to grow and compete. They interpret and analyse data from multiple sources to come up with imaginative solutions to problems' )
        self.assertEqual(r1.to_dict(), {
            'id': None,
            'name': 'Data Sicentist',
            'description': 'A data scientist turns raw data into valuable insights that an organisation needs in order to grow and compete. They interpret and analyse data from multiple sources to come up with imaginative solutions to problems',
            'isDeleted' : None
            }
        )

class TestLearningJourney(unittest.TestCase):
    def test_to_dict(self):
        lj1 = LearningJourney(Completion_Status='In Progress',Roles_id=2,Staff_ID=13002 )
        self.assertEqual(lj1.to_dict(), {
            'id': None,
            'Completion_Status': 'In Progress',
            'Roles_id': 2,
            'Staff_ID': 13002}
        )

class TestRole_Skill(unittest.TestCase):
    def test_to_dict(self):
        rs1 =Role_Skill(roles_id=2,skills_id=2 )
        self.assertEqual(rs1.to_dict(), {
            'roles_id': 2,
            'skills_id': 2,
            'id': None}
        )

class TestCourse_Skill(unittest.TestCase):
    def test_to_dict(self):
        rs1 =Course_Skill(Course_id='COR001',Skill_id=2 )
        self.assertEqual(rs1.to_dict(), {
            'Course_id': 'COR001',
            'Skill_id': 2,
            'ID': None,}
        )
        
class TestLearning_Journey_Courses(unittest.TestCase):
    def test_to_dict(self):
        ljc1 = Learning_Journey_Courses(Course_id= 'COR002', Skill_id = 2,Learning_Journey_Id = 1)
        self.assertEqual(ljc1.to_dict(), {
            'id': None,
            'Course_id': 'COR002',
            'Skill_id': 2,
            'Learning_Journey_Id': 1}
        )
class TestRegistration(unittest.TestCase):
    
    def test_to_dict(self):
        r1 = Registration(Reg_ID= 1, Course_ID = 'COR002',Staff_ID = 130001 , Reg_Status = "Registered",Completion_Status= "Completed")
        self.assertEqual(r1.to_dict(), {
            'Reg_ID': 1,
            'Course_ID': 'COR002',
            'Staff_ID': 130001,
            'Reg_Status': "Registered",
            'Completion_Status': "Completed"}
        )

# class TestDoctor(unittest.TestCase):
#     def test_to_dict(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         self.assertEqual(d1.to_dict(), {
#             'hourly_rate': 30,
#             'id': None,
#             'name': 'Imran',
#             'title': 'Dr',
#             'reg_num': 'UKM123'}
#         )

#     def test_minimum_charge(self):
#         d1 = Doctor(name='Joseph', title='Dr',
#                     reg_num='SCIS123', hourly_rate=24)
#         charge = d1.calculate_charges(5)
#         self.assertEqual(d1.hourly_rate, 24)
#         self.assertEqual(charge, 4)

#     def test_higher_charges(self):
#         d1 = Doctor(name='Chris', title='Dr',
#                     reg_num='SCIS88', hourly_rate=18)
#         charge = d1.calculate_charges(40)
#         self.assertEqual(d1.hourly_rate, 18)
#         self.assertEqual(charge, 12)


# class TestPatient(unittest.TestCase):
#     def test_to_dict(self):
#         p1 = Patient(name='Kankan', title='Lord',
#                      contact_num='+65 8888 8888', ewallet_balance=88)
#         self.assertEqual(p1.to_dict(), {
#             'id': None,
#             'name': 'Kankan',
#             'title': 'Lord',
#             'contact_num': '+65 8888 8888',
#             'ewallet_balance': 88}
#         )

#     def test_ewallet_topup(self):
#         p1 = Patient(name='Bob', title='Mr',
#                      contact_num='+65 1234 5678', ewallet_balance=8)
#         self.assertEqual(p1.ewallet_balance, 8)
#         p1.ewallet_topup(88)
#         self.assertEqual(p1.ewallet_balance, 96)

#     def test_ewallet_topup_negative(self):
#         p1 = Patient(name='Elise', title='Ms',
#                      contact_num='+65 1234 5678', ewallet_balance=8)
#         self.assertEqual(p1.ewallet_balance, 8)
#         try:
#             p1.ewallet_topup(-88)
#         except Exception as e:
#             self.assertEqual(str(e), 'Negative topups not allowed.')
#             self.assertEqual(p1.ewallet_balance, 8)

#     def test_ewallet_withdraw(self):
#         p1 = Patient(name='Elise', title='Ms',
#                      contact_num='+65 1234 5678', ewallet_balance=88)
#         self.assertEqual(p1.ewallet_balance, 88)
#         p1.ewallet_withdraw(8)
#         self.assertEqual(p1.ewallet_balance, 80)

#     def test_ewallet_withdraw_empty(self):
#         p1 = Patient(name='Elise', title='Ms',
#                      contact_num='+65 1234 5678', ewallet_balance=88)
#         self.assertEqual(p1.ewallet_balance, 88)
#         p1.ewallet_withdraw(88)
#         self.assertEqual(p1.ewallet_balance, 0)

#     def test_ewallet_withdraw_fail(self):
#         p1 = Patient(name='Elise', title='Ms',
#                      contact_num='+65 1234 5678', ewallet_balance=88)
#         self.assertEqual(p1.ewallet_balance, 88)
#         try:
#             p1.ewallet_withdraw(888)
#         except Exception as e:
#             self.assertEqual(str(e),
#                              'Unable to withdraw: insufficient balance.')
#             self.assertEqual(p1.ewallet_balance, 88)


# class TestConsultation(unittest.TestCase):
#     def test_to_dict(self):
#         c1 = Consultation(diagnosis='Nosebleed',
#                           prescription='Tissue paper for nose',
#                           charge=55, doctor_id=8, patient_id=9)
#         self.assertEqual(c1.to_dict(), {
#             'id': None,
#             'diagnosis': 'Nosebleed',
#             'prescription': 'Tissue paper for nose',
#             'charge': 55,
#             'doctor_id': 8,
#             'patient_id': 9
#             }
#         )


if __name__ == "__main__":
    unittest.main()

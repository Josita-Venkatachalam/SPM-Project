import unittest

from app import app, db, Skill,Course,Role,Role_Skill,Course_Skill,LearningJourney,Learning_Journey_Courses,registration
#Unit tests doesn't consider database 
#but for this applcation , it involves validating doctor , adding records to db etc , hence we need integration tests too

class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill(name='Problem Solving',description='Solve the problems well!' )
        self.assertEqual(s1.to_dict(), {
            'id': None,
            'name': 'Problem Solving',
            'description': 'Solve the problems well!'}
        )

class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(name='Problem Solving',description='Solve the problems well by learning this coruse!', status='Active',type='Internal' ,category='Core')
        self.assertEqual(c1.to_dict(), {
            'id': None,
            'name': 'Problem Solving',
            'description': 'Solve the problems well by learning this coruse!',
            'status': 'Active',
            'type': 'Internal'
            }
        )
        
class TestRole(unittest.TestCase):
    def test_to_dict(self):
        r1 = Role(name='Data Sicentist',description='A data scientist turns raw data into valuable insights that an organisation needs in order to grow and compete. They interpret and analyse data from multiple sources to come up with imaginative solutions to problems' )
        self.assertEqual(r1.to_dict(), {
            'id': None,
            'name': 'Data Sicentist',
            'description': 'A data scientist turns raw data into valuable insights that an organisation needs in order to grow and compete. They interpret and analyse data from multiple sources to come up with imaginative solutions to problems'}
        )

class TestLearningJourney(unittest.TestCase):
    def test_to_dict(self):
        lj1 = LearningJourney(Compeletion_Status='In Progress',Role_id=2,Staff_ID=13002 )
        self.assertEqual(lj1.to_dict(), {
            'id': None,
            'Compeletion_Status': 'In Progress',
            'Role_id': 2,
            'Staff_ID': 13002}
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

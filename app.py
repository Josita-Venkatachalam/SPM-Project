# from crypt import methods
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root' + \
                                        '@localhost:3306/spmProj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Skill(db.Model):
    __tablename__ = 'skill'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    isDeleted = db.Column(db.Integer)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    status = db.Column(db.String(50))
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
        
class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    isDeleted = db.Column(db.Integer)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Role_Skill(db.Model):
    __tablename__ = 'roles_skills'

    roles_id = db.Column(db.Integer)
    skills_id = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key = True)

    
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Course_Skill(db.Model):
    __tablename__ = 'courses_skills'

    Course_id = db.Column(db.String(50))
    Skill_id = db.Column(db.Integer)
    ID = db.Column(db.Integer, primary_key = True)
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class LearningJourney(db.Model):
    __tablename__ = 'LearningJourney'

    id = db.Column(db.Integer, primary_key = True)
    Completion_Status = db.Column(db.String(100))
    Roles_id = db.Column(db.Integer)
    Staff_ID = db.Column(db.Integer)
    
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
class Learning_Journey_Courses(db.Model):
    __tablename__ = 'learning_journey_courses'

    id = db.Column(db.Integer, primary_key = True)
    Course_id = db.Column(db.String(50))
    Skill_id = db.Column(db.Integer)
    Learning_Journey_Id = db.Column(db.Integer)
    
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
class Registration(db.Model):
     __tablename__ = 'registration'
     
     Reg_ID =db.Column(db.Integer, primary_key = True)
     Course_ID = db.Column(db.String(6))
     Staff_ID = db.Column(db.Integer)
     Reg_Status = db.Column(db.String(10))
     Completion_Status = db.Column(db.String(9))
     
     def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
     

with app.app_context():
    db.create_all()


    @app.route("/skills/<int:skill_id>")
    def skill_by_id(skill_id):
        skill = Skill.query.filter_by(id=skill_id).first()
        if skill:
            return jsonify({
                "data": skill.to_dict()
            }), 200
        else:
            return jsonify({
                "message": "Skill not found."
            }), 404


    @app.route("/skills_add", methods=['POST'])
    def create_skill():
        data = request.get_json()
        #check if skill alr exist in the DB , if yes don't allow it to add and display error ( name)
        if not all(key in data.keys() for
                key in ('name',
                        'description')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
        skill = Skill(**data)
        
        print(skill)
        print(data)
        skill_name = data["name"].lower()
        skill_description = data["description"].lower()
        
        try:
            db.session.add(skill)
            db.session.commit()
            return jsonify({"data": skill.to_dict()}), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/skill_delete/<int:skill_id>", methods=['DELETE'])
    def delete_skill(skill_id):
    
        skill = Skill.query.filter_by(id=skill_id).first()
        try:
            skill.isDeleted = 1
            db.session.commit()
            return jsonify(skill.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
    @app.route("/skills_update/<string:id>/<string:name>/<string:description>", methods=['PUT'])
    def update_skill(id, name ,description):
            # name = request.args.get('name')
            # description = request.args.get('description')
            # skill_id = request.args.get('id')
            print(name)
            print(id)
            skill = Skill.query.filter_by(id=int(id)).first()
            # data=request.get_json()
            
            print(skill)
            
            skill.name = name
            skill.description = description
            db.session.commit()
            #retrive the data from the request to update the data in the database
            return jsonify(
                {
                    "code":200,
                    # "data":skill

                }  
                
            )



    @app.route("/skills/")
    def skills():
        # search_name = request.args.get('skill')
        # print(searchname)
        # if searchname:
        #     # skills_list = Skill.query.filter(Skill.name.contains(search_name))
        #     skill = Skill.query.filter_by(name=searchname).first()
        #     print(skill.to_dict())
        #     return jsonify({
        #         "data": skill.to_dict()
        #     }), 200
            
        # else:
        skills_list = Skill.query.filter_by(isDeleted=0).all()
        return jsonify(
            {
                "data": [skill.to_dict() for skill in skills_list]
            }
        ), 200



    @app.route("/roles/<int:role_id>")
    def role_by_id(role_id):
        role = Role.query.filter_by(id=role_id).first()
        if role:
            return jsonify({
                "data": role.to_dict()
            }), 200
        else:
            return jsonify({
                "message": "Role not found."
            }), 404


    @app.route("/roles_add", methods=['POST'])
    def create_role():
        data = request.get_json()
        #Validate if name and description input is filled , if not display error msg
        #check if role alr exist in the DB , if yes don't allow it to add and display error ( name)
        if not all(key in data.keys() for
                key in ('name',
                        'description')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
        role = Role(**data)
        
        print(data)
        role_name = data["name"].lower()
        role_description = data["description"].lower()
        
        try:
            db.session.add(role)
            db.session.commit()
            return jsonify(role.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/role_delete/<int:role_id>", methods=['DELETE'])
    def delete_role(role_id):
    
        role = Role.query.filter_by(id=role_id).first()
        try:
            role.isDeleted = 1
            db.session.commit()
            return jsonify(role.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/roles_update/<string:id>/<string:name>/<string:description>", methods=['PUT'])
    def update_role(id, name ,description):
            # name = request.args.get('name')
            # description = request.args.get('description')
            # role_id = request.args.get('id')
            print(name)
            print(id)
            role = Role.query.filter_by(id=int(id)).first()
            # data=request.get_json()
            
            print(role)
            
            role.name = name
            role.description = description
            db.session.commit()
            #retrive the data from the request to update the data in the database
            return jsonify(
                {
                    "code":200,
                    # "data":role

                }  
                
            )

    @app.route("/roles")
    def roles():
        search_name = request.args.get('role')
        if search_name:
            roles_list = Role.query.filter(Role.name.contains(search_name))
        else:
            roles_list = Role.query.filter_by(isDeleted=0).all()
        return jsonify(
            {
                "data": [role.to_dict() for role in roles_list]
            }
        ), 200
        # roles_list = Role.query.all()
        # return jsonify(
        #     {
        #         "data": [role.to_dict()
        #                  for role in roles_list]
        #     }
        # ), 200
    @app.route("/roles/<int:role_id>")
    def get_role_by_id(role_id):
        role = Role.query.filter(Role.id == role_id).first()
    
        if role:
            return jsonify(
            {
                "data": role.to_dict()
            }
        ), 200
        else:
            return jsonify({
                "message": "Role not found."
            }), 404


    
        

    @app.route("/skillsearch/<string:searchname>")
    def search_skill(searchname):
        # search_name = request.args.get('skill')
        print(searchname)
        skill = Skill.query.filter_by(name=searchname).first()
        if skill:
            # skills_list = Skill.query.filter(Skill.name.contains(search_name))
            
            print(skill.to_dict())
            return jsonify({
                "data": [skill.to_dict()]
            }), 200
            
        else:
            # skills_list = Skill.query.all()
            skills_list = []
            return jsonify(
                {
                    "data": []
                }
            ), 500
        

    @app.route("/roles_skills/<int:RoleID>")
    def get_skills():
        search_role = request.args.get('RoleID')
        if search_role != '':
            skill_list = Role_Skill.query.filter(Role_Skill.roleID == search_role) 
        else:
            skill_list = Role_Skill.query.all()
            skillIDs = [skill.to_dict() for skill in skill_list]
            result = Skill.query.filter(Skill.id.in_(skillIDs))
            jsonify(
                {
                    "data": [skill.to_dict() for skill in result]
                }
            ), 200
    @app.route("/roles_skills_LJ/<int:RoleID>")
    def get_skills_for_chosenLJ(RoleID):
        
        skill_list = Role_Skill.query.filter(Role_Skill.roles_id == RoleID) 
        if skill_list:
            return jsonify(
                {
                    "data": [skill.to_dict() for skill in skill_list]
                }
            ), 200
        else:
            return jsonify({
                "message": "cant retrieve skills for chosen LJ"
            }), 404

    @app.route("/courses/")
    def courses():
        # search_name = request.args.get('skill')
        # print(searchname)
        # if searchname:
        #     # skills_list = Skill.query.filter(Skill.name.contains(search_name))
        #     skill = Skill.query.filter_by(name=searchname).first()
        #     print(skill.to_dict())
        #     return jsonify({
        #         "data": skill.to_dict()
        #     }), 200
            
        # else:
        courses_list = Course.query.all()
        return jsonify(
            {
                "data": [course.to_dict() for course in courses_list]
            }
        ), 200

    @app.route("/assignskilltocourse/", methods = ['POST'])
    def assignskilltocourse():
        print('im in assign course')
        data = request.get_json()
        print(data)
        course_skill = Course_Skill(**data)

        try:
            db.session.add(course_skill)
            db.session.commit()
            return jsonify({"message":"added successfully"}), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/deassignskilltocourse/<string:course_id>/<int:skill_id>", methods = ['DELETE'])
    def deassignskilltocourse(course_id, skill_id):
        print('im in deassign')
        course_skill = Course_Skill.query.filter_by(Course_id = course_id , Skill_id = skill_id).first()

        try:
            db.session.delete(course_skill)
            db.session.commit()
            return jsonify({"message":"deleted successfully"}), 201
        except Exception:
            return jsonify({
                "message": "Unable to delete from database."
            }), 500

    @app.route("/skillsofcourse/<string:course_id>")
    def skills_of_course(course_id):
        print("im in getting alr assigned skills")
        print(course_id)
        records = Course_Skill.query.filter(Course_Skill.Course_id == course_id)
        print(records)
        if records:
            return jsonify({
                "data": [record.to_dict() for record in records]
            }), 200
        else:
            return jsonify({
                "message": "cant retrieve records"
            }), 404

    @app.route("/assignskilltorole/", methods = ['POST'])
    def assignskilltorole():
        print('im in assign role')
        data = request.get_json()
        print(data)
        role_skill = Role_Skill(**data)

        try:
            db.session.add(role_skill)
            db.session.commit()
            return jsonify({"message":"added successfully"}), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/deassignskilltorole/<string:role_id>/<int:skill_id>", methods = ['DELETE'])
    def deassignskilltorole(role_id, skill_id):
        print('im in deassign')
        role_skill = Role_Skill.query.filter_by(Roles_id = role_id , Skills_id = skill_id).first()

        try:
            db.session.delete(role_skill)
            db.session.commit()
            return jsonify({"message":"deleted successfully"}), 201
        except Exception:
            return jsonify({
                "message": "Unable to delete from database."
            }), 500

    @app.route("/skillsofrole/<string:role_id>")
    def skills_of_role(role_id):
        print("im in getting alr assigned skills")
        print(role_id)
        records = Role_Skill.query.filter(Role_Skill.Roles_id == role_id)
        print(records)
        if records:
            return jsonify({
                "data": [record.to_dict() for record in records]
            }), 200
        else:
            return jsonify({
                "message": "cant retrieve records"
            }), 404

    @app.route("/rolesskills/<int:rolesid>")
    def get_roleskill(rolesid):
        # roleskill_list = Role_Skill.query.filter_by(roles_id = rolesid)

        subquery = (
            db.session.query(Role_Skill.skills_id)
            .filter(Role_Skill.roles_id == rolesid)
        )

        result = (
            db.session.query(Skill)
            .filter(Skill.id.in_(subquery))
            .all()
        )

        if result:
            return jsonify(
                {
                    "data": [item.to_dict() for item in result]
                }
            ), 200
        else:
            return jsonify({
                "message": "Role not found."
            }), 404

    @app.route("/skillcourses/<int:skillsid>")
    def get_courseskill(skillsid):
        # roleskill_list = Role_Skill.query.filter_by(roles_id = rolesid)
        print(skillsid)
        subquery = (
            db.session.query(Course_Skill.Course_id)
            .filter(Course_Skill.Skill_id == skillsid)
        )

        result = (
            db.session.query(Course)
            .filter(Course.id.in_(subquery))
            .all()
        )

        if result:
            return jsonify(
                {
                    "data": [item.to_dict() for item in result]
                }
            ), 200
        else:
            return jsonify({
                "message": "Skill not found."
            }), 404

    @app.route("/LearningJourney/<int:LearningJourneyID>")
    def get_LJ_by_Id(LearningJourneyID):
        lj = LearningJourney.query.filter(LearningJourney.id == LearningJourneyID).first()
    
        if lj:
            return jsonify(
            {
                "data": lj.to_dict()
            }
        ), 200
        else:
            return jsonify({
                "message": "Learning Journey not found."
            }), 404


    @app.route("/LearningJourney/")
    def getLJ():
        learning_journeys= LearningJourney.query.filter_by(Staff_ID = 130001)
        print(learning_journeys)
        if learning_journeys:
            return jsonify(
            {
                "data": [lj.to_dict() for lj in learning_journeys]
            }), 200
        else:
            return jsonify({
                "message": "LJ not found."
            }), 404
            
    @app.route("/createLJ", methods=['POST'])
    def create_LJ():
        data = request.get_json()
        #check if skill alr exist in the DB , if yes don't allow it to add and display error ( name)
        print("Hi I am inside")
        if not all(key in data.keys() for
                key in ('Completion_Status','Roles_id',
                        'Staff_ID')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
        
        LJ = LearningJourney(**data)
    
        
        print(LJ)
        try:
            db.session.add(LJ)
            db.session.commit()
            #print(LJ.to_dict())
            return jsonify(
                {
                    "data": LJ.to_dict(),
                    "message": "Learning Journey Created!"
            }), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

    @app.route("/deleteLJ/<int:LJ_ID>", methods=['DELETE'])
    def delete_LJ(LJ_ID):
    
        LJ = LearningJourney.query.filter_by(id=LJ_ID).first()
        try:
            db.session.delete(LJ)
            db.session.commit()
            return jsonify(LJ.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
    @app.route("/delete_All_LJ_Courses/<int:LJ_ID>", methods=['DELETE'])
    def delete_All_LJ_Courses(LJ_ID):
    

        # LJ_query= Learning_Journey_Courses.query.filter()
        # print(LJ_query)
        delete_q = Learning_Journey_Courses.__table__.delete().where(Learning_Journey_Courses.Learning_Journey_Id == LJ_ID)
        try:
            db.session.execute(delete_q)
            db.session.commit()
            return jsonify({"Message":"deleted"}), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500


        # try:
        #     db.session.delete(LJ_query)
        #     db.session.commit()
        #     return jsonify(LJ.to_dict()), 201
        # except Exception:
        #     return jsonify({
        #         "message": "Unable to commit to database."
        #     }), 500
        
    @app.route("/create_LJ_course", methods=['POST'])
    def create_LJ_course():
        print("Hi I am inside create lj course")
        data = request.get_json()
        #check if skill alr exist in the DB , if yes don't allow it to add and display error ( name)
        
        if not all(key in data.keys() for
                key in ('Course_id','Skill_id',
                        'Learning_Journey_Id')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
        
        LJ_Course = Learning_Journey_Courses(**data)
    
        
        print(LJ_Course)
        try:
            db.session.add(LJ_Course)
            db.session.commit()
            print(LJ_Course.to_dict())
            return jsonify(
                {
                    "data": [LJ_Course.to_dict()],
                    "message": "Hi there!"
            }), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
    @app.route("/delete_LJ_course/<int:LJ_ID>/<int:Skill_ID>/<string:Course_ID>", methods=['DELETE'])
    def delete_LJ_course(LJ_ID, Skill_ID, Course_ID):
    
        LJ = Learning_Journey_Courses.query.filter_by(Learning_Journey_Id = LJ_ID, Course_id = Course_ID, Skill_id = Skill_ID ).first()
        print(LJ)
        try:
            db.session.delete(LJ)
            db.session.commit()
            return jsonify(LJ.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
            
    @app.route("/get_skills_LJ/<int:LearningJourneyID>")
    def get_skills_by_Id(LearningJourneyID):
        lj = Learning_Journey_Courses.query.filter(Learning_Journey_Courses.Learning_Journey_Id == LearningJourneyID)
        if lj:
            return jsonify(
                {
                    "data": [ljs.to_dict() for ljs in lj]
                }
            ), 200
        else:
            return jsonify({
            "message": "Role not found."
            }), 404
            
        # @app.route("/roles_add", methods=['POST'])
        # def create_role():
        #     data = request.get_json()
        #     #Validate if name and description input is filled , if not display error msg
        #     #check if role alr exist in the DB , if yes don't allow it to add and display error ( name)
        #     if not all(key in data.keys() for
        #                key in ('name',
        #                        'description')):
        #         return jsonify({
        #             "message": "Incorrect JSON object provided."
        #         }), 500
        #     role = Role(**data)
            
        #     print(data)
        #     role_name = data["name"].lower()
        #     role_description = data["description"].lower()
            
        #     try:
        #         db.session.add(role)
        #         db.session.commit()
        #         return jsonify(role.to_dict()), 201
        #     except Exception:
        #         return jsonify({
        #             "message": "Unable to commit to database."
        #         }), 500
    @app.route("/get_courses_skill_LJ/<int:LearningJourneyID>/<int:SkillID>/")
    def get_courses_skill_LJ(LearningJourneyID,SkillID):
        records = Learning_Journey_Courses.query.filter(Learning_Journey_Courses.Learning_Journey_Id == LearningJourneyID, Learning_Journey_Courses.Skill_id == SkillID)
        if records:
            return jsonify(
                {
                    "data": [record.to_dict() for record in records]
                }
            ), 200
        else:
            return jsonify({
            "message": "chosen courses not found."
            }), 404
    @app.route("/get_roleid_LJ/<int:LearningJourneyID>")
    def get_roleid_LJ(LearningJourneyID):
        print(LearningJourneyID)
        record = LearningJourney.query.filter(LearningJourney.id == LearningJourneyID).first()
        print(record)
        if record:
            return jsonify(
                {
                    "data": [record.to_dict()]
                }
            ), 200
        else:
                return jsonify({
                "message": "Role not found."
                }), 404

    @app.route("/get_completed_courses/<string:staffID>")
    def get_completed_courses(staffID):
        print(staffID)
        records = Registration.query.filter(Registration.Staff_ID == staffID, Registration.Completion_Status == "Completed")
        print(records)
        if records:
            return jsonify(
                {
                     "data": [record.to_dict() for record in records]
                }
            ), 200
        else:
                return jsonify({
                "message": "CANT retrieve completed courses from registration table."
                }), 404
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

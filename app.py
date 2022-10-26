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

class LearningJourney(db.Model):
    __tablename__ = 'LearningJourney'

    id = db.Column(db.Integer, primary_key = True)
    Completion_status = db.Column(db.String(45))
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
        return jsonify(skill.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/skill_delete/<int:skill_id>", methods=['DELETE'])
def delete_skill(skill_id):
   
    skill = Skill.query.filter_by(id=skill_id).first()
    try:
        db.session.delete(skill)
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
    skills_list = Skill.query.all()
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
        db.session.delete(role)
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
        roles_list = Role.query.all()
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
    print('im in assign')
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
def LJ_by_id(LearningJourneyID):
    LJ = LearningJourney.query.filter_by(id=LearningJourneyID).first()
    if LJ:
        return jsonify({
            "data": LJ.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Role not found."
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

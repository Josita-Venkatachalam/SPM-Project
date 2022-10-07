from token import DOUBLESLASH
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root' + \
                                        '@localhost:3306/spmProj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


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

class Role(db.Model):
    __tablename__ = 'roles'

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

    roleID = db.Column(db.Integer, primary_key=True)
    SkillID = db.Column(db.Integer, primary_key=True)


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
    #Validate if name and description input is filled , if not display error msg
    #check if skill alr exist in the DB , if yes don't allow it to add and display error ( name)
    if not all(key in data.keys() for
               key in ('name',
                       'description')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    skill = Skill(**data)
    
    print(data)
    skill_name = data["name"].lowercase()
    skill_description = data["description"].lowercase()
    
    try:
        db.session.add(skill)
        db.session.commit()
        return jsonify(skill.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500



@app.route("/skills")
def skills():
    search_name = request.args.get('skill')
    if search_name:
        skills_list = Skill.query.filter(Skill.name.contains(search_name))
    else:
        skills_list = Skill.query.all()
    return jsonify(
        {
            "data": [skill.to_dict() for skill in skills_list]
        }
    ), 200
    # skills_list = Skill.query.all()
    # return jsonify(
    #     {
    #         "data": [skill.to_dict()
    #                  for skill in skills_list]
    #     }
    # ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route("/roles/<int:RoleID>")
def searchRole():
    search_name = request.args.get('RoleID')
    if search_name:
        role_list = Skill.query(Role.id).filter(Role.id.contains(search_name))
        return jsonify(
        {
            "data": [role.to_dict() for role in role_list]
        }
    ), 200



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




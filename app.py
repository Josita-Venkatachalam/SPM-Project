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
    role_name = data["name"].lowercase()
    role_description = data["description"].lowercase()
    
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

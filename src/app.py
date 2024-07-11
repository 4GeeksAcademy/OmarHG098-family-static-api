"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member(
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Jackson",
        "age": "33",
        "lucky_numbers": [7, 13, 2]
    }
)
jackson_family.add_member(
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": "35",
        "lucky_numbers": [10, 14, 3]
    }
)
jackson_family.add_member(
    {
        "id": 3,
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": "5",
        "lucky_numbers": [1]
    }
)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member/<int:id>', methods = ['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    else:
        return jsonify(member), 200

@app.route('/member/<int:id>', methods = ['DELETE'])
def delete_member(id):
    #member = jackson_family.get_member(id)
    
    success = jackson_family.delete_member(id)
    # if member is None:
    #     return jsonify({"error": "Member not found"}), 404
    # else: 

    if success != "Member not found":
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404
    
"""
DELETE USER
"""    

@app.route('/member', methods = ['POST'])
def add_member():
    request_body = request.get_json(force=True)
    jackson_family.add_member(request_body)
    members = jackson_family.get_all_members()
    return jsonify(members), 200



    # body = request.get_json(force = True)
    # new_member = {
    #     {
    #         "age": body.get("age", None),
    #         "first_name": body.get("first_name", None),
    #         "lucky_numbers": body.get("lucky_numbers", None)
    #     }
    # }
    # jackson_family.add_member(new_member)
    # members = jackson_family.get_all_members()
    # return jsonify(members), 200
    

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()



    return jsonify(members), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

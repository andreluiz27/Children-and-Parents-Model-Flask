import json
from flask import Response, flash, redirect, request
from .models import Child


from main import app, db


@app.route('/api/children')
def list_children():
    children = Child.query.all()
    
    if not children:
        return json.dumps({"message":"no children in the database"})


    for child in children:
        json_response = json.dumps({
                                  'id': child.id,
                                  'name': child.name
                        })
    
    response = Response(json_response, content_type='application/json; charset=utf-8')
    response.status_code = 200
    return response

@app.route('/api/child/<id>', methods=['GET', 'POST'])
def retrieve_child(id):
    this_child = Child.query.filter_by(id=id)

    if this_child.parent1_id:
        parent1 = this_child.parent1_id
    else:
        parent1 = None

    if this_child.parent2_id:
        parent2 = this_child.parent2_id
    else:
        parent2 = None         

    response_as_dict = {
        "id": this_child.id,
        "name": this_child.name,
        "parents": [
            {"id": parent1, "name": this_child.name},
            {"id": parent2,"name": this_child.name}
        ]

    }
    
    response = Response(json.dumps(response_as_dict), content_type='application/json; charset=utf-8')
    response.status_code = 200
    return response_as_dict


@app.route('/api/child/delete/<id>', methods=['GET'])
def delete_child(id):
   # deleting from database     
    child_to_be_deleted = Child.query.filter_by(id=id)
    child_to_be_delete.delete()
    db.session.commit()
    return redirect(url_for('home'))

















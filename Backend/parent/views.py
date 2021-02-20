import json

from flask import Response, redirect

# make a analog
from main import app, bcrypt, db


@app.route('/api/parents')
@login_required
def list_parents():
    parents = Parents.query.all()
    
    if not parents:
        return json.dumps({"message":"no parents in the database"})

    parents_list = []
    for parent in parents:
        children_list =[{"id":child.id, "name": child.name} for child in parent.child.all()]
        response_as_list = parents_list.append(json.dumps({
                                  'id': parent.id,
                                  'name': parent.name
                                  'children': children_list
                        }))
    
    response = Response(response_as_list, content_type='application/json; charset=utf-8')
    response.status_code = 200
    return response

@login_required
@app.route('/api/parent/<id>', methods=['GET', 'POST'])
def retrieve_parent(id):
    this_parent = Parent.query.filter_by(id=id)

    children_list = []
    for child in this_parent.child.all():
        children_list.append({
            "id": child.id,
            "name": child.name
        })
        
    response_as_dict = {
        "id": this_parent.id,
        "name": this_parent.name,
        "children": children_list
    }

    response = Response(json.dumps(response_as_dict), content_type='application/json; charset=utf-8')
    response.status_code = 200
    return response


@app.route('/api/delete/parent', methods=['GET'])
def delete_parent(source, audio_owner_id, audio_id):
   # deleting from database
    parent_to_be_deleted = Parent.query.filter_by(id=id)
    parent_to_be_delete.delete()
    db.session.commit()

    return redirect(url_for('home'))

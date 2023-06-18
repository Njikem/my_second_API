from flask import Flask,request
import dbhelpers
import json

app = Flask(__name__)

#item get request
@app.get("/api/item")
def get_item():
    id = request.json.get("id")
    name = request.json.get("name")
    description = request.json.get("description")
    price = request.json.get("price")
    created_at = request.json.get("created_at")
    results = dbhelpers.run_procedure('call items(?,?,?,?,?)', [id, name, description, price, created_at])
    results_json = json.dumps(results, default=str)
    return results_json

#item post request
@app.post("/api/item")
def post_item():
    name = request.json.get("name")
    description = request.json.get("description")
    quantity = request.json.get("quantity")
    results = dbhelpers.run_procedure('call insert_three_items(?,?,?)', [name, description, quantity])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry,something went wrong"
    
#item patch request
@app.patch("/api/item")
def patch_item():
    id = request.json.get("id")
    price = request.json.get("price")
    results = dbhelpers.run_procedure('call get_two_item(?,?)', [id, price] )
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry,something went wrong"

#item delete request
@app.delete("/app/item")
def delete_item():
    id = request.json.get("id")
    results = dbhelpers.run_procedure('call get_one_item(?)', [id])
    return json.dumps(results, default=str)





    
#employee get request
@app.get("/api/employee")
def get_employee():
    name = request.json.get("name")
    position = request.json.get("position")
    hired_at = request.json.get("hired_at")
    hourly_wage = request.json.get("hourly_wage")
    results = dbhelpers.run_procedure('call get_one_employee(?,?,?,?)', [name, position, hired_at, hourly_wage])
    results_json = json.dumps(results, default=str)
    return results_json

#employee post request
@app.post("/api/employee")
def post_employee():
    name = request.json.get("name")
    position = request.json.get("position")
    hourly_wage = request.json.get("hourly_wage")
    results = dbhelpers.run_procedure('call get_three_employee(?,?,?)', [name, position, hourly_wage])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry,something went wrong"
    
#employee patch request
@app.patch("/api/employee")
def patch_employee():
    id = request.json.get("id")
    hourly_wage = request.json.get("hourly_wage")
    results = dbhelpers.run_procedure('call get_two_employee(?,?)', [id, hourly_wage] )
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry,something went wrong"

#employee delete request
@app.delete("/app/employee")
def delete_employee():
    id = request.json.get("id")
    results = dbhelpers.run_procedure('call get_one_employee1(?)', [id])
    return json.dumps(results, default=str)






app.run(debug=True)
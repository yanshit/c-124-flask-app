from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'kajal',
        'Contact': u'9937041890', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'yanshit',
        'Contact': u'9937541156', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello there "

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please give the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
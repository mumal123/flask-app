from flask import Flask,jsonify,request

app= Flask(__name__)

contacts = [
    {
        'id':1,
        'Name':u'Chirag',
        'Contact':u'0215487965',
        'done':False,
    
    },
    {
        'id':1,
        'Name':u'Mumal',
        'Contact':u'8795348',
        'done':False,
    }
]

@app.route('/add-data',methods = ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
        
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
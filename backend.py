from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import geopy.distance

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("geo-todo-first-draft-firebase-adminsdk-bh7v3-2b513e522d.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

tasks_collection = db.collection('tasks')

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    task = {
        'title': data['title'],
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'is_done': False
    }
    tasks_collection.add(task)
    return jsonify({'message': 'Task added successfully'}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = [task.to_dict() for task in tasks_collection.stream()]
    return jsonify(tasks), 200

@app.route('/nearby_tasks', methods=['POST'])
def nearby_tasks():
    data = request.json
    user_location = (data['latitude'], data['longitude'])
    radius = data.get('radius', 0.5)  # Default radius is 0.1 km

    nearby_tasks_list = []
    for task in tasks_collection.stream():
        task_data = task.to_dict()
        task_location = (task_data['latitude'], task_data['longitude'])
        distance = geopy.distance.distance(user_location, task_location).km
        if distance <= radius:
            nearby_tasks_list.append(task_data)

    return jsonify(nearby_tasks_list), 200

if __name__ == '__main__':
    app.run(debug=True)

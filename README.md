# To-Do List with Location

This project is a simple to-do list application with a feature that allows users to assign a geographic location to each task. It uses Python (Flask) for the backend and a JavaScript web frontend with OpenStreetMap for location integration.

## Features
- Create tasks with a title and geographic location.
- Store tasks in Firebase Firestore.
- Display tasks on a map and manage them through a web interface.
- Find nearby tasks based on your current location.

## Technologies Used
- **Backend**: Python, Flask, Firebase Firestore, Geopy, Flask-CORS
- **Frontend**: HTML, JavaScript, Leaflet.js (OpenStreetMap integration)

## Setup Instructions

### Backend Setup
1. Install dependencies:
   ```sh
   pip install Flask firebase-admin geopy flask-cors
   ```
2. Initialize Firebase by downloading the credentials JSON file and updating the path in the script.
3. Run the backend:
   ```sh
   python app.py
   ```

### Frontend Setup
1. Save the HTML code in a file named `index.html`.
2. Serve the HTML file using a simple HTTP server (e.g., Python's built-in server):
   ```sh
   python3 -m http.server 8000
   ```
3. Open a browser and navigate to `http://localhost:8000/index.html`.

## Usage
- Click on the map to select a location for the task.
- Enter a task title and click "Add Task" to store it.
- The backend will store the task in Firestore and you will be notified of successful creation.

## License
This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

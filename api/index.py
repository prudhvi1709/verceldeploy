import json
from http.server import BaseHTTPRequestHandler

# Function to load marks from the JSON file
def load_marks():
    with open('q-vercel-python.json', 'r') as file:
        return json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.end_headers()

        # Parse the query parameters
        query_params = self.path.split('?')[1]
        names = query_params.split('&')
        student_names = [name.split('=')[1] for name in names]

        # Load student marks from the JSON file
        student_marks = load_marks()

        # Fetch marks for the requested students
        marks = [student_marks.get(name, 'Student not found') for name in student_names]

        # Return the JSON response
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

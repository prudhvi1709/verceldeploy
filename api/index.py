import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Load student marks from a JSON file
def load_student_marks():
    with open('q-vercel-python.json', 'r') as file:
        return json.load(file)

STUDENT_MARKS = load_student_marks()  # Load marks dynamically from the JSON file

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # Allow specific methods
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow specific headers
        self.end_headers()

        try:
            # Parse the URL and query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            # Get student names from the 'name' parameter
            student_names = query_params.get('name', [])

            if not student_names:
                # If no names provided, return an empty marks array
                response = {"marks": []}
            else:
                # Fetch marks for the requested students
                # Returns "Student not found" for unknown students
                marks = [STUDENT_MARKS.get(name, "Student not found") for name in student_names]
                response = {"marks": marks}

            # Return the JSON response
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except Exception as e:
            # Handle any errors
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Hardcode the student marks data
STUDENT_MARKS = {
    "u": 5,
    "uEq4XSDq2p": 9,
    "pyHLbdLvxn": 19,
    "dAD7K": 15,
    "mRXOtnM8": 42
    # Add other student marks here
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.end_headers()

        try:
            # Parse the URL and query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            # Get student names from the 'name' parameter
            student_names = query_params.get('name', [])

            # Fetch marks for the requested students
            marks = [STUDENT_MARKS.get(name, 'Student not found') for name in student_names]

            # Return the JSON response
            response = {"marks": marks}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except Exception as e:
            # Handle any errors
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

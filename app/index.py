from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json  # Add this import at the top of the file

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data from a file
with open('q-vercel-python.json', 'r') as file:
    students_data = json.load(file)

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [s["marks"] for s in students_data if s["name"] in name]
        return {"marks": marks}
    return {"marks": []}
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [
    {"name": "nax", "marks": 12},
    {"name": "L33", "marks": 26},
    {"name": "0de3hRG", "marks": 34},
    {"name": "G5XU3", "marks": 42},
    {"name": "mRXOtnM8", "marks": 21},
    {"name":"ho8ePmxFs","marks":70},{"name":"Zfmi","marks":55},{"name":"J","marks":23},{"name":"DMUtJX","marks":71},{"name":"t5BhO","marks":66},{"name":"Jkky1M1hQ","marks":45},{"name":"3UWR89Rgv6","marks":97},{"name":"6piPGIJfcF","marks":73},{"name":"F","marks":51},{"name":"3","marks":1},{"name":"Xna9rF","marks":9},{"name":"5IQVXqZo","marks":40},{"name":"Jr","marks":67},{"name":"0O928","marks":0},{"name":"O7","marks":64},{"name":"HsV1","marks":83},{"name":"3w3gI","marks":82},{"name":"egFSOla","marks":98},{"name":"ChW","marks":86},{"name":"Gh","marks":31},{"name":"YiSb","marks":97},{"name":"aJceF","marks":76},{"name":"fxW","marks":78},{"name":"O","marks":38},{"name":"Pdwz1","marks":48},{"name":"v","marks":47},{"name":"Lw","marks":94},{"name":"m","marks":77},{"name":"w","marks":51},{"name":"5Y","marks":55},{"name":"U","marks":55},{"name":"KOc","marks":20},{"name":"1vcbyn","marks":98},{"name":"SAZliK","marks":11},{"name":"a10XKLr","marks":82},{"name":"uN3AXWXrJ","marks":22},{"name":"4Qg","marks":97},{"name":"AVS","marks":53},{"name":"cLv90d","marks":10},{"name":"n","marks":94},{"name":"PTna2i","marks":47},{"name":"P795bQ","marks":3},{"name":"LRepFhFbgY","marks":45},{"name":"g4NYMG31","marks":84},{"name":"PMeVCSois","marks":48},{"name":"9lDbQN8","marks":92},{"name":"JNg01w","marks":77},{"name":"EB","marks":61},{"name":"O","marks":40},{"name":"W64uOG","marks":23},{"name":"4FXj8rz","marks":75},{"name":"Yo6VnMiR","marks":71},{"name":"uUPEZ","marks":32},{"name":"0QrZZ","marks":38},{"name":"URHTNPdl5","marks":61},{"name":"LlOs","marks":99},{"name":"f0Kxwv6Y","marks":61},{"name":"h","marks":86},{"name":"GTz6","marks":28},{"name":"yYFOnfR","marks":88},{"name":"puOz6jxsGj","marks":49},{"name":"JsegBWDG","marks":38},{"name":"UOvU0h","marks":94},{"name":"5cUgoFBBjv","marks":44},{"name":"wpq","marks":59},{"name":"M","marks":37},{"name":"FecSMDB","marks":2},{"name":"UTMzigaJ","marks":36},{"name":"ZE1qySZ","marks":68},{"name":"P0","marks":49},{"name":"vByjQufe","marks":19},{"name":"V","marks":63},{"name":"i6","marks":33},{"name":"loMo9s","marks":33},{"name":"GN","marks":63},{"name":"It","marks":92},{"name":"9T1HLSwbI","marks":16},{"name":"4KlGGoDZ","marks":87},{"name":"iw","marks":66},{"name":"Bg","marks":50},{"name":"AIaN","marks":22},{"name":"GRc0d","marks":84},{"name":"AoQsMDj","marks":86},{"name":"u556BFC","marks":6},{"name":"m0","marks":0},{"name":"bcrwDLukp","marks":14},{"name":"59MAsswl","marks":3},{"name":"ay","marks":9},{"name":"HTNQ0bz","marks":21},{"name":"vaduevGi","marks":29},{"name":"NPb","marks":16},{"name":"p","marks":72},{"name":"eFw0","marks":57},{"name":"V","marks":98},{"name":"U","marks":99},{"name":"crEJAV","marks":53},{"name":"YJz","marks":2},{"name":"PVB8bMPsE","marks":54},{"name":"0","marks":34},{"name":"UHj1Bmd","marks":74}
]

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=X&name=Y` -> {"marks": [10, 20]}
    """
    if not name:
        return {"marks": []}

    result = []
    for student_name in name:
        for student in students_data:
            if student["name"] == student_name:
                result.append(student["marks"])
                break

    return {"marks": result}

# Add this at the end of the file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
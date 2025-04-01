from fastapi import FastAPI, Query, UploadFile, File
from typing import Optional, List
import json 
import httpx
from typing import List
from main import app
from pathlib import Path

def load_data():
    FILE_PATH = Path(__file__).parent / "q-vercel-python.json"
    #data = [{"name":"4","marks":20},{"name":"PDceauB","marks":55},{"name":"PK8YfO4VWN","marks":30},{"name":"1NVMlbtt0","marks":75},{"name":"Bcm","marks":49},{"name":"BUcKp6Uz","marks":69},{"name":"DdVm1","marks":45},{"name":"9FFGRQcq","marks":27},{"name":"gt3rUWe","marks":36},{"name":"zjGAKd91","marks":59},{"name":"eTxsm7F","marks":49},{"name":"jqNj","marks":1},{"name":"uVjgF3JU","marks":11},{"name":"mdGJ","marks":63},{"name":"8as","marks":68},{"name":"MOQDg","marks":35},{"name":"Le","marks":81},{"name":"Li9u","marks":34},{"name":"JdcPhJB","marks":53},{"name":"sNAZG3LVR2","marks":91},{"name":"faOGTvy","marks":73},{"name":"HtgJYdl2c9","marks":68},{"name":"PBBY","marks":28},{"name":"EzD4T","marks":60},{"name":"PLTDz","marks":51},{"name":"Mzp4KV","marks":63},{"name":"619EF","marks":28},{"name":"QVbZ","marks":31},{"name":"L","marks":3},{"name":"O2c7LNUZy","marks":53},{"name":"4r5xfO6ne","marks":75},{"name":"o2RvanH","marks":66},{"name":"rTGUG","marks":38},{"name":"Lak7PpM2T","marks":39},{"name":"nZh6","marks":76},{"name":"E","marks":76},{"name":"EYA1N","marks":53},{"name":"wF","marks":34},{"name":"nZ1cRMxYk","marks":97},{"name":"z","marks":37},{"name":"q9AQDW0","marks":45},{"name":"O44y3xzam","marks":70},{"name":"GQT8QD3","marks":19},{"name":"9Q2k","marks":0},{"name":"z","marks":5},{"name":"pK","marks":15},{"name":"L","marks":73},{"name":"T7Q7J","marks":3},{"name":"MP9epcp","marks":46},{"name":"PHxXJGR","marks":14},{"name":"kWdx","marks":3},{"name":"De0VaPOt","marks":7},{"name":"I2PDAd7","marks":67},{"name":"5e","marks":78},{"name":"N","marks":85},{"name":"a","marks":88},{"name":"Bm4dEOj","marks":41},{"name":"QQWHqv","marks":33},{"name":"tKV50Grl97","marks":26},{"name":"HsfzrsW6G","marks":83},{"name":"cGv","marks":41},{"name":"Eb","marks":37},{"name":"oUvBRWMyE","marks":23},{"name":"rJiEc8FO2","marks":36},{"name":"Q6ictmsZC6","marks":78},{"name":"Vq0CAh","marks":68},{"name":"Smme","marks":86},{"name":"hFodLF","marks":52},{"name":"RemsVbpC","marks":24},{"name":"6RH9Q3xBcn","marks":89},{"name":"qUYZ2Z","marks":76},{"name":"uFA9Wy7c","marks":25},{"name":"PWmu50P","marks":88},{"name":"p5Ehdg","marks":46},{"name":"K","marks":18},{"name":"LZ7","marks":37},{"name":"i4WRda8VDt","marks":57},{"name":"wZTcDaew","marks":72},{"name":"1u","marks":43},{"name":"yJH","marks":60},{"name":"T0zCig","marks":20},{"name":"3qmUsUhXOV","marks":16},{"name":"oVZh6GNbaX","marks":53},{"name":"jZA","marks":41},{"name":"UI2XxX6hx1","marks":34},{"name":"4ax1jYT9uW","marks":35},{"name":"0zA7yEJD","marks":24},{"name":"BIhRmbz","marks":16},{"name":"nU4WmZmnRq","marks":91},{"name":"8GB1iKpSr","marks":78},{"name":"Zkkpgrz","marks":44},{"name":"D8mJe","marks":35},{"name":"FIJFZtZezl","marks":65},{"name":"ih","marks":40},{"name":"lh9","marks":91},{"name":"Ucd79o","marks":86},{"name":"wJtLm","marks":98},{"name":"zmkUC","marks":69},{"name":"6nSl","marks":87},{"name":"APOcH5T","marks":65}]
    data = json.loads(FILE_PATH.read_text())
    return {entry["name"]: entry["marks"] for entry in data}

def load_data_api():
    response = httpx.get("https://tds-app.centralindia.cloudapp.azure.com/vercel/api")
    if response.status_code == 200:
        data = response.json()
        return {entry["name"]: entry["marks"] for entry in data}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api")
async def root_api(name: List[str] = Query(...)):
    students = load_data_api()
    marks = []
    for student in name:
        student = student.strip()
        if student in students:
            marks.append(students[student])
            
    return {"marks": marks}

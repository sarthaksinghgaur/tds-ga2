from fastapi import FastAPI, Query, UploadFile, File
from typing import Optional, List
import json
from typing import List
from main import app
from pathlib import Path

def load_data():
    FILE_PATH = Path(__file__).parent / "q-vercel-python.json"
    data = json.loads(FILE_PATH.read_text())
    return {entry["name"]: entry["marks"] for entry in data}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api")
async def root_api(name: List[str] = Query(...)):
    students = load_data()
    marks = []
    for student in name:
        student = student.strip()
        if student in students:
            marks.append(students[student])
            
    return {"marks": marks}
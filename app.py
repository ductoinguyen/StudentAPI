from flask import Flask, request, jsonify, render_template
import os
import json
import time
import datetime

students = [{
  "id": "18021292",
  "name": "Nguyễn Đức Tới",
  "birthday": "2000-09-08",
  "gender": "Nam",
  "emails": {
    "vnuemai": "18021292@vnu.edu.vn",
    "otheremail": "18021292@gmail.com"
  },
  "contacts": [
    {"name": "ABC", "phone": "0989898989"},
    {"name": "XYZ", "phone": "0639273682"},
  ]
}, {
  "id": "18021318",
  "name": "Vũ Thành Trung",
  "birthday": "2000-09-04",
  "gender": "Nam",
  "emails": {
    "vnuemai": "18021318@vnu.edu.vn",
    "otheremail": "18021318@gmail.com"
  },
  "contacts": [
    {"name": "NDJ", "phone": "0567826323"},
    {"name": "KLM", "phone": "0456782672"},
  ]
}, {
  "id": "18020419",
  "name": "Nguyễn Hùng Duy",
  "birthday": "2000-05-29",
  "gender": "Nam",
  "emails": {
    "vnuemai": "18020419@vnu.edu.vn",
    "otheremail": "18020419@gmail.com"
  },
  "contacts": [
    {"name": "AKD", "phone": "0572832832"},
    {"name": "GSH", "phone": "0768767732"},
  ]
}]

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def getStudents():
  global students
  return app.response_class(json.dumps(students),mimetype='application/json')

@app.route("/student/<id>", methods=["GET"])
def getStudent(id):
  global students
  for student in students:
    if student["id"] == id:
      return app.response_class(json.dumps(student),mimetype='application/json')
  return app.response_class(json.dumps([]),mimetype='application/json')

if __name__ == "__main__":
  app.run(debug=True)

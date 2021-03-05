from flask import Flask, request, jsonify, render_template
import os
import datetime

students = [{
  "id": "18021292",
  "name": "Nguyễn Đức Tới",
  "birthday": datetime.datetime(2000, 9, 8),
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
  "birthday": datetime.datetime(2000, 4, 9),
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
  "birthday": datetime.datetime(2000, 5, 29),
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
  return students

@app.route("/student/<id>", methods=["GET"])
def getStudent(id):
  for student in students:
    if student["id"] == id:
      return student
  return dict()

if __name__ == "__main__":
  app.run(debug=True)

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host='mongodb',
                     port=27017,
                     username='school',
                     password='schoolpassword',
                     authSource='school')
db = client['school']

@app.route('/auth/student', methods=['POST'])
def auth_student():
    user = request.form['user']

    user = db.users.find_one({"user": user})
    if user is not None and user.get('role') == "student":
        return jsonify('message: Authorized'), 200
    return jsonify('error: Unauthorized'), 400

@app.route('/auth/teacher', methods=['POST'])
def auth_teacher():
    user = request.form['user']

    user = db.users.find_one({"user": user})
    if user is not None and user.get('role') == "teacher":
        return jsonify('message: Authorized'), 200
    return jsonify('error: Unauthorized'), 400

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('user')
    course_name = data.get('role')

    db.users.insert_one(data)
    return jsonify('message: User Registered'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

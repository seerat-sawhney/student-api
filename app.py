from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
students = []
next_id = 1

# Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Retrieve a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student is not None:
        return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.json
    student = {
        'id': next_id,
        'name': data['name'],
        'grade': data['grade'],
        'email': data['email']
    }
    students.append(student)
    next_id += 1
    return jsonify(student), 201

# Update a student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    student = next((s for s in students if s['id'] == id), None)
    if student is not None:
        student['name'] = data.get('name', student['name'])
        student['grade'] = data.get('grade', student['grade'])
        student['email'] = data.get('email', student['email'])
        return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

# Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({'message': 'Student deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)


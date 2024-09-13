from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Ruta de los archivos JSON
rooms_file_path = os.path.join('JSON', 'rooms.JSON')
meeting_times_file_path = os.path.join('JSON', 'meeting_times.JSON')

# Verifica si los archivos JSON existen, si no, crea unos vacíos
if not os.path.exists(rooms_file_path):
    with open(rooms_file_path, 'w') as f:
        json.dump([], f)

if not os.path.exists(meeting_times_file_path):
    with open(meeting_times_file_path, 'w') as f:
        json.dump([], f)
        
instructors_file_path = os.path.join('JSON', 'instructors.JSON')

if not os.path.exists(instructors_file_path):
    with open(instructors_file_path, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    # Cargar los datos desde los archivos JSON
    with open(rooms_file_path, 'r') as f:
        rooms = json.load(f)
    
    with open(meeting_times_file_path, 'r') as f:
        meeting_times = json.load(f)
        
    with open(instructors_file_path, 'r') as f:
        instructors = json.load(f)

    return render_template('index.html', rooms=rooms, meeting_times=meeting_times, instructors=instructors)

@app.route('/submit', methods=['POST'])
def submit():
    room_number = request.form['room_number']
    room_name = request.form['room_name']
    
    room_id = request.form['room_id']
    meeting = request.form['meeting']
    
    id = request.form['id']
    name = request.form['name']
    
    # Cargar datos existentes de instructors
    with open(instructors_file_path, 'r') as f:
        instructors = json.load(f)
        
    # Añadir el nuevo instructor
    new_instructor = {
        "id": id,
        "name": name
    }
    instructors.append(new_instructor)
    
    # Guardar los datos en el archivo instructors.JSON
    with open(instructors_file_path, 'w') as f:
        json.dump(instructors, f, indent=4)
        
    
    # Cargar datos existentes de rooms
    with open(rooms_file_path, 'r') as f:
        rooms = json.load(f)

    # Añadir el nuevo salón
    new_room = {
        "room_number": room_number,
        "room_name": room_name
    }
    rooms.append(new_room)

    # Guardar los datos en el archivo rooms.JSON
    with open(rooms_file_path, 'w') as f:
        json.dump(rooms, f, indent=4)

    # Cargar datos existentes de meetings_times
    with open(meeting_times_file_path, 'r') as f:
        meeting_times = json.load(f)

    # Añadir la nueva reunión
    new_meeting = {
        "room_id": room_id,
        "meeting": meeting
    }
    meeting_times.append(new_meeting)

    # Guardar los datos en el archivo meeting_times.JSON
    with open(meeting_times_file_path, 'w') as f:
        json.dump(meeting_times, f, indent=4)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

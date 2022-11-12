
import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from test_floor_plan import engineering_building_first_floor, display_shortest_path
from floor_plan import Room

from location import location

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('demo_webapp.html')

@app.route('/locator')
def locator():
	return render_template('location.html')

@app.route('/locator', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		locname = location(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		display_name = locname['display_name']
		lat = locname['lat']
		lon = locname['lon']
		return render_template('location.html', filename=filename, display_data=display_name, lat=lat, lon=lon)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/navigator')
def astar():
	return render_template("astar.html")

@app.route('/navigator', methods=['POST'])
def find_path():
	start_name = request.form.get("start")
	end_name = request.form.get("end")
	print(start_name)
	print(end_name)
	g = engineering_building_first_floor()
	path = display_shortest_path(g, Room(start_name), Room(end_name))
	return render_template("astar.html", path=path)

if __name__ == "__main__":
	app.run(port=8000)
	
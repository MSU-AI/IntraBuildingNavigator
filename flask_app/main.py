
import base64
import io
import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from test_floor_plan import engineering_building_first_floor, display_shortest_path
from floor_plan import Room

from location import location

import cv2
import numpy as np

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

@app.route('/photo_locator', methods=['POST'])
def photo_locator():
	if 'picture' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['picture']
	# image_bytes = request.files['picture']
	# in_memory_file = io.BytesIO()
	# image_bytes.save(in_memory_file)
	# data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
	# file = cv2.imdecode(data, 1)
	# # file = Image(base64(image_bytes, 'utf-8'))

	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)

		#save the base64 string into a temporary file
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], "temp.txt"))

		#open file with base64 string data
		file = open(os.path.join(app.config['UPLOAD_FOLDER'], "temp.txt"), 'rb')
		encoded_data = file.read()
		file.close()
		#decode base64 string data
		decoded_data=base64.b64decode((encoded_data))
		#write the decoded data back to original format in  file
		img_file = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb')
		img_file.write(decoded_data)
		img_file.close()

		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		locname = location(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		display_name = locname['display_name']
		lat = locname['lat']
		lon = locname['lon']
		return display_name
		# return render_template('location.html', filename=filename, display_data=display_name, lat=lat, lon=lon)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		# return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/navigator')
def astar():
	return render_template("astar.html")

@app.route('/navigator', methods=['POST'])
def find_path():
	# start_name = request.form.get("start")
	# end_name = request.form.get("end")
	# print(start_name)
	# print(end_name)
	# g = engineering_building_first_floor()
	# path = display_shortest_path(g, Room(start_name), Room(end_name))
	path = get_path()
	return render_template("astar.html", path=path)

@app.route('/getpath', methods=['POST'])
def get_path():
	start_name = request.form.get("start")
	end_name = request.form.get("end")
	print(start_name)
	print(end_name)
	g = engineering_building_first_floor()
	path = display_shortest_path(g, Room(start_name), Room(end_name))
	return path

if __name__ == "__main__":
	app.run(port=8000)
	
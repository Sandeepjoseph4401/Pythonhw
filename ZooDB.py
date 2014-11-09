'''
Program     : Maintaing zoo Database online
Description : Maintaining zoo database through web interface
              Querry gets displayed in : localhost:8000
Author      : Sandeep Joseph
'''
from   wsgiref.simple_server import make_server
import re
import sqlite3

def ZooDBWeb(environment, start_response):
    message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded:"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		for item in form_vals.keys():
			message += "<br/>"+item + " = " + form_vals[item]
	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]





httpd = make_server('', 8000, ZooDBWeb)

print("Serving on port 8000...")

httpd.serve_forever()

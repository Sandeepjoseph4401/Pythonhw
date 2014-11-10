'''

Program     : Maintaing zoo Database online

Description : Maintaining zoo database through web interface
           
Querry gets displayed in : localhost:8000

Author      : Sandeep Joseph


'''


from wsgiref.simple_server import make_server
import sqlite3
message  = ""


def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals
    
def listBuild(form_vals):

    for item in form_vals.keys():
        message   += "<br/>"+item + " = " + form_vals[item]
        if item   == "count":
            l1     =  form_vals[item]
        elif item == "animal":
            l2    =  form_vals[item]
        else:
            continue
    listAnimal = [(l1,l2)]
    return listAnimal
    
def ZooDBWeb(environ, start_response):

        status  = '200 OK'
        headers = [('Content-type', 'html; charset=utf-8')]
        start_response(status, headers)
        
        if(environ['REQUEST_METHOD'] == 'POST'):
                message          += "<br>Your data has been recorded:"
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body      = environ['wsgi.input'].read(request_body_size)

                form_vals  = get_form_vals(request_body)
                listAnimal = listBuild(form_vals)
                
                conn       = sqlite3.connect("zoo.sqlite")
                cursor     = conn.cursor()
                try:
                    cursor.executemany("insert into animal_count(name,count) values(?,?)", listAnimal)
                    result = cursor.execute("select * from animal_count")
                    
                except sqlite3.OperationalError:
                    cursor.execute("create table animal_count (name text, count integer)")
                    cursor.executemany("insert into animal_count(name,count) values(?,?)", listAnimal)
                    result = cursor.execute("select * from animal_count")

                else:
                    print("Unexpected Error!!Sorry")
                conn.commit()
                conn.close()

        message += "<h1>Welcome to the Zoo</h1>"
        message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
        message += "<br><br>Count:<input type=text name='count'>"
        message += "<br><br><input type='submit' name='Submit' ></form>"
        return[bytes(message,'utf-8')]

httpd = make_server('', 8000, ZooDBWeb)
print("Serving on port 8000...")

httpd.serve_forever()

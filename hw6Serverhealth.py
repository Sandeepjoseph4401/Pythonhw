'''
Program     : RealTime Server health Monitoring 
Description : Monitors server health and gives alert by displaying in different colors,
              Red -needs attention
              Displays Result in : localhost:8000
Author      : Sandeep Joseph
'''
import psutil, datetime
from   wsgiref.simple_server import make_server

def ServerRealtimeMonitoring(environ, start_response):

    message = ''
    status  = '200 OK'
    n       = 0
    header  = [('Content-type','html; charset = utf-8')]

    start_response(status, header)
    
    message += "<h1>Server Real Time Monitor</h1>"
    
    message += "<table border =\"4\" allign=\"center\" BCOLOR = \"blue\">"
    

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    message += "<tr>"
    message += "<td><b>BOOT TIME: <br></td>"
    message += "<td>{}".format(boot_time)+"<br></td>"
    message += "</tr>"


    cpu_util  = psutil.cpu_percent(interval=1, percpu=True)
    message += "<tr>"
    message += "<td><b>CPU UTILIZATION:</td>"
    message += "<br>"
    message += "<td>"
    for onecpu in cpu_util:
        if onecpu > 50:
            message += "<font color = \"red\">"
        else:
            message += "<font color = \"green\">"
        n += 1    
        message += "CPU {} : {}%".format(n, onecpu)
        message += "<br>"
        message += "<br>"
    message += "</td>"
    message += "</tr>"


    memory_available = psutil.virtual_memory()
    message += "<tr>"
    message += "<td><b>MEMORY INFORMATION </td>"
    message += "<td>"
    if memory_available.used > memory_available.total/2:
            message += "<font color = \"red\">"
    else:
            message += "<font color = \"green\">"        
    message += "Memory Used     :{}".format(memory_available.used)+"<br>"
    message += "<br>"
    message += "Used Percentage :{}%".format(memory_available.percent)+"<br>"
    message += "<br>"
    message += "Total           :{}%".format(memory_available.total)+"<br>"
    message += "<br>"
    message += "Free Percentage :{}%".format(memory_available.free)+"<br>"
    message += "<br>"
    message += "</td>"
    message += "</tr>"
        
    return[bytes(message,'utf-8')]


httpd = make_server('', 8000, ServerRealtimeMonitoring)
print("Serving on port 8000...")

httpd.serve_forever()

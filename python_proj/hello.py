from flask import Flask, render_template
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    txt = "Hello!!! " + " | Host Name: "+ host_name+ " | Host IP: " + host_ip
    return txt
if __name__ == '__main__':
    app.run()

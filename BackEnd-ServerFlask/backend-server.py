from flask import Flask, request
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/fileid/<name>')
def hello_name(name):
    qfile = "queue.txt"
    f = open(qfile, "a")
    random_int = format(name)
    f.write(str(random_int) + "\n")
    f.close()
    #return "Hello {}!".format(name)
    return "done!"

@app.route('/stop/')
def stop():
    qfile = "stoptalking.txt"
    f = open(qfile, "a")
    f.write("stop")
    f.close()
    return "done!"

@app.route('/start/')
def start():
    if os.path.exists("stoptalking.txt"):
        os.remove("stoptalking.txt")
    return "done!"

@app.route('/isTalking/')
def isTalking():
    if os.path.exists("stoptalking.txt"):
        return "false"
    else:
        return "true"
        
if __name__ == '__main__':
    # runs on its own IP address
    #app.run(host='192.168.1.137')
    app.run(port=5001)
    #app.run()

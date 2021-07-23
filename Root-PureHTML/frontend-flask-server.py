from flask import Flask, request
import os
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

        
if __name__ == '__main__':
    # runs on its own IP address
    #app.run(host='192.168.1.137')
    #app.run(port=80)
    app.run()

import socketio
import eventlet
from flask import Flask, render_template
import time
import threading

import amma_api as aapi
import symspell_python


sio = socketio.Server()
app = Flask(__name__)
trie = aapi.amma_api_initiate_trie()
aapi.amma_api_initiate_spell_dictionary(symspell_python)


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('snail/index.html')

@app.route('/indulekha')
def indulekha():
    """Serve the client-side application."""
    return render_template('index.html')

'''@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)'''

@sio.on('request_transliteration')
def message(sid, data):
    #print('message ', data)
    #time.sleep(2)
    t1 = threading.Thread(target=someFunc(data))
    t1.start()
    #t1.join()

@sio.on('request_learning')
def learn(sid, data):
    print("recieved training data as : {} & {}".format(data["malayalam"],data["mangleesh"]))
    aapi.teach_with_new_pair(symspell_python,trie,data["malayalam"],data["mangleesh"])


    

'''@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)'''

def someFunc(data):
    #print("starts thread")
    result = aapi.amma_api_suggest_word(trie,data["client_input"],symspell_python)
    stream = ""
    #print(result)
    for item in result:
        #print(item)
        try:
            stream = stream + item[0] + ":"
        except:
            print("nothing retrieved as suggestion")
    print(stream)
    sio.emit('transliteration_success',stream)
    #print("end thread")
 
if __name__ == '__main__':
    #app.run()
    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
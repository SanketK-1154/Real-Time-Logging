from flask import Flask, render_template, Response
import time
import os

app = Flask(__name__)

LOG_FILE = '/home/sanket/PycharmProjects/sse_log/.venv/my.log'

def stream_log_updates():
    with open(LOG_FILE, 'r') as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if line:
                yield f"data: {line}\n\n"
            time.sleep(1)

def get_last_n_lines(n=10):
    with open(LOG_FILE, 'rb') as files:
        files.seek(-10000, os.SEEK_END)
        line = files.read(10000)
        linestr = line.decode("utf-8")
        # a = []
        # while line != '' :
        #      print(line)
        #      a.append(line)
        #      line = files.read(100)
        return linestr.split("\n")[-n:]

@app.route('/')
def index():
    last_lines = get_last_n_lines()
    return render_template('index.html', logs=last_lines)

@app.route('/stream')
def stream():
    return Response(stream_log_updates(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run()
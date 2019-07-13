from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import send_from_directory

import func_markAtom as Mk

import os
from pathlib import Path
workpath = Path(os.path.abspath(os.path.dirname(__file__)))
imgdir = workpath / 'images'

if __name__ == '__main__':
    app = Flask(__name__)
else:
    from server_def import app

@app.route('/mark/pattern_input')
def mark_visualize():
    return render_template('mark.html')

@app.route('/mark/pattern_result', methods=['POST', 'GET'])
def mark_getSMART(imgsrc='mark.png'):

    Mk.mark(request.form['smart'],request.form['mark'],str(imgdir / imgsrc) )

    return render_template('mark_result.html', imgsrc='mark_image',smart = request.form['smart'],pattern = request.form['mark'])

@app.route('/mark/pattern_error')
def mark_pic():
    image_data = open( str(imgdir / 'not_specified.png'), "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/mark/image')
def mark_markimg():
    image_data = open( str(imgdir / 'mark.png'), "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response

"""
@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = os.getcwd()  # 假设在当前目录
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    return response
"""

if __name__ == '__main__':
    app.run(port=5720,debug=True)
else:
    print("Loaded module : "+__name__)
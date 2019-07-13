from flask import render_template

import service_mark

import service_search

import service_getSMILE

from server_def import app as main_server

@main_server.route('/')
def search_visualize():
    return render_template('index.html')


main_server.run(port=80,debug=False)
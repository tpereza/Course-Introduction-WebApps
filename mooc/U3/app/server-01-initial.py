# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """
    It process the '/' url.
    :return: basic HTML
    """
    return "Hello Word! This is the answer of the server"

@app.route('/ex2')
def function_for_ex2():
    return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/my-socnet-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> This is the page title</title>' \
           '</head>' \
           '<body> <div id="container">' \
           '<h1>Example of HTML Content</h1>' \
		   '<a href="/"> Home </a>'\
	       '</div> </body>' \
           '</html>'

# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
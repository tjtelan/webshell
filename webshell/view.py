import os
from bottle import route, static_file 
from jinja2 import Environment, FileSystemLoader

loader=FileSystemLoader('webshell/templates')
env = Environment(loader=loader)

@route('/')
def index():
	return env.get_template('index.html').render()

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='webshell/static')

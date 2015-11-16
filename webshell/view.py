import os
from bottle import route, jinja2_view
from jinja2 import Environment, FileSystemLoader

loader=FileSystemLoader('webshell/templates')
env = Environment(loader=loader)

#@jinja2_view('index.html', template_lookup=['webshell/templates'])
@route('/')
def index():
	return env.get_template('index.html').render()

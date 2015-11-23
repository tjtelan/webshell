from __future__ import unicode_literals
from bottle import request, response, post, route, static_file
import subprocess
import json
import socket
import time
import os
import hashlib
from model import jobs

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='webshell/static')

@post("/api/command")
def run_command_form():
	command = request.forms.get("command")

	job_id = start_job(command)

	return job_id

def start_job(command):

	# Generate id
	job_id = generate_id()

	# Use id as key for storing execution status and stdout/stderr/exitcode
	jobs[job_id] = "Queued"

	run_command(job_id, command)
	return { 'job_id' : job_id }

def run_command(job_id, command):
	print jobs[job_id]
	print command


def generate_id() :
	hostname = socket.gethostname()
	timestamp = time.time()
	salt = str(os.urandom(1)).encode('base-64')
	key = "{0}{1}{2}".format(hostname, timestamp, salt)

	return hashlib.sha512(key.encode('utf-8')).hexdigest()
		

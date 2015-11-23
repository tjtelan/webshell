from __future__ import unicode_literals
from bottle import request, response, post, get, route
import subprocess
import json
from model import jobs, generate_id

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

@post("/api/command")
def run_command_form():
	return start_job(request.forms.get("command"))

# TODO: Start run_command in a thread
# FIXME: Make sure jobs table modifications get moved into model.py
def start_job(command):

	# Generate id
	job_id = generate_id()

	# Use id as key for storing execution status and stdout/stderr/exitcode
	jobs[job_id] = "Queued"

	# TODO: Start me in a separate thread
	run_command(job_id, command)

	return { 'job_id' : job_id }

# TODO: Start thread, and join, figure out reasonable way to have running stdout, for polling
def run_command(job_id, command):
	pass
	#print jobs[job_id]
	#print command

@get("/api/status/<job_id>")
def get_job_id_status(job_id):
	pass
	# { jobid: ..., status: running, }
	# { jobid: ..., status: finished, exitcode: ..., stdout: ..., stderr: ...}


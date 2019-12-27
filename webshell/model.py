import sqlalchemy
import socket
import time
import os
import hashlib
import base64

jobs = dict()

def generate_id():
	hostname = socket.gethostname()
	timestamp = time.time()
	salt = base64.b64encode(os.urandom(1))
	key = "{0}{1}{2}".format(hostname, timestamp, salt)

	return hashlib.sha512(key.encode('utf-8')).hexdigest()
		

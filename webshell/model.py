import sqlalchemy
import socket
import time
import os
import hashlib

jobs = dict()

def generate_id():
	hostname = socket.gethostname()
	timestamp = time.time()
	salt = str(os.urandom(1)).encode('base-64')
	key = "{0}{1}{2}".format(hostname, timestamp, salt)

	return hashlib.sha512(key.encode('utf-8')).hexdigest()
		

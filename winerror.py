#!/usr/bin/env python

import json, zlib
import os
import sys

from pathlib import Path
from database_util import create_cache


HOME = str(Path.home())

if os.name != 'nt':
	CACHE_FOLDER = "{}/.config/winerror".format(HOME)
else:
	CACHE_FOLDER = '{}\\.winerr'.format(HOME)

CACHE_FILE = "{}/cache.bin".format(CACHE_FOLDER)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: {} WIN_ERROR_CODE".format(sys.argv[0]))
		sys.exit()
	

	if not os.path.exists(CACHE_FILE):
		print("Database not found, will be created...")
		create_cache()
		print("\n\n")

	try:	
		base = 10
		if '0x' in sys.argv[1]:
			base = 16

		error_code = int(sys.argv[1], base=base)
	except:
		print("Invalid number {}".format(sys.argv[1]))
		sys.exit()

	error_code = str(error_code)

	cached_db = None
	with open(CACHE_FILE, 'rb') as cachefd:
		cached_db = zlib.decompress(cachefd.read())
		cached_db = json.loads(cached_db) 
	

	error = cached_db.get(error_code, False)
	
	if error:
		print("Error code: {}\n\tValue: {}\n\tDescription: {}".format(error_code, error.get('error_status'), error.get('description')))
		exit(0)

	print("Error code {} not found!".format(error_code))





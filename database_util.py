import requests
import json, zlib
import os, shutil

from bs4 import BeautifulSoup
from pathlib import Path
from pprint import pprint

ERRORS_CODE = [
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--500-999-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--1000-1299-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--1300-1699-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--1700-3999-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--4000-5999-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--6000-8199-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--8200-8999-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--9000-11999-',
	'https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--12000-15999-'
]


HOME = str(Path.home())

if os.name != 'nt':
	CACHE_FOLDER = "{}/.config/winerror".format(HOME)
else:
	CACHE_FOLDER = '{}\\.winerr'.format(HOME)

CACHE_FILE = "{}/cache.bin".format(CACHE_FOLDER)


def create_cache():
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}	

	print("Downloading system error list from Microsoft...")
	
	soups = []
	for error_site in ERRORS_CODE:
		html_page = requests.get(error_site, headers=headers)
		if html_page.status_code == 200:
			soup = BeautifulSoup(html_page.content.decode(), "html.parser")
			soups.append(soup)

		

	print("Processing {} pages...".format(len(soups)))

	cache_data = {}

	for soup in soups:
		error_table = soup.find('dl').contents
		error_table.pop()
		error_table.pop(0)
		
		error_status = ""

		for i in range(0, len(error_table), 4):
			error_description = error_table[i].find('p').find('span')['id']
			error_code   = error_table[i+2].find_all('p')[0].text
			error_status = error_table[i+2].find_all('p')[0].text
		
			error_code = error_code.split(' ')[0]

			cache_data[error_code] = {
				'description': error_description,
				'error_status': error_status
			}

	
	print("Compressing database...")

	json_str = json.dumps(cache_data)
	compressed = zlib.compress(json_str.encode())
	
	
	if os.path.exists(CACHE_FOLDER):
		shutil.rmtree(CACHE_FOLDER)
	
	os.mkdir(CACHE_FOLDER)

	print("Saving...")

	with open(CACHE_FILE, "wb") as cachefd:
		cachefd.write(compressed)
	
	print("Saved cache at {}".format(CACHE_FILE)) 



if __name__ == '__main__':
	create_cache()


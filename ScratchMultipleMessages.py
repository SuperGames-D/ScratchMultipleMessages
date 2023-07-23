import requests

usernames = []
result =[]

print("Scratch Multiple Messages")
print()

print("Enter usernames to get message count of (one per line)")
print("After you enter all usernames, leave blank to start")

username = " "
while not username == "":
	username = input()
	if not username == "":
		usernames.append(username)

listlen = len(usernames)
print()
print()

print("Getting data...")

for i in range(listlen):
	valid = requests.get("https://api.scratch.mit.edu/accounts/checkusername/" +usernames[i])
	url = "https://api.scratch.mit.edu/users/" +  usernames[i]  + "/messages/count"
	page = requests.get(url)
	txt = usernames[i] + "  -  " + page.text
	result.append(txt)
	
for i in range(listlen):
	print(result[i])

print()	
input("Press enter to close")

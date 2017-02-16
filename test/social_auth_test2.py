from social_auth.facebook.authentication import login
username = raw_input('Enter username: ')
password = raw_input('Ener password: ')

login = login(username, password)
print login


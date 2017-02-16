import social_auth.facebook.authentication
username = raw_input('Enter username: ')
password = raw_input('Enter password: ')
login = social_auth.facebook.authentication.login(username, password)
print login

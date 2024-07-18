from user import User
user = User()
print(user.register('james', 111, 'test@gmail.com', 'abc'))

email = input('what is your email')
password = input('what is you password')

print(user.login(email, password))

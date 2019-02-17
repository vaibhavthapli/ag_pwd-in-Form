while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        print('Age successfully saved')
        break
    else:
        print('Please enter age in 123')

while True:
    print('Enter your password: ')
    password = input()
    if password.istitle():
        print('Password successfully saved')
        break
    else:
        print('Password contain first capital letter ')

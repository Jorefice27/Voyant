s = set()
passwords = open('passwords.txt')
for password in passwords:
    s.add(password.strip())

print('Enter "checkpassword" followed by a password to see if it is a common password (ex "checkpassword abc123")')
print('Enter "Exit" to quit the program\n')
while True:
    userInput = input('$').strip()
    if userInput.lower() == 'exit':
        break
    # expecting input with the form "checkpassword {password}"
    arr = userInput.split(' ')
    if len(arr) != 2: # doesn't match the above form
        print('Invalid input')
    elif arr[0].lower() != 'checkpassword':
        print('Invalid input')
    elif arr[1] in s:
        print('Common password')
    else: 
        print('Not common password')
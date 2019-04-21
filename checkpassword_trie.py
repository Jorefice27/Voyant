from trie import Trie

t = Trie()
passwords = open('passwords.txt')
for password in passwords:
    t.add(password.strip())

print('Enter "checkpassword" followed by a password to see if it is a common password')
print('Enter "Exit" to quit the program\n')
while True:
    userInput = input('$').strip()
    if userInput.lower() == 'exit':
        break
    arr = userInput.split(' ')
    if len(arr) != 2:
        print('Invalid input')
    elif arr[0].lower() != 'checkpassword':
        print('Invalid input')
    elif t.contains(arr[1]):
        print('Common password')
    else:
        print('Not common password')
        

import random
import math

# Create a list of passwords

passwords = []

# def part
# Input Password

def inputpw():
    input_title = input('Enter your title of password: ')
    for title, password in passwords:
        if title == input_title:
            print('the title already exists')
            return
   # y = int(input("Do you)
    repeat = False
    input_password = input('Enter your passsword: ')
    for title, password in passwords:
        if password == input_password:
            repeat = True
            a = int(input("Your password has already existed, would you like to generate a random password to instead it?\n(1) Yes\n(2) No\nEnter your choice: "))
            if a == 1:
                b = input("Do you want to customized your random password?\n(1) Yes\n(2) No\nEnter your choice: ")
                if b == "2" or b =="No":
                    randomPassword=getRandomPassword()
                    temp=randomPassword
                elif b == "1" or b == "Yes" :
                    randomPassword=customize()
                    temp=randomPassword
                print("will be your new password")
                changed = (input_title, randomPassword)
                passwords.append(changed)
                c = input("Do you want to check the strength of this password?\n(1) Yes\n(2) No\nEnter your choice: ")
                if c == "1" or c == "Yes" :
                    passwordAnalysis(temp)
                update_pw()
                break
            elif a == 2:
                continue
    t = (input_title, input_password)
    if repeat == False:
        passwords.append(t)
        c = input("Do you want to check the strength of this password?\n(1) Yes\n(2) No\nEnter your choice: ")
        if c == "1" or c == "Yes" :
            passwordAnalysis(input_password)
    update_pw()


# Input password repeatly

def repeat():
    while True:
        inputpw()
        is_quit = input("Enter 'quit' to quit or Enter anything to continue to imput password: ")
        if is_quit == 'quit':
            break
        else:
            continue
        
# load the file of passwords

def load_password():
    with open('pw.txt', 'w+') as file:
        pws = file.readlines()
        for line in pws:
            line = line.strip()
            title, password = line.split(',')
            t = (title, password)
            passwords.append(t)
            
# Update Password

def update_pw():
    with open('pw.txt', 'w') as file:
        for title, password in passwords:
            file.write(title + ',' + password + '\n')

# Change Password

def change_pw():
    to_ask = True
    while to_ask:
        old_t = input('Enter the title of password which you want to update: ')
        for title, password in passwords:
            t = (title , password)
            if title == old_t:
                new_pw = input('Your old password is, ' + password + '. ' + 'Enter your new password: ')
                new_pw_again = input('Enter the new password again: ')
                if new_pw == new_pw_again:
                    passwords.remove(t)
                    passwords.append((title, new_pw))
                    update_pw()
                    print('Change Successful')
                    return
                else:
                    print('the two passwords are not the same')
                    to_ask = True
                    break
        to_ask = False
        change_success = False
    if change_success:
        print('Change Successful')
    else:
        print('title not found')

# This function can generate random password
# The library of "import random" and code "random.randint()" is refer to (https://docs.python.org/3/library/random.html)
def getRandomPassword(lowRandom=8,highRandom=14,math=True,upper=True,lower=True,symbol=True):
    # This code generate random length of the password while no special requirement
    passwordLength = random.randint(lowRandom,highRandom)
    randomList = []
    # The list below contain those common symbol in password
    symbolList = ["\"","#","$","%","&","*","/",":",";","@","^","-","_","~"]
    i = 0
    while i < passwordLength :
        # This code is to allocate the ratio of different type of character
        chrType = random.randint(0,9)
        if chrType in range(0,5) :
            if math == True :
                randomChr = chr(random.randint(48,57))
                randomList.append(randomChr)
                i+=1
        elif chrType in range(5,7) :
            if upper == True :
                randomChr = chr(random.randint(65,90))
                randomList.append(randomChr)
                i+=1
        elif chrType in range(7,9) :
            if lower == True :
                randomChr = chr(random.randint(97,122))
                randomList.append(randomChr)
                i+=1
        else :
            if symbol == True :
                randomChr = symbolList[random.randint(0,13)]
                randomList.append(randomChr)
                i+=1
    randomPassword = "".join(randomList)
    print(randomPassword)
    return(randomPassword)

# This function can analysis the password of the password inputed and output the grade of the strength
# The fomular of calculating password strength is partly come form(https://www.omnicalculator.com/other/password-entropy)
def passwordAnalysis(password):
    chrList = set(password)
    containMath = False
    containUpperChr = False
    containLowerChr = False
    containSymbol = False
    i = 0
    # This part check the size of the pool of unique characters in password
    while i < len(password) :
        if ord(password[i]) in range(48,58) :
            containMath = True
        elif ord(password[i]) in range(65,91) :
            containUpperChr = True
        elif ord(password[i]) in range(97,123) :
            containLowerChr = True
        else :
            containSymbol = True
        i += 1
    noOfType = 0
    if containMath == True :
        noOfType += 10
    if containUpperChr == True :
        noOfType += 26
    if containLowerChr == True :
        noOfType += 26
    if containSymbol == True :
        noOfType += 32

    # This formula consider the length of the password, the size of the pool of unique characters in password and the number of unique characters in password
    if noOfType != 0 :
        strengthIndex = len(password) * math.log2(noOfType) * (len(chrList) ** 0.5)
    else :
        strengthIndex = 0
        
    if strengthIndex == 0 :
        strength = "empty password"
    elif strengthIndex < 0 :
        strength = "error"
    elif strengthIndex < 100 :
        strength = "weak\nYou can :\n1.add the length of your password\n2.use various type of character\n3.use non-repeating unique words\nto strengthen your password\n"
    elif strengthIndex < 200 :
        strength = "medium"
    else :
        strength = "strong"
    print(strength)

def customize():
    q2 = int(input("Please input the length of the random password(e.g.8):\n"))
    q3 = input("Do you want to contain uppercase letters in the random password?\n(1) Yes\n(2) No\nEnter your choice: ")
    if q3 == "1" or q3 == "Yes" :
        upper = True
    else :
        upper = False
    q4 = input("Do you want to contain lowercase letter in the random password?\n(1) Yes\n(2) No\nEnter your choice: ")
    if q4 == "1" or q4 == "Yes" :
        lower = True
    else :
        lower = False
    q5 = input("Do you want to contain symbol in the random password?\n(1) Yes\n(2) No\nEnter your choice: ")
    if q5 == "1" or q4 == "Yes" :
        symbol = True
    else :
        symbol = False
    randomPassword=getRandomPassword(q2,q2,True,upper,lower,symbol)
    return(randomPassword)
# main part

load_password()
while True:                # if user choose to input pw
    x = int(input('(1) Input Password\n(2) Retrieval All Passwords\n(3) Update Password\n(4) Generate Random Password\n(5) Password Strength Analysis\nEnter your choice: '))
    if x == 1:
        inputpw()
        y = int(input('(1) Back menu\n(2) Add another password\nEnter your choice: '))
        if y == 1:
            continue
        elif y == 2:
            repeat()
        else:
            continue
    elif x == 2:        # if user want to retrieval all the passwords
        with open('pw.txt', 'r') as file:
            pws = file.readlines()
            for pw in pws:
                pw = pw.strip()
                print(pw)
    elif x == 3:          # if user want to change passwords
        change_pw()
    elif x == 4 :
        # User can generate random password by either giving requirement or not
        q1 = input("Do you want to customized your random password?\n(1) Yes\n(2) No\nEnter your choice: ")
        if q1 == "2" or q1 == "No" :
            getRandomPassword()
        elif q1 == "1" or q1 == "Yes" :
            customize()
        else :
            print("Invalid input\n")
    elif x == 5 :
        y = input("Please input your password and press 'Enter'\n")
        passwordAnalysis(y)

    else :
        print("Invalid input\n")


    
        

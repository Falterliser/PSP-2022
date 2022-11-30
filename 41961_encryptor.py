# File: 41961_encryptor.py <-- Replace with *your* file name
# Author: Thanh Son Aiden Nguyen <-- Replace with *your* name
# Email Id: nguty385@mymail.unisa.edu.au <-- Replace with *your* email id
# Description: Assignment 1 - Part 2 of assignment 1 / The encryptor
# This is my own work as defined by the University's
# Academic Misconduct policy.


#Value for encryption (string)
estring = ''

#Value for decryption (string)
dstring = ''

#Values for brute force decryption (string/offset)
bstring = ''
boffset = 0

#Value to store the encrypting strings
encrypt = ''
#Value to store the decrypting strings
decrypt = ''
#Value to store finished encryption string
efinish = []
#Value to store finished decryption string
dfinish = []
#Value to store finished decyption strings
bfinish = []

#Value to iterate through list of the strings to be encrypted/decrypted
i = 0
#Variable to check whether the ASCII value after adding the offset is valid
checkvalue = 0
#Variable to track the number of the finished decrypted strings
offsetnum = 1
bcount = 0

#While loop for user menu choice validation
Menu = True
#Variable for user menu choices
user = 0


def display_details():
    print("File: 41961_encryptor.py")
    print("Author: Thanh Son Aiden Nguyen")
    print("Stud ID: 41961")
    print("Email ID: nguty385")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    print("")



def get_menu_choice():
    inputcheck = False
    #local variable to check for valid user input
    print("*** Menu ***")
    print("")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")
    print("")
    user = input("What would you like to do [1,2,3,4]? ")
    while not inputcheck:
    #Using .isdigit() to determine whether the user input was a character or digit which can then be further narrowed down to the 4 digits wanted for menu item selection
        if user.isdigit():
            if int(user) == 1:
                choice = 1
                inputcheck = True
            elif int(user) == 2:
                choice = 2
                inputcheck = True
            elif int(user) == 3:
                choice = 3
                inputcheck = True
            elif int(user) == 4:
                choice = 4
                inputcheck = True
            else:
                print("Invalid choice, please enter either 1, 2, 3 or 4.")
                user = input("What would you like to do [1,2,3,4]? ")
        else:
            print("Invalid choice, please enter either 1, 2, 3 or 4. ")
            user = input("What would you like to do [1,2,3,4]? ")
    return choice



   
def get_offset():
    inputcheck = False
    #Local variable to check for valid user input
    offset = input("Please enter offset value (1 to 94): ")
    while not inputcheck:
        if offset.isdigit():
            if int(offset) in range(0,95):
                offset = int(offset)
                inputcheck = True
        else:
            offset = input("Please enter offset value (1 to 94): ")
    return offset



display_details()

#Choice value becomes whatever input was returned from the 'get_menu_choice' function
choice = get_menu_choice()

while Menu:
    #Section to encrypt string
    if choice == 1:
        print("")
        estring = input("Please enter string to encrypt: ")
        # eoffset = int(input("Please enter offset value (1 to 94): "))
        offset = get_offset()
        print("")
        estring = list(estring)
    #This section is here to determine whether or not the new ASCII value needs to be wrapped around 32-126
        for checkvalue in estring:
            checkvalue = offset + ord(estring[i])
            if checkvalue >= 127:
                encrypt = (offset - 95) + ord(estring[i])
                efinish.append(chr(encrypt))
                i += 1
            elif checkvalue <= 31:
                encrypt = (offset + 95) + ord(estring[i])
                efinish.append(chr(encrypt))
                i += 1
            else:
                encrypt = offset + ord(estring[i])
                efinish.append(chr(encrypt))
                i += 1
        i = 0
    #Resetting 'i' value here to reuse for later for loops
    #This here is to print the encrypted result... but i think that's a TAD obvious
        efinish = ''.join(efinish)
        print('')
        print('Encrypted string:')
        print(efinish)
    #resetting efinish followed by prompting another menu choice will allow for the user to encrypt more if they wish
        efinish = []
        choice = get_menu_choice()

    #Section to decrypt string
    elif choice == 2:
        dstring = input("Please enter string to decrypt: ")
        offset = get_offset()
        print("")
        dstring = list(dstring)
        for checkvalue in dstring:
            checkvalue = ord(dstring[i]) - offset
            if checkvalue >= 127:
                decrypt = ord(dstring[i]) - (95 - offset)
                dfinish.append(chr(decrypt))
                i += 1
            elif checkvalue <= 31:
                decrypt = ord(dstring[i]) + (95 - offset)
                dfinish.append(chr(decrypt))
                i += 1
            else:
                decrypt = ord(dstring[i]) - offset
                dfinish.append(chr(decrypt))
                i += 1
        i = 0
    #This here is to print the encrypted result... but i think that's a TAD obvious
        dfinish = ''.join(dfinish)
        print('')
        print('Decrypted string:')
        print(dfinish)
        dfinish = []
        choice = get_menu_choice()


    #Section to brute force the string
    elif choice == 3:
        bstring = input("Please enter string to decrypt: ")
        print("")
        bstring = list(bstring)
        while bcount < 94:
            if i > len(bstring) - 1:
                i = 0
            for checkvalue in bstring:
                checkvalue = ord(bstring[i]) + offsetnum
                if checkvalue >= 127:
                    decrypt = checkvalue - 95
                    bfinish.append(chr(decrypt))
                elif checkvalue <= 31:
                    dncrypt = checkvalue + 95
                    bfinish.append(chr(decrypt))
                else:
                    decrypt = checkvalue
                    bfinish.append(chr(decrypt))
                i += 1
            bfinish = ''.join(bfinish)
            print(f"Offset: {offsetnum} = Decrypted string: {bfinish}")
            offsetnum += 1
            bcount += 1
            bfinish = []
        i = 0
        choice = get_menu_choice()


    #Goodbye :)
    elif choice == 4:
        print("Goodbye.")
        Menu = False
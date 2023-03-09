en_password = ""
#menu
print("Menu")
print("-------------")
print("1. Encode ")
print("2. Decode")
print("3. Quit ")
print("")


#options

while True:
    choice = int(input("Please enter an option: "))
    if choice == 1:
        #encode
        password = input("Please enter your password to encode: ")
        holdlist = []
        en_password = ""
        holdlist[:0] = password
        for i in range(len(password)):
            for j in range(3):
                holdlist[i] = int(holdlist[i]) + 1
                if int(holdlist[i]) == 10:
                    holdlist[i] = 0
        #turn back to string
        for num in holdlist:
            en_password += str(num)
        print("Your password has been encoded and stored! ")
        print()
    elif choice == 2:
        pass
    elif choice == 3:
        exit()
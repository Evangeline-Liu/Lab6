# Encode: Evangeline
# Decode: Renan

#for decode function
def decode():
    choice = int(input("Please enter an option: "))
    if choice == 1:
        #encode
        password = input("Please enter your password to encode: ")
        #reset nums
        holdlist = []
        global en_password
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
        #decode
        dec_password = ""
        #password = "123456789"
        for num in en_password:
            num_dec = int(num) - 3
            if num_dec < 0:
                num_dec += 10
            dec_password = dec_password + str(num_dec)
        #print(num_dec)
        print(f"The encoded password is {en_password}, and the original password is {dec_password}. ")
        print()
    elif choice == 3:
        #exit
        exit()
        #


def main():

    continue_menu = True
    while continue_menu == True:
        # menu
        print("Menu")
        print("-------------")
        print("1. Encode ")
        print("2. Decode")
        print("3. Quit ")
        print("")
        decode()

if __name__ == "__main__":
    main()
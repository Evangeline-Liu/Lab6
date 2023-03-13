decoded = ""
password ="123456789"
for num in password:
    num_dec = int(num) - 3
    if num_dec < 0:
        num_dec += 10
    decoded = decoded + str(num_dec)
print(num_dec)
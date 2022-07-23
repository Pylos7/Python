# Nestor Ingles Jr
# CSC 121 001

bank_balance = float(input("Enter current bank balance:"))
interest_rate = float(input("Enter interest rate:"))
months_passed = int(input("Enter the ammount of time that passes:"))
print(bank_balance * (1 + interest_rate) ** months_passed)



# Revel wanted functions but did not ask for them so I did not know
# what to do untill I saw the answer.

def savings(present, interest, time):
    return present * (1 + interest)**time

def main():
    present = float(input('Enter current bank balance:'))
    interest = float(input('Enter interest rate:'))
    time = float(input('Enter the amount of time that passes:'))
    print(savings(present, interest, time))

main()

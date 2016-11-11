

import account



def main():

    johnny = account.Account("Johnny", 10, 2000)

    donny = account.Account("Donny", 11, 200)

    connie = account.Account("Connie", 12, 20)

    if johnny.withdraw(1999):
        print(johnny)
    else:
        print("Insufficient funds.")


    if connie.withdraw(21):
        print("Insufficient funds")
    else:
        print(connie)


    donny.deposit(200)
    print(donny)


    johnny.deposit(25000)
    print(johnny)


main()

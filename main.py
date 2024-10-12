name = input("What is your name? ")
bill = 5000
payed = int(input("How much have you payed out of 5000? "))
def func(bill,payed):
    return(bill-payed)
due= func(bill,payed)
print("Your due amount is ",due)

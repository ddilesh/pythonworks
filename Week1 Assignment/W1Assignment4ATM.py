withdrawalamt=int(input("Enter the amount to withdraw: "))
if(withdrawalamt%100==0):
    print("Dispensing cash...")
else:
    print('Invalid amount')
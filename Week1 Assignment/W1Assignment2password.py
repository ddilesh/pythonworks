correctpassword='openAI123'
for i in range(3):
    password=input("Enter your password: ")
    if password==correctpassword:
        print('Login Successful')
        break
else:
        
            print('Account Locked')

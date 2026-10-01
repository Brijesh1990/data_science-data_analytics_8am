email=input("Enter your email :")
password=input("Enter your password :")

if email=='admin@gmail.com' and password=='admin123456':
    res="You are Logged in as admin successfully"
else:
    res="Your credentials are wrong try again" 

print(res)
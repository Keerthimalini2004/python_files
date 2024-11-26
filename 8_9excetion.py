#RAISE
print('----INSTAGRAM----')
password_=input("enter your password:")
PW='Jsp@123'
try:
    if password_==PW:
        print("Login Successfully")
    else:
        raise exception
except Exception:
    print('invalid password')

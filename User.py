username = "P@ssword"
password = "@onetoten"
attempts = 3

while attempts > 0:
    user = input("enter username: ")
    pwd = input("enter passsword: ")
    
    if user == username and pwd == password:
        print("login successful! Welcome.")
        break
    else:
        attempts-=1
        print(f"incorrect.you have {attempts} attempts left.")
        
    if attempts == 0:
        print("account locked. too many attempts!")
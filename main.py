def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("account_details.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
for i in range(6):
    create_account()
    with open("account_details.txt", "r") as file:
        print(file.read())

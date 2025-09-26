import json    # Program of collecting data from user, it creates a file and store data init.
import os
def user_data():

        if os.path.exists("users.json"):
                with open("users.json", "r") as f:
                        users = json.load(f)
        else:
                users = {}

        n = int(input("Enter the no of user's data you want to store: "))
        
        for i in range(1,n+1):
                user_id = input(f"{i}. Enter user's ID: ")
                name = input(f"{i}. Enter user's Name: ")
                age = input(f"{i}. Enter user's Age: ")
                users[user_id]= {"Name": name, "Age": age}

        with open("users.json","a") as f:
                json.dump(users, f, indent=4)        

        search_id =  (input("SEARCH USER INFO [User ID]: "))
        if search_id in users:
                print(f"User's id is: {search_id}")
                print(f"User's Name is: {users[search_id]['Name']}")
                print(f"User Age is: {users[search_id]['Age']}")
        else:
                print("user not found")

user_data()
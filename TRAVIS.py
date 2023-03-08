# TRAVIS

import time

known_users = ["Alice", "Bob", "Claire", "Dan", "Eamma", "Fred", "Georgie", "Harry", "Łukasz"]

print(len(known_users))

while True:
    print("Hi! My name is Travis! I am seciurity robot")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Beep Beep proccesing data..")
        time.sleep(2)
        print("Name recognised")
        time.sleep(1)
        print("ohhh I know You! Welcome {}!".format(name))
        time.sleep(1)
        remove = input("Do you want to be removed from the list (y/n)?: ").lower()
        if remove == "y":
            known_users.remove(name)
            time.sleep(1)
            print("You have been removed! Bye Bye now.")
        else:
            time.sleep(1)
            print(" Ok then you can stay as long as you want {}".strip().format(name))
    
    else:
        print("Beep Beep proccesing data..")
        time.sleep(2)
        print("Name NOT recognised")
        time.sleep(1)
        print("ohhh I dont know You!")
        time.sleep(1)
        add = input("Do you want to be added to the list (y/n)?: ").lower()
        if add == "y":
            known_users.append(name)
            time.sleep(1)
            print("Congratulation {}. You have been added to the list!".strip().format(name))
        else:
            time.sleep(1)
            print("No issues my Friend! Bye bye now.")
        
        

       

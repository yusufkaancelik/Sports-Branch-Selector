def eligible():
    print("You can join this branch.")

def not_eligible():
    print("You are not eligible for this branch.")

branches = ["Football", "Swimming", "Handball", "Basketball", "Gymnastics"]
girls = {"Nihal", "Ipek", "Ozden"}
boys = {"Enes", "Ufuk", "Ulas", "Burak", "Caner"}

name_input = input("Enter your name: ").lower()
age_input = int(input("Enter your age: "))
index = 0

for branch in branches:
    index += 1
    print(index, branch)

branch_input = input("Enter the branch you want to choose: ").lower()

if name_input in girls:
    if branch_input == "football" or branch_input == "1":
        certification = input("Do you have a football certificate? [y/n]: ").lower()
        if certification == "y":
            eligible()
        else:
            not_eligible()

    elif branch_input == "swimming" or branch_input == "2" and age_input <= 6:
        eligible()

    elif branch_input == "handball" or branch_input == "3" and age_input <= 8:
        eligible()

    elif branch_input == "basketball" or branch_input == "4" and 20 <= age_input <= 30:
        eligible()

    elif branch_input == "gymnastics" or branch_input == "5":
        not_eligible()

    else:
        not_eligible()

elif name_input in boys:
    if branch_input == "football" or branch_input == "1":
        certification = input("Do you have a football certificate? [y/n]: ").lower()
        if certification == "y":
            eligible()
        else:
            not_eligible()

    elif branch_input == "swimming" or branch_input == "2" and age_input <= 6:
        eligible()

    elif branch_input == "handball" or branch_input == "3" and age_input <= 8:
        eligible()

    elif branch_input == "basketball" or branch_input == "4" and 20 <= age_input <= 30:
        eligible()

    elif branch_input == "gymnastics" or branch_input == "5":
        not_eligible()

    else:
        not_eligible()

else:
    print("Enter a valid name!")




#This code was made for no lucrative purposes.

'This is an easy code for make a command to add in bulk multiples items to your Tf2autobot pricelist.json'

while True:
    print("What's the parameter you'll use? Please, only type the number or parameter's name.\n")
    question_1 = input(
                "1 --> Name\n"
                "2 --> Sku\n"
                "3 --> Defindex\n"
                "4 --> Item \n"
                "5 --> Id\n"
                "Write the parameter: ")
    if question_1.isdigit() and 1<= int(question_1) <= 5:
        break
    elif question_1.lower() in ['name', 'sku', 'defindex', 'item', 'id']:
        break
    else:
        print("\nPlease, enter a valid number/name parameter")

if question_1 == "1":
    question_1 = "name"
elif question_1 == "2":
    question_1 = "sku"
elif question_1 == "3":
    question_1 == "defindex"
elif question_1 == "4":
    question_1 = "item"
elif question_1 == "5":
    question_1 = "item"
else:
    question_1 = question_1.lower()
    
print(f"You have choosen: {question_1}")

print("#You can close this programm any time you want by typing \'close\'")


item_list = []
while True:

    item_1 = input(f"Type the item's {question_1}: ")

    if item_1.lower() == "close":
        break

    elif item_1 != "": 
        item_list.append(item_1)
        print(f"Item '{item_1}' added successfully!")

    else: 
        print("Please, type a valid item")
    

print("Here is your whole list: ")


print(f"!addbulk {question_1}={item_list[0]}")
for i in item_list[1:]:
    print(f"{question_1}={i}")
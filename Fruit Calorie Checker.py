print("Welcome to Fruit calorie Checker")

print("1 - Apple")
print("2 - Banana")
print("3 - Orange")
print("4 - Grapes")
print("5 - Strawberry")
print("6 - Mango")
print("7 - Peach")

def find_calories():
    fruit_cal = {
        "Apple" : 95,
        "Banana" : 111,
        "Orange" : 62,
        "Grapes" : 104,
        "Strawberry" : 49,
        "Mango" : 202,
        "Peach" : 59
}
    fruit = list(fruit_cal.keys())

    select = int(input("Enter your fruit number: "))

    if select >=1 and select <=7:
        selected_fruit = fruit[select-1]
        print(f"{selected_fruit} has {fruit_cal[selected_fruit]} calories")
    else:
        print("Please enter a valid number")

find_calories()









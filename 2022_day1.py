def calory_count(food):
    Calories = 0
    Max_Calories = 0
    for f in food:
        if (f != ''):
            Calories = Calories + int(f)
        else:
            if (Max_Calories < Calories):
                Max_Calories = Calories
                print(Max_Calories)
                Calories = 0
    return Max_Calories


input_file = open("day1input.txt", "r")
content = input_file.read()
food = content.split("\n")
print(calory_count(food))

input_file = open("day1_test.txt", "r")
content = input_file.read()
food = content.split("\n")
print(calory_count(food))
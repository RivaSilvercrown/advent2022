def calory_count(food):
    Calories = 0
    print(food)
    return Calories


input_file = open("day1input.txt", "r")
content = input_file.read()
food = content.split("\n")
print(calory_count(food))

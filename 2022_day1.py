#find the maximum amount of calories the elfs are carrying
def calory_count(food):
    Calories = 0
    Max_Calories = 0
    #check every element in food
    for f in food:
        #if the element is not empty, add its value to the calories count
        if (f != ''):
            Calories = Calories + int(f)
        #if the element is empty, check if the calories count is higher than the max calories count. If so, set the max calories count to the calories count.
        # Then reset the calories count to 0    
        else:
            if (Max_Calories < Calories):
                Max_Calories = Calories
                print(Max_Calories)
            Calories = 0
    return Max_Calories

#main function
def __main__():
    input_file = open("day1input.txt", "r")
    content = input_file.read()
    food = content.split("\n")
    print(calory_count(food))

    input_file = open("day1_test.txt", "r")
    content = input_file.read()
    food = content.split("\n")
    print(calory_count(food))

if __name__ == "__main__":
    __main__()
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

def top_three_calories(food):
    Calories = 0
    Max_Calories = [0,0,0]
    top_three = 0

    #check every element in food
    for f in food:

        #if the element is not empty, add its value to the calories count
        if (f != ''):
            Calories = Calories + int(f)

        #if the element is empty or it is the last elemento: check if the calories count is higher than the max calories count. 
        # If so, set the max calories count to the calories count.
        # Then reset the calories count to 0    
        if (f == '') or (f == food[-1]):
            print(food[-1])

            #check if the calories count is higher than any of the three max calories count. If so, set the lowest max calories count to the calories count.
            if (Max_Calories[0] < Calories) or (Max_Calories[1] < Calories) or (Max_Calories[2] < Calories):
                Max_Calories[0] = Calories
                #sort the list
                Max_Calories.sort()

            #reset the calories count to 0
            Calories = 0
    print(Max_Calories)
    #add the three highest calories count
    top_three=Max_Calories[0]+Max_Calories[1]+Max_Calories[2]
    return top_three

#main function
def __main__():
    input_file = open("day1input.txt", "r")
    content = input_file.read()
    food = content.split("\n")
    print(calory_count(food))

    input_file = open("day1input.txt", "r")
    content = input_file.read()
    food = content.split("\n")
    print(top_three_calories(food))

if __name__ == "__main__":
    __main__()
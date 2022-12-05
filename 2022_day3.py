def rucksacks(supplies):
    priority_sum = 0
    #mapping the priorities for different supplies
    priority = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }
    # check each rucksack
    for rucksack in supplies:
        #divide the rucksack into two parts
        r1 = rucksack[:len(rucksack)//2]
        r2 = rucksack[len(rucksack)//2:]
        
        found = 0

        for element in r1:
            #checks if the element is in the second rucksack and has not been found yet
            if (element in r2) and (found == 0):
                priority_sum = priority_sum + priority[element]
                e = element
                #the element in both parts is found
                found = 1

    return priority_sum

def __main__():
    input_file = open("day3input.txt", "r")
    content = input_file.read()
    supplies = content.split("\n")
    print(rucksacks(supplies))
    

    input_file = open("day3_test.txt", "r")
    content = input_file.read()
    supplies = content.split("\n")
    print(rucksacks(supplies))

if __name__ == "__main__":
    __main__()
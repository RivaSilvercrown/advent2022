def overlap(sections):
    overlapped = 0
    for i in range(len(sections)):
        S=sections[i].split(",")
        s0=S[0]
        s1=S[1]

        

def __main__():
    input_file = open("day3input.txt", "r")
    content = input_file.read()
    sections = content.split("\n")
    print(overlap(sections))
    #print(group_rucksack(supplies))
    

    input_file = open("day3_test.txt", "r")
    content = input_file.read()
    sections = content.split("\n")
    print(overlap(sections))
    #print(group_rucksack(supplies))

if __name__ == "__main__":
    __main__()
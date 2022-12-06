def overlap(sections):
    overlapped = 0
    for i in range(len(sections)):
        S=sections[i].split(",")
        s0= S[0].split("-")
        s1= S[1].split("-")

        #convert to int. If this step is not done, the result will be incorrect because it will compare strings
        s0[0] = int(s0[0])
        s0[1] = int(s0[1])
        s1[0] = int(s1[0])
        s1[1] = int(s1[1])

        if ((s0[0] <= s1[0] <= s0[1]) and (s0[0] <= s1[1] <= s0[1])) or ((s1[0] <= s0[0] <= s1[1]) and (s1[0] <= s0[1] <= s1[1])):
            overlapped = overlapped + 1
    return overlapped



def __main__():
    input_file = open("day4input.txt", "r")
    content = input_file.read()
    sections = content.split("\n")
    print(overlap(sections))
    #print(group_rucksack(supplies))
    

    input_file = open("day4_test.txt", "r")
    content = input_file.read()
    sections = content.split("\n")
    print(overlap(sections))
    #print(group_rucksack(supplies))

if __name__ == "__main__":
    __main__()
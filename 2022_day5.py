def crane(input):
    flag=''
    
    #get the crates stacks
    index = input.index('')

    #crates go from start to empty line
    crates = input[0:index]

    #moves go from empty line to end
    moves = input[index+1:]

    columns = crates[len(crates)-1]

    #number of columns is the array length plus one divided by 4.
    #we force an int because the result is a float
    num_columns = int((len(columns)+1)/4)

    #we traspose the crates array
    crates_T = [[crates[j][i] for j in range(len(crates))] for i in range(len(crates[0]))]
    
    #clean empty rows (they contain spaces or brackets)
    removable = ['[',']']
    crates_T = [x for x in crates_T if not any(el in x for el in removable)]
    crates2 = [[0]*len(crates_T[0])]*len(crates_T)
    print(crates)
    for i in range(len(crates_T)):
        for j in range(len(crates_T[i])):
            crates2[i][j] = crates_T[i][len(crates_T[i])-j-1]
    print(crates2)
    #set crates arrays
    #for i in range(len(crates)):
    #    for j in range(num_columns):
            
    #        crates[i][columns.index(str(j+1))]
            
    

    #print(crates)
    #print(columns.index('9'))
    #print(crates[0].index('D'))

    return flag


def __main__():
    input_file = open("day5input.txt", "r")
    content = input_file.read()
    crates = content.split("\n")
    #print(crane(crates))
    #print(crane(crates))
    

    input_file = open("day5_test.txt", "r")
    content = input_file.read()
    crates = content.split("\n")
    print(crane(crates))
    print(crane(crates))

if __name__ == "__main__":
    __main__()
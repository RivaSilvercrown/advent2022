#rock paper scissors
def RPS(strategy):
    score = 0
    for i in range(0, len(strategy)):
        game = strategy[i].split(" ")
        #for the opponent: rock = A, paper = B, scissors = C
        #for me : rock = X, paper = Y, scissors = Z
        #rock beats scissors
        #scissors beats paper
        #paper beats rock
        #if both players choose the same, it's a tie
        if (game[0] == 'A') and (game[1] == 'Y'):
            #paper beats rock
            score = score + 6
        elif (game[0] == 'B') and (game[1] == 'Z'):
            #scissors beats paper
            score = score + 6
        elif (game[0] == 'C') and (game[1] == 'X'):
            #rock beats scissors
            score = score + 6
        elif ((game[0] == 'A') and (game[1] == 'X')) or ((game[0] == 'B') and (game[1] == 'Y')) or ((game[0] == 'C') and (game[1] == 'Z')):
            #tie
            score = score + 3
        if (game[1]=='X'):
            #I played rock
            score = score + 1
        elif (game[1]=='Y'):
            #I played paper
            score = score + 2
        elif (game[1]=='Z'):
            #I played scissors
            score = score + 3
            
    return score



def __main__():
    input_file = open("day2input.txt", "r")
    content = input_file.read()
    strategy = content.split("\n")
    print(RPS(strategy))

if __name__ == "__main__":
    __main__()
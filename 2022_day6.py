def marker_detector(stream):

    # program sliding window of width 4
    marker = -1
    for i in range(len(stream)-3):
        # check if the window is a marker (all characters are different)
        if (stream[i] != stream[i+1]) and (stream[i] != stream[i+2]) and (stream[i] != stream[i+3]) \
            and (stream[i+1] != stream[i+2]) and (stream[i+1] != stream[i+3]) \
            and (stream[i+2] != stream[i+3]):
            # if it is, return the marker: last character position in the window
            return i+4
    return marker

def __main__():
    input_file = open("day6input.txt", "r")
    stream = input_file.read()
    print("Result: ")
    print(marker_detector(stream))

    

    input_file = open("day6_test.txt", "r")
    stream = input_file.read()
    print("Test: ")
    print(marker_detector(stream))

if __name__ == "__main__":
    __main__()
def marker_detector(stream: str, n: int):

    # program sliding window of width n

    for i in range(len(stream[n - 1:])):
        # check that all characters are different
        #a set must have all different elements
        s = set(stream[i:i + n])
        if n == len(s):
            return i + n

    return None

def __main__():
    input_file = open("day6input.txt", "r")
    stream = input_file.read()
    print("Result: ")
    print(marker_detector(stream, 4))
    print(marker_detector(stream, 14))

    

    input_file = open("day6_test.txt", "r")
    stream = input_file.read()
    print("Test: ")
    print(marker_detector(stream, 4))
    print(marker_detector(stream, 14))

if __name__ == "__main__":
    __main__()
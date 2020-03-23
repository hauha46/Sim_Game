
import pickle
import numpy as np
import math
import random

triangles = [['a', 'c', 'k'], ['a', 'i', 'o'], ['a', 'm', 'j'], ['a', 'b', 'g'], ['k', 'e', 'o'], ['k', 'h', 'j'],
             ['k', 'n', 'b'], ['o', 'f', 'j']
    , ['o', 'l', 'b'], ['j', 'd', 'b'], ['c', 'e', 'i'], ['c', 'h', 'm'], ['c', 'g', 'n'], ['i', 'f', 'm'],
             ['i', 'l', 'g'], ['m', 'd', 'g']
    , ['e', 'f', 'h'], ['e', 'l', 'n'], ['l', 'd', 'f'], ['h', 'n', 'd']]
# Initialize empty var
available_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
fixed_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
map_input = [0] * 15
hidden = []
output = []
picked_line_com = []
picked_line_man = []
resultString =''
def checkTriangles(picked):
    ret = False
    for i in range(len(triangles)):
        if set(triangles[i]).issubset(set(picked)):
            ret = True
    return ret


class Hidden:
    def __init__(self):
        self.den = []
        self.th = np.random.random()
        self.axonValue = 0
        self.axon = 0
        for i in range(15):
            self.den.append(np.random.random())


class Output:
    def __init__(self):
        self.den = []
        self.th = np.random.random()
        self.axonValue = 0
        self.axon = 0
        for i in range(7):
            self.den.append(np.random.random())

def search_line():
    global picked_line_com, resultString
    # Choose line based on triangles
    for i in range(len(available_lines)):
        picked_line_com.append(available_lines[i])
        #print("Computer picked: " + str(available_lines[i]))
        resultString += "Computer picked: " + str(available_lines[i]) + "\n" 
        for j in range(len(triangles)):
            if not set(triangles[j]).issubset(set(picked_line_com)):
                return available_lines[i]
        picked_line_com.remove(available_lines[i])
    return available_lines.pop(0)

def display_line(input):
    next_line = search_line()
    available_lines.remove(next_line)
    if next_line == 'a':
        input[0] = 1
    elif next_line == 'b':
        input[1] = 1
    elif next_line == 'c':
        input[2] = 1
    elif next_line == 'd':
        input[3] = 1
    elif next_line == 'e':
        input[4] = 1
    elif next_line == 'f':
        input[5] = 1
    elif next_line == 'g':
        input[6] = 1
    elif next_line == 'h':
        input[7] = 1
    elif next_line == 'i':
        input[8] = 1
    elif next_line == 'j':
        input[9] = 1
    elif next_line == 'k':
        input[10] = 1
    elif next_line == 'l':
        input[11] = 1
    elif next_line == 'm':
        input[12] = 1
    elif next_line == 'n':
        input[13] = 1
    elif next_line == 'o':
        input[14] = 1
    return input


def training(input, hidden, output, alpha=0.9, ):
    global fixed_lines, resultString
    # dendrite 2d list
    ddo = [[0] * len(hidden)] * len(output)
    ddh = [[0] * len(output)] * len(hidden)
    # error init
    errorOutput = [0] * len(output)
    axonErrorOutput = [0] * len(output)
    errorHidden = [0] * len(hidden)
    # Propagate
    for i in range(len(hidden)):
        temp_sum = 0
        for j in range(len(input)):
            temp_sum += hidden[i].den[j] * input[j]
        hidden[i].axonValue = 1 / (1 + math.exp(0 - (temp_sum + hidden[i].th)))
        if (temp_sum > hidden[i].th):
            hidden[i].axon = 1
        else:
            hidden[i].axon = 0
    #print("Output")
    resultString += "Output \n"
    for i in range(len(output)):
        temp_sum = 0
        for j in range(len(hidden)):
            temp_sum += output[i].den[j] * hidden[j].axon
        output[i].axonValue = 1 / (1 + math.exp(0 - (temp_sum + output[i].th)))
        if (temp_sum > output[i].th):
            output[i].axon = 1
        else:
            output[i].axon = 0
        #print(fixed_lines[i] + ": " + str(output[i].axonValue))
        resultString += fixed_lines[i] + ": " + str(output[i].axonValue) + "\n"
    outputAxon = display_line(input)
    # Backpropagate
    for i in range(len(output)):
        errorOutput[i] = outputAxon[i] - output[i].axonValue
        axonErrorOutput[i] = (1 - output[i].axonValue) * output[i].axonValue * errorOutput[i]
        for j in range(len(hidden)):
            ddo[i][j] = axonErrorOutput[i] * output[i].den[j]
            errorHidden[j] = ddo[i][j] * hidden[j].axonValue * (1 - hidden[j].axonValue) + errorHidden[j]
            output[i].den[j] = output[i].den[j] + alpha * ddo[i][j]

        output[i].th += alpha * axonErrorOutput[i]

    for i in range(len(hidden)):
        for j in range(len(output)):
            ddh[i][j] = errorHidden[i] * hidden[i].den[j]
            hidden[i].den[j] += alpha * ddh[i][j]
        hidden[i].th += alpha * errorHidden[i]

    return outputAxon

def reset():
    global available_lines, picked_line_man, picked_line_com, hidden, output, resultString
    #print("Total moves picked by computer: " + str(picked_line_com))
    resultString += "Total moves picked by computer: " + str(picked_line_com) + "\n"
    picked_line_man = []
    picked_line_com = []
    available_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

def main():
    global hidden, output, map_input, resultString

    #Setup neural
    try:
        with open('hiddenNeurons', 'rb') as hiddenLoad:
            hidden = pickle.load(hiddenLoad)
        with open('outputNeurons', 'rb') as outputLoad:
            output = pickle.load(outputLoad)
    except(FileNotFoundError):
        for i in range(7):
            hidden.append(Hidden())
        for i in range(15):
            output.append(Output())

    count = 0
    # Functionality
    # Number of steps executing. A game can include from 3 to 7 steps
    for i in range(100):
        next_line = random.choice(available_lines)
        picked_line_man.append(next_line)
        available_lines.remove(next_line)
        if next_line == 'a':
            map_input[0] = 1
        elif next_line == 'b':
            map_input[1] = 1
        elif next_line == 'c':
            map_input[2] = 1
        elif next_line == 'd':
            map_input[3] = 1
        elif next_line == 'e':
            map_input[4] = 1
        elif next_line == 'f':
            map_input[5] = 1
        elif next_line == 'g':
            map_input[6] = 1
        elif next_line == 'h':
            map_input[7] = 1
        elif next_line == 'i':
            map_input[8] = 1
        elif next_line == 'j':
            map_input[9] = 1
        elif next_line == 'k':
            map_input[10] = 1
        elif next_line == 'l':
            map_input[11] = 1
        elif next_line == 'm':
            map_input[12] = 1
        elif next_line == 'n':
            map_input[13] = 1
        elif next_line == 'o':
            map_input[14] = 1
        if checkTriangles(picked_line_man):
            reset()
            #print("Game number: " + str(count) + "\n")
            resultString += "Game number: " + str(count) + "\n"
            count += 1
        else:
            training(map_input, hidden, output)
            if checkTriangles(picked_line_com):
                reset()
                #print("Game number: " + str(count) + "\n")
                resultString += "Game number: " + str(count) + "\n"
                count += 1

    with open('hiddenNeurons', 'wb') as hiddenLoad:
        pickle.dump(hidden, hiddenLoad)
    with open('outputNeurons', 'wb') as outputLoad:
        pickle.dump(output, outputLoad)
    text_file = open("output.txt", "wt")
    n = text_file.write(resultString)
    text_file.close()
if __name__ == '__main__':
    main()

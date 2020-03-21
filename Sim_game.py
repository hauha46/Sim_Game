from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import numpy as np
import math
import numpy

triangles = [['a','c','k'], ['a','i','o'], ['a','m','j'], ['a','b','g'], ['k', 'e', 'o'], ['k','h','j'], ['k','n','b'], ['o','f','j']
             , ['o','l','b'], ['j','d','b'], ['c','e','i'], ['c','h','m'], ['c', 'g', 'n'], ['i','f','m'], ['i', 'l', 'g'], ['m','d','g']
             , ['e','f','h'], ['e','l','n'], ['l','d','f'], ['h','n','d']]
# Initialize empty var
available_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']
fixed_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']


class Player:

    def __init__(self, mark):
        self.lines = []
        self.mark = mark

    def checkTriangles(self):
        ret = False
        for i in range (len(triangles)):
            if set(triangles[i]).issubset(set(self.lines)):
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

def choose_line(input,canvas):
    next_line = available_lines.pop(0)
    if next_line == 'a':
        canvas.create_line(75, 86, 150, 28, fill='red')
        input[0] = 1
    elif next_line == 'b':
        canvas.create_line(150, 28, 225, 86, fill='red')
        input[1] = 1
    elif next_line == 'c':
        canvas.create_line(75, 86, 75, 144, fill='red')
        input[2] = 1
    elif next_line == 'd':
        canvas.create_line(225, 86, 225, 144, fill='red')
        input[3] = 1
    elif next_line == 'e':
        canvas.create_line(75, 144, 150, 202, fill='red')
        input[4] = 1
    elif next_line == 'f':
        canvas.create_line(225, 144, 150, 202, fill='red')
        input[5] = 1
    elif next_line == 'g':
        canvas.create_line(75, 86, 225, 86, fill='red')
        input[6] = 1
    elif next_line == 'h':
        canvas.create_line(75, 144, 225, 144, fill='red')
        input[7] = 1
    elif next_line == 'i':
        canvas.create_line(75, 86, 150, 202, fill='red')
        input[8] = 1
    elif next_line == 'j':
        canvas.create_line(150, 28, 225, 144, fill='red')
        input[9] = 1
    elif next_line == 'k':
        canvas.create_line(150, 28, 75, 144, fill='red')
        input[10] = 1
    elif next_line == 'l':
        canvas.create_line(225, 86, 150, 202, fill='red')
        input[11] = 1
    elif next_line == 'm':
        canvas.create_line(75, 86, 225, 144, fill='red')
        input[12] = 1
    elif next_line == 'n':
        canvas.create_line(75, 144, 225, 86, fill='red')
        input[13] = 1
    elif next_line == 'o':
        canvas.create_line(150, 28, 150, 202, fill='red')
        input[14] = 1
    return input
def training(input, hidden, output, canvas, alpha = 0.9,):
    #dendrite 2d list
    ddo = [[0]*len(hidden)]*len(output)
    ddh = [[0] * len(output)] * len(hidden)

    # error init
    errorOutput = [0]*len(output)
    axonErrorOutput = [0] * len(output)
    errorHidden = [0]*len(hidden)
    #Propagate
    for i in range (len(hidden)):
        temp_sum = 0
        for j in range (len(input)):
            temp_sum += hidden[i].den[j] * input[j]
        print(temp_sum)
        hidden[i].axonValue = 1 / (1 + math.exp( 0-(temp_sum + hidden[i].th)))

        if (temp_sum > hidden[i].th):
            hidden[i].axon = 1
        else:
            hidden[i].axon = 0

    for i in range(len(output)):
        temp_sum = 0
        for j in range(len(hidden)):
            temp_sum += output[i].den[j] * hidden[j].axon
        output[i].axonValue = 1 / (1 + math.exp(0-(temp_sum + output[i].th)))
        if (temp_sum > output[i].th):
            output[i].axon = 1
        else:
            output[i].axon = 0
    outputAxon = choose_line(input, canvas)
    #Backpropagate
    for i in range(len(output)):
        errorOutput[i] = outputAxon[i] - output[i].axonValue
        axonErrorOutput[i] = (1- output[i].axonValue) * output[i].axonValue * errorOutput[i]
        for j in range (len(hidden)):
            ddo[i][j] = axonErrorOutput[i]*output[i].den[j]
            errorHidden[j] = ddo[i][j]*hidden[j].axonValue*(1-hidden[j].axonValue) + errorHidden[j]
            output[i].den[j] = output[i].den[j] + alpha * ddo[i][j]

        output[i].th += alpha * axonErrorOutput[i]


    for i in range(len(hidden)):
        for j in range(len(output)):
            ddh[i][j] = errorHidden[i]*hidden[i].den[j]
            hidden[i].den[j] += alpha * ddh[i][j]
        hidden[i].th += alpha * errorHidden[i]

    return outputAxon
def main():
    global step
    #Access the file to take input
    try:
        with open('record.stm', 'rb') as record:
            step = pickle.load(record)
    except(FileNotFoundError):
        print()

    #Player Setup
    p1 = Player("Player 1")

    #Setup neurons
    map_input= [0]*15
    hidden = []
    output = []
    for i in range(7):
        hidden.append(Hidden())
    for i in range(15):
        output.append(Output())

    # Layout with Tkinter
    window = Tk()
    window.title("SIM")
    window.geometry('300x300')
    input = Entry(window,width = 5)
    input.place(x = 90, y = 250)
    canvas = Canvas(window, width=300, height=230, background='white')
    canvas.place(x=0, y=0)
    label = Label(window, text="Player 1")
    label.place(x=20, y=250)
    canvas.create_line(75, 86, 150, 28, fill='gray', dash=(4, 2))
    canvas.create_line(150, 28, 225, 86, fill='gray', dash=(4, 2))
    canvas.create_line(75, 86, 75, 144, fill='gray', dash=(4, 2))
    canvas.create_line(225, 86, 225, 144, fill='gray', dash=(4, 2))
    canvas.create_line(75, 144, 150, 202, fill='gray', dash=(4, 2))
    canvas.create_line(225, 144, 150, 202, fill='gray', dash=(4, 2))
    canvas.create_line(75, 86, 225, 86, fill='gray', dash=(4, 2))
    canvas.create_line(75, 86, 150, 202, fill='gray', dash=(4, 2)   )
    canvas.create_line(75, 144, 225, 144, fill='gray', dash=(4, 2))
    canvas.create_line(150, 28, 225, 144, fill='gray', dash=(4, 2))
    canvas.create_line(150, 28, 75, 144, fill='gray', dash=(4, 2))
    canvas.create_line(225, 86, 150, 202, fill='gray', dash=(4, 2))
    canvas.create_line(75, 86, 225, 144, fill='gray', dash=(4, 2))
    canvas.create_line(75, 144, 225, 86, fill='gray', dash=(4, 2))
    canvas.create_line(150, 28, 150, 202, fill='gray', dash=(4, 2))


    # Functionality

    def reset():
        canvas.delete("all")
        label = Label(window, text="Player 1")
        label.place(x=20, y=250)
        canvas.create_line(75, 86, 150, 28, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 225, 86, fill='gray', dash=(4, 2))
        canvas.create_line(75, 86, 75, 144, fill='gray', dash=(4, 2))
        canvas.create_line(225, 86, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(75, 144, 150, 202, fill='gray', dash=(4, 2))
        canvas.create_line(225, 144, 150, 202, fill='gray', dash=(4, 2))
        canvas.create_line(75, 86, 225, 86, fill='gray', dash=(4, 2))
        canvas.create_line(75, 86, 150, 202, fill='gray', dash=(4, 2)   )
        canvas.create_line(75, 144, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 75, 144, fill='gray', dash=(4, 2))
        canvas.create_line(225, 86, 150, 202, fill='gray', dash=(4, 2))
        canvas.create_line(75, 86, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(75, 144, 225, 86, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 150, 202, fill='gray', dash=(4, 2))
        p1.lines = []
         global selected, selected_lines, available_lines
        selected_lines = []
        available_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        selected = []
    def player_choose_lines():

        color = 'blue'
        label = Label(window, text="Player 1")
        label.place(x=20,y = 250)
        player = p1

        if input.get() == 'a':
            canvas.create_line(75, 86, 150, 28, fill=color)
            player.lines.append('a')
            available_lines.remove('a')
            map_input[0] = 1
        elif input.get() == 'b':
            canvas.create_line(150, 28, 225, 86, fill=color)    
            player.lines.append('b')
            available_lines.remove('b')
            map_input[1] = 1
        elif input.get() == 'c':
            canvas.create_line(75, 86, 75, 144, fill=color)
            player.lines.append('c')
            available_lines.remove('c')
            map_input[2] = 1
        elif input.get() == 'd':
            canvas.create_line(225, 86, 225, 144, fill=color)
            player.lines.append('d')
            available_lines.remove('d')
            map_input[3] = 1
        elif input.get() == 'e':
            canvas.create_line(75, 144, 150, 202, fill=color)
            player.lines.append('e')
            available_lines.remove('e')
            map_input[4] = 1
        elif input.get() == 'f':
            canvas.create_line(225, 144, 150, 202, fill=color)
            player.lines.append('f')
            available_lines.remove('f')
            map_input[5] = 1
        elif input.get() == 'g':
            canvas.create_line(75, 86, 225, 86, fill=color)
            player.lines.append('g')
            available_lines.remove('g')
            map_input[6] = 1
        elif input.get() == 'h':
            canvas.create_line(75, 144, 225, 144, fill=color)
            player.lines.append('h')
            available_lines.remove('h')
            map_input[7] = 1
        elif input.get() == 'i':
            canvas.create_line(75, 86, 150, 202, fill=color)
            player.lines.append('i')
            available_lines.remove('i')
            map_input[8] = 1
        elif input.get() == 'j':
            canvas.create_line(150, 28, 225, 144, fill=color)
            player.lines.append('j')
            available_lines.remove('j')
            map_input[9] = 1
        elif input.get() == 'k':
            canvas.create_line(150, 28, 75, 144, fill=color)
            player.lines.append('k')
            available_lines.remove('k')
            map_input[10] = 1
        elif input.get() == 'l':
            canvas.create_line(225, 86, 150, 202, fill=color)
            player.lines.append('l')
            available_lines.remove('l')
            map_input[11] = 1
        elif input.get() == 'm':
            canvas.create_line(75, 86, 225, 144, fill=color)
            player.lines.append('m')
            available_lines.remove('m')
            map_input[12] = 1
        elif input.get() == 'n':
            canvas.create_line(75, 144, 225, 86, fill=color)
            player.lines.append('n')
            available_lines.remove('n')
            map_input[13] = 1
        elif input.get() == 'o':
            canvas.create_line(150, 28, 150, 202, fill=color)
            player.lines.append('o')
            available_lines.remove('o')
            map_input[14] = 1

        if player.checkTriangles():
            messagebox.showinfo("Result",player.mark + " lose")
        else:
            computer_choose_lines()
        # Computer choose line
    def computer_choose_lines():
        training(map_input, hidden, output,canvas)

    # Show and action
    choose_button = Button(window, text = "Choose line", command = player_choose_lines)
    choose_button.place(x = 130, y = 250)

    reset_button = Button(window, text="Reset Game", command=reset)
    reset_button.place(x=220, y=250)

    path = "Helper.png"

    img = ImageTk.PhotoImage(Image.open(path).resize((774,683), Image.ANTIALIAS))

    top = Toplevel(window, bg='red')
    top.geometry('774x683')
    top.title("Instruction")
    image = Label(top, image = img)
    image.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()


if __name__ == '__main__':
    main()

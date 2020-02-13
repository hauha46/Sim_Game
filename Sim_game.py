from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import numpy

triangles = [['a','c','k'], ['a','i','o'], ['a','m','j'], ['a','b','g'], ['k', 'e', 'o'], ['k','h','j'], ['k','n','b'], ['o','f','j']
             , ['o','l','b'], ['j','d','b'], ['c','e','i'], ['c','h','m'], ['c', 'g', 'n'], ['i','f','m'], ['i', 'l', 'g'], ['m','d','g']
             , ['e','f','h'], ['e','l','n'], ['l','d','f'], ['h','n','d']]
# Initialize empty var
available_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']
fixed_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']
selected = [] 
selected_lines = [] 
step1 ={}
step2 ={}
step3 ={}
step4 ={}
step5 ={}
step6 ={}
step7 ={}
step = []
step.append(step1)
step.append(step2)
step.append(step3)
step.append(step4)
step.append(step5)
step.append(step6)
step.append(step7)

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
def find_max(arr):
    max = 0
    index = 0
    for i in arr:
        if i.startswith(selected[-1])and i[-1] in available_lines:
            if arr.get(i) > max:
                max = arr.get(i)
                index = i
    return index

def find_max_init(arr):
    max = 0
    index = 0
    for i in arr:
        if arr.get(i) > max and i[-1] in available_lines:
            max = arr.get(i)
            index = i
    return index

def initialize(step):
    try:
        for i in range(len(fixed_lines)):
            if fixed_lines[i] not in selected[-1]:
                step[selected[-1] + fixed_lines[i]] = 1 / (len(fixed_lines) - len(selected[-1]))
    except(IndexError):
        for i in range(len(fixed_lines)):
            step[fixed_lines[i]] = 1 / len(fixed_lines)

def reward(step, move):
    pre_move = move[:-1]
    possible_move =[]
    for i in step:
        if i.startswith(pre_move):
            possible_move.append(i)
    step[move] = step.get(move) * 2
    possible_move.remove(move)
    for i in range (len(possible_move)):
        step[possible_move[i]] = step.get(possible_move[i]) - (step.get(move)/2)/(len(possible_move))

def punish(step, move):
    pre_move = move[:-1]
    possible_move = []
    for i in step:
        if i.startswith(pre_move):
            possible_move.append(i)
    step[move] = step.get(move) / 2
    possible_move.remove(move)

    for i in range(len(possible_move)):
        step[possible_move[i]] = step.get(possible_move[i]) + (step.get(move)) / len(possible_move)

def find_in_step(step):
    found = False

    if step == {}:
        initialize(step)
        return find_max_init(step)
    for i in step:
        if i.startswith(selected[-1]):
            found = True
    if (found):
        return find_max(step)
    else:
        initialize(step)
        return find_max(step)

def choose_next_line():
    if selected == []:
        if step[0] == {}: initialize(step[0])
        return find_max_init(step[0])
    else:
        if len(selected) == 1:
            return find_in_step(step[1])
        elif len(selected) == 2:
            return find_in_step(step[2])
        elif len(selected) == 3:
            return find_in_step(step[3])
        elif len(selected) == 4:
            return find_in_step(step[4])
        elif len(selected) == 5:
            return find_in_step(step[5])
        elif len(selected) == 6:
            return find_in_step(step[6])

def main():
    global step
    #Access the file to take input
    try:
        with open('record.stm', 'rb') as record:
            step = pickle.load(record)
    except(FileNotFoundError):
        print()
    #print(step)
    #Player Setup
    p1 = Player("Player 1")

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

    def reset2():
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
        elif input.get() == 'b':
            canvas.create_line(150, 28, 225, 86, fill=color)
            player.lines.append('b')
            available_lines.remove('b')
        elif input.get() == 'c':
            canvas.create_line(75, 86, 75, 144, fill=color)
            player.lines.append('c')
            available_lines.remove('c')
        elif input.get() == 'd':
            canvas.create_line(225, 86, 225, 144, fill=color)
            player.lines.append('d')
            available_lines.remove('d')
        elif input.get() == 'e':
            canvas.create_line(75, 144, 150, 202, fill=color)
            player.lines.append('e')
            available_lines.remove('e')
        elif input.get() == 'f':
            canvas.create_line(225, 144, 150, 202, fill=color)
            player.lines.append('f')
            available_lines.remove('f')
        elif input.get() == 'g':
            canvas.create_line(75, 86, 225, 86, fill=color)
            player.lines.append('g')
            available_lines.remove('g')
        elif input.get() == 'h':
            canvas.create_line(75, 144, 225, 144, fill=color)
            player.lines.append('h')
            available_lines.remove('h')
        elif input.get() == 'i':
            canvas.create_line(75, 86, 150, 202, fill=color)
            player.lines.append('i')
            available_lines.remove('i')
        elif input.get() == 'j':
            canvas.create_line(150, 28, 225, 144, fill=color)
            player.lines.append('j')
            available_lines.remove('j')
        elif input.get() == 'k':
            canvas.create_line(150, 28, 75, 144, fill=color)
            player.lines.append('k')
            available_lines.remove('k')
        elif input.get() == 'l':
            canvas.create_line(225, 86, 150, 202, fill=color)
            player.lines.append('l')
            available_lines.remove('l')
        elif input.get() == 'm':
            canvas.create_line(75, 86, 225, 144, fill=color)
            player.lines.append('m')
            available_lines.remove('m')
        elif input.get() == 'n':
            canvas.create_line(75, 144, 225, 86, fill=color)
            player.lines.append('n')
            available_lines.remove('n')
        elif input.get() == 'o':
            canvas.create_line(150, 28, 150, 202, fill=color)
            player.lines.append('o')
            available_lines.remove('o')

        global step
        if player.checkTriangles():
            messagebox.showinfo("Result",player.mark + " lose")
            for i in range(len(selected)):
                reward(step[i], selected[i])
            with open('record.stm', 'wb') as record:
                pickle.dump(step,record)
        else:
            computer_choose_lines()
            print(step)

    def computer_choose_lines():
        line = choose_next_line()
        selected.append(line)
        selected_lines.append(line[-1])
        # print(line[-1])
        # print(available_lines)
        available_lines.remove(line[-1])


        if line[-1] == 'a':
            canvas.create_line(75, 86, 150, 28, fill='red')
        elif line[-1] == 'b':
            canvas.create_line(150, 28, 225, 86, fill='red')
        elif line[-1] == 'c':
            canvas.create_line(75, 86, 75, 144, fill='red')
        elif line[-1] == 'd':
            canvas.create_line(225, 86, 225, 144, fill='red')
        elif line[-1] == 'e':
            canvas.create_line(75, 144, 150, 202, fill='red')
        elif line[-1] == 'f':
            canvas.create_line(225, 144, 150, 202, fill='red')
        elif line[-1] == 'g':
            canvas.create_line(75, 86, 225, 86, fill='red')
        elif line[-1] == 'h':
            canvas.create_line(75, 144, 225, 144, fill='red')
        elif line[-1] == 'i':
            canvas.create_line(75, 86, 150, 202, fill='red')
        elif line[-1] == 'j':
            canvas.create_line(150, 28, 225, 144, fill='red')
        elif line[-1] == 'k':
            canvas.create_line(150, 28, 75, 144, fill='red')
        elif line[-1] == 'l':
            canvas.create_line(225, 86, 150, 202, fill='red')
        elif line[-1] == 'm':
            canvas.create_line(75, 86, 225, 144, fill='red')
        elif line[-1] == 'n':
            canvas.create_line(75, 144, 225, 86, fill='red')
        elif line[-1] == 'o':
            canvas.create_line(150, 28, 150, 202, fill='red')


        ret = False
        for i in range(len(triangles)):
            if set(triangles[i]).issubset(set(selected_lines)):
                ret = True
        if ret:
            messagebox.showinfo("Player 1 wins")
            for i in range(len(selected)):
                punish(step[i], selected[i])
            with open('record.stm', 'wb') as record:
                pickle.dump(step, record)


    # Show and action
    choose_button = Button(window, text = "Choose line", command = player_choose_lines)
    choose_button.place(x = 130, y = 250)

    reset_button = Button(window, text="Reset Game", command=reset2)
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

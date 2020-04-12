from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sys
sys.setrecursionlimit(2000)
import pickle
import numpy as np
import math

triangles = [['a', 'c', 'k'], ['a', 'i', 'o'], ['a', 'm', 'j'], ['a', 'b', 'g'], ['k', 'e', 'o'], ['k', 'h', 'j'],
             ['k', 'n', 'b'], ['o', 'f', 'j']
    , ['o', 'l', 'b'], ['j', 'd', 'b'], ['c', 'e', 'i'], ['c', 'h', 'm'], ['c', 'g', 'n'], ['i', 'f', 'm'],
             ['i', 'l', 'g'], ['m', 'd', 'g']
    , ['e', 'f', 'h'], ['e', 'l', 'n'], ['l', 'd', 'f'], ['h', 'n', 'd']]
# Initialize empty var
available_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
fixed_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
player_lines = []
machine_lines = []

def checkTriangles(lines):
    for i in range(len(triangles)):
        if set(triangles[i]).issubset(set(lines)):
            return True
    return False

def minimax(depth, isMaximizing):
    print(available_lines)
    if checkTriangles(player_lines):
        return 100 - depth
    if checkTriangles(machine_lines):
        return -100 + depth

    if (isMaximizing):
        best_score = -9999999999
        for i in range(len(available_lines)):
            line = available_lines.pop(i)
            machine_lines.append(line)
            line_score = minimax(depth + 1, False)
            machine_lines.remove(line)
            available_lines.insert(i, line)
            if (line_score > best_score):
                best_score = line_score
        return best_score
    else:
        best_score = 9999999999
        for i in range(len(available_lines)):
            line = available_lines.pop(i)
            player_lines.append(line)
            line_score = minimax(depth + 1, True)
            player_lines.remove(line)
            available_lines.insert(i, line)
            if (line_score < best_score):
                best_score = line_score
        return best_score
def choose_line():
    best_score = -999999999999
    line = None
    # Choose line based on triangles
    for i in range(len(available_lines)):
        line = available_lines.pop(i)
        machine_lines.append(line)
        line_score = minimax(0, False)
        machine_lines.remove(line)
        available_lines.insert(i,line)
        if (line_score > best_score ):
            best_score = line_score
            line = available_lines[i]
    return line

def display_line(canvas):
    next_line = choose_line()
    available_lines.remove(next_line)
    if next_line == 'a':
        canvas.create_line(75, 86, 150, 28, fill='red')
    elif next_line == 'b':
        canvas.create_line(150, 28, 225, 86, fill='red')
    elif next_line == 'c':
        canvas.create_line(75, 86, 75, 144, fill='red')
    elif next_line == 'd':
        canvas.create_line(225, 86, 225, 144, fill='red')
    elif next_line == 'e':
        canvas.create_line(75, 144, 150, 202, fill='red')
    elif next_line == 'f':
        canvas.create_line(225, 144, 150, 202, fill='red')
    elif next_line == 'g':
        canvas.create_line(75, 86, 225, 86, fill='red')
    elif next_line == 'h':
        canvas.create_line(75, 144, 225, 144, fill='red')
    elif next_line == 'i':
        canvas.create_line(75, 86, 150, 202, fill='red')
    elif next_line == 'j':
        canvas.create_line(150, 28, 225, 144, fill='red')
    elif next_line == 'k':
        canvas.create_line(150, 28, 75, 144, fill='red')
    elif next_line == 'l':
        canvas.create_line(225, 86, 150, 202, fill='red')
    elif next_line == 'm':
        canvas.create_line(75, 86, 225, 144, fill='red')
    elif next_line == 'n':
        canvas.create_line(75, 144, 225, 86, fill='red')
    elif next_line == 'o':
        canvas.create_line(150, 28, 150, 202, fill='red')


def main():

    # Layout with Tkinter
    window = Tk()
    window.title("SIM")
    window.geometry('300x300')
    input = Entry(window, width=5)
    input.place(x=90, y=250)
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
    canvas.create_line(75, 86, 150, 202, fill='gray', dash=(4, 2))
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
        canvas.create_line(75, 86, 150, 202, fill='gray', dash=(4, 2))
        canvas.create_line(75, 144, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 75, 144, fill='gray', dash=(4, 2))
        canvas.create_line(225, 86, 150, 202, fill='gray', dash=(4, 2))
        canvas.create_line(75, 86, 225, 144, fill='gray', dash=(4, 2))
        canvas.create_line(75, 144, 225, 86, fill='gray', dash=(4, 2))
        canvas.create_line(150, 28, 150, 202, fill='gray', dash=(4, 2))

        global picked_line, available_lines
        available_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        picked_line = []

    def player_choose_lines():

        color = 'blue'
        label = Label(window, text="Player 1")
        label.place(x=20, y=250)

        move = input.get()

        if (move not in available_lines):
            messagebox.showinfo("Line not available")
        else:
            player_lines.append(move)
            available_lines.remove(move)
            if move == 'a':
                canvas.create_line(75, 86, 150, 28, fill=color)
            elif move == 'b':
                canvas.create_line(150, 28, 225, 86, fill=color)
            elif move == 'c':
                canvas.create_line(75, 86, 75, 144, fill=color)
            elif move == 'd':
                canvas.create_line(225, 86, 225, 144, fill=color)
            elif move == 'e':
                canvas.create_line(75, 144, 150, 202, fill=color)
            elif move == 'f':
                canvas.create_line(225, 144, 150, 202, fill=color)
            elif move == 'g':
                canvas.create_line(75, 86, 225, 86, fill=color)
            elif move == 'h':
                canvas.create_line(75, 144, 225, 144, fill=color)
            elif move == 'i':
                canvas.create_line(75, 86, 150, 202, fill=color)
            elif move == 'j':
                canvas.create_line(150, 28, 225, 144, fill=color)
            elif move == 'k':
                canvas.create_line(150, 28, 75, 144, fill=color)
            elif move == 'l':
                canvas.create_line(225, 86, 150, 202, fill=color)
            elif move == 'm':
                canvas.create_line(75, 86, 225, 144, fill=color)
            elif move == 'n':
                canvas.create_line(75, 144, 225, 86, fill=color)
            elif move == 'o':
                canvas.create_line(150, 28, 150, 202, fill=color)
            if checkTriangles(player_lines):
                messagebox.showinfo("Result: Player lose")
                reset()
            else:
                computer_choose_lines()

    # Computer choose line
    def computer_choose_lines():
        choose_line()
        if checkTriangles(machine_lines):
            messagebox.showinfo("Result: Computer lose")
            reset()

    # Show and action
    choose_button = Button(window, text="Choose line", command=player_choose_lines)
    choose_button.place(x=130, y=250)

    reset_button = Button(window, text="Reset Game", command=reset)
    reset_button.place(x=220, y=250)

    path = "Helper.png"

    img = ImageTk.PhotoImage(Image.open(path).resize((774, 683), Image.ANTIALIAS))

    top = Toplevel(window, bg='red')
    top.geometry('774x683')
    top.title("Instruction")
    image = Label(top, image=img)
    image.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()


if __name__ == '__main__':
    main()

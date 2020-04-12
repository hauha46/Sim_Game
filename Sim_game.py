from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sys
sys.setrecursionlimit(2000)

triangles = [['a', 'c', 'k'], ['a', 'i', 'o'], ['a', 'm', 'j'], ['a', 'b', 'g'], ['k', 'e', 'o'], ['k', 'h', 'j'],
             ['k', 'n', 'b'], ['o', 'f', 'j']
    , ['o', 'l', 'b'], ['j', 'd', 'b'], ['c', 'e', 'i'], ['c', 'h', 'm'], ['c', 'g', 'n'], ['i', 'f', 'm'],
             ['i', 'l', 'g'], ['m', 'd', 'g']
    , ['e', 'f', 'h'], ['e', 'l', 'n'], ['l', 'd', 'f'], ['h', 'n', 'd']]
# Initialize empty var
all_lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
fixed_lines = [0]*15
player_lines = []
machine_lines = []

def checkTriangles(lines):
    for i in range(len(triangles)):
        if set(triangles[i]).issubset(set(lines)):
            return True
    return False

def minimax(depth, isMaximizing, alpha, beta):
    if checkTriangles(player_lines):
        return 100 - depth
    if checkTriangles(machine_lines):
        return -100 + depth

    if isMaximizing:
        best_score = -9999999999
        for i in range(len(fixed_lines)):
            if fixed_lines[i] == 0:
                fixed_lines[i] = 1
                machine_lines.append(all_lines[i])
                line_score = minimax(depth + 1, False, alpha, beta)
                machine_lines.remove(all_lines[i])
                fixed_lines[i] = 0
                if line_score > best_score:
                    best_score = line_score
                if line_score > alpha:
                    alpha = line_score
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 9999999999
        for i in range(len(fixed_lines)):
            if fixed_lines[i] == 0:
                fixed_lines[i] = 1
                player_lines.append(all_lines[i])
                line_score = minimax(depth + 1, True, alpha, beta)
                player_lines.remove(all_lines[i])
                fixed_lines[i] = 0
                if line_score < best_score:
                    best_score = line_score
                if line_score < beta:
                    beta = line_score
                if beta <= alpha:
                    break
        return best_score
def choose_line():
    best_score = -999999999999
    line = None
    # Choose line based on triangles
    for i in range(len(fixed_lines)):
        if fixed_lines[i] == 0:
            fixed_lines[i] = 1
            machine_lines.append(all_lines[i])
            line_score = minimax(0, True, -99999, 99999)
            print(line_score)
            machine_lines.remove(all_lines[i])
            fixed_lines[i] = 0
            if (line_score > best_score ):
                best_score = line_score
                line = all_lines[i]
    return line

def display_line(canvas):
    next_line = choose_line()
    if next_line == 'a':
        fixed_lines[0] = 1
        canvas.create_line(75, 86, 150, 28, fill='red')
    elif next_line == 'b':
        fixed_lines[1] = 1
        canvas.create_line(150, 28, 225, 86, fill='red')
    elif next_line == 'c':
        fixed_lines[2] = 1
        canvas.create_line(75, 86, 75, 144, fill='red')
    elif next_line == 'd':
        fixed_lines[3] = 1
        canvas.create_line(225, 86, 225, 144, fill='red')
    elif next_line == 'e':
        fixed_lines[4] = 1
        canvas.create_line(75, 144, 150, 202, fill='red')
    elif next_line == 'f':
        fixed_lines[5] = 1
        canvas.create_line(225, 144, 150, 202, fill='red')
    elif next_line == 'g':
        fixed_lines[6] = 1
        canvas.create_line(75, 86, 225, 86, fill='red')
    elif next_line == 'h':
        fixed_lines[7] = 1
        canvas.create_line(75, 144, 225, 144, fill='red')
    elif next_line == 'i':
        fixed_lines[8] = 1
        canvas.create_line(75, 86, 150, 202, fill='red')
    elif next_line == 'j':
        fixed_lines[9] = 1
        canvas.create_line(150, 28, 225, 144, fill='red')
    elif next_line == 'k':
        fixed_lines[10] = 1
        canvas.create_line(150, 28, 75, 144, fill='red')
    elif next_line == 'l':
        fixed_lines[11] = 1
        canvas.create_line(225, 86, 150, 202, fill='red')
    elif next_line == 'm':
        fixed_lines[12] = 1
        canvas.create_line(75, 86, 225, 144, fill='red')
    elif next_line == 'n':
        fixed_lines[13] = 1
        canvas.create_line(75, 144, 225, 86, fill='red')
    elif next_line == 'o':
        fixed_lines[14] = 1
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


    def player_choose_lines():

        color = 'blue'
        label = Label(window, text="Player")
        label.place(x=20, y=250)

        move = input.get()

        if (move not in all_lines):
            messagebox.showinfo("Line not available")
        else:
            player_lines.append(move)
            if move == 'a':
                fixed_lines[0] = 1
                canvas.create_line(75, 86, 150, 28, fill=color)
            elif move == 'b':
                fixed_lines[1] = 1
                canvas.create_line(150, 28, 225, 86, fill=color)
            elif move == 'c':
                fixed_lines[2] = 1
                canvas.create_line(75, 86, 75, 144, fill=color)
            elif move == 'd':
                fixed_lines[3] = 1
                canvas.create_line(225, 86, 225, 144, fill=color)
            elif move == 'e':
                fixed_lines[4] = 1
                canvas.create_line(75, 144, 150, 202, fill=color)
            elif move == 'f':
                fixed_lines[5] = 1
                canvas.create_line(225, 144, 150, 202, fill=color)
            elif move == 'g':
                fixed_lines[6] = 1
                canvas.create_line(75, 86, 225, 86, fill=color)
            elif move == 'h':
                fixed_lines[7] = 1
                canvas.create_line(75, 144, 225, 144, fill=color)
            elif move == 'i':
                fixed_lines[8] = 1
                canvas.create_line(75, 86, 150, 202, fill=color)
            elif move == 'j':
                fixed_lines[9] = 1
                canvas.create_line(150, 28, 225, 144, fill=color)
            elif move == 'k':
                fixed_lines[10] = 1
                canvas.create_line(150, 28, 75, 144, fill=color)
            elif move == 'l':
                fixed_lines[11] = 1
                canvas.create_line(225, 86, 150, 202, fill=color)
            elif move == 'm':
                fixed_lines[12] = 1
                canvas.create_line(75, 86, 225, 144, fill=color)
            elif move == 'n':
                fixed_lines[13] = 1
                canvas.create_line(75, 144, 225, 86, fill=color)
            elif move == 'o':
                fixed_lines[14] = 1
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

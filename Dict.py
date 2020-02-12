available_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']
fixed_lines = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o']
selected = []
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

def find_max(arr):
    # TODO: check available lines to see if the max line has been picked/colored, then choose the next max available option
    max = 0
    index = 0
    for i in arr:
        if i.startswith(selected[-1]) and i[-1] in available_lines:
            if arr.get(i) > max:
                max = arr.get(i)
                index = i
    return index


def find_max_init(arr):
    max = 0
    index = 0
    for i in arr:
        if arr.get(i) > max:
            max = arr.get(i)
            index = i
    return index


def initialize(step):
    #TODO: make a temp array to store available character, so that it can prevent duplicated lines
    try:
        for i in range(len(available_lines)):
            step[selected[-1] + available_lines[i]] = 1 / len(available_lines)
    except(IndexError):
        for i in range(len(available_lines)):
            step[available_lines[i]] = 1 / len(available_lines)


def reward(step, move):
    pre_move = move[:-1]
    possible_move = []
    for i in step:
        if i.startswith(pre_move):
            possible_move.append(i)
    step[move] = step.get(move) * 2
    possible_move.remove(move)
    for i in range(len(possible_move)):
        step[possible_move[i]] = step.get(possible_move[i]) - (step.get(move) / 2) / (len(possible_move))


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
#step 1
available_lines.remove('o')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 2
available_lines.remove('b')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 3
available_lines.remove('d')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 4
available_lines.remove('f')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 5
available_lines.remove('j')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 6
available_lines.remove('k')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
#step 6
available_lines.remove('l')
line = choose_next_line()
selected.append(line);
available_lines.remove(line[-1])
print(available_lines)
print(selected)
print(step7)


print(step)
for i in range(len(selected)):
    reward(step[i], selected[i])

for i in range(len(selected)):
    punish(step[i],selected[i])

print(step)
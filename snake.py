import os
import keyboard
import time
import random
#inchalla il va se manger la queue
background = {}
snake = '0' #░
pomme = '$'
long = 50
haut = 25
def position_x(x):
    return int(x)
def position_y(y):
    return int(y)
for x in range(haut):
    for y in range(long):
        background[x,y] = ' '
position_pomme = [position_x(random.randint(1,24)),position_y(random.randint(1,24))]
position_snake = [position_x(long/2),position_y(haut/2)]
old_position_snake = ['','']
all_old_position = []
score = 0
longueur =0
vie = True
partie = True
final_decision = True
y_direction = 0
x_direction = 0
UP = True
DOWN = True
LEFT = True
RIGHT = True
while partie == True :
    position_snake = [position_x(long/2),position_y(haut/2)]
    longueur =0
    final_decision = True
    while vie == True:
        if longueur > 1 :
            str_all_old_position = str(all_old_position)
            bad_chars = ['[',"]'",'(',')',", '","['[","]']"]
            for i in bad_chars:
                str_all_old_position = str_all_old_position.replace(i,' ')
            str_all_old_position = str_all_old_position.replace("'",' ')
            str_all_old_position = str_all_old_position.replace(']',' ')
            str_all_old_position = str_all_old_position.split('  ')
            str_all_old_position.pop(0)
            str_all_old_position.pop(-1)
            if len(str_all_old_position) > 2:
                for i in range(longueur-1):
                    val = str(str_all_old_position[-i-1])
                    val1 = val[3:]
                    val1 = val1.replace(',','')
                    val1 = int(val1)
                    val2 = val[:3]
                    val2 = val2.replace(',','')
                    val2 = int(val2)
                    str_all_old_position.pop(0)
                    background[val1,val2] = snake
            if len(str_all_old_position) > 20 and longueur >1:
                for loop in range((len(str_all_old_position)-longueur)):
                    str_all_old_position.pop(0)
        if position_pomme == position_snake :
            score += 10
            longueur += 1
            position_pomme = [position_x(random.randint(1,24)),position_y(random.randint(1,24))]
        print(position_snake)
        if keyboard.is_pressed("w") and UP == True:#up
            if position_snake[1] > 0:
                if position_snake[1] > 0:
                    y_direction = 1
                    x_direction = 0
                    UP=False
                    LEFT=True
                    RIGHT=True
                    DOWN = False
        if keyboard.is_pressed("s") and DOWN == True:#down
            if position_snake[1] < 24:
                if position_snake[1] < 24:
                    y_direction = -1
                    x_direction = 0
                    DOWN=False
                    UP=False
                    LEFT=True
                    RIGHT=True
        if keyboard.is_pressed("d") and LEFT == True :#left
            if position_snake[0] < 49:
                if position_snake[0] < 49:
                    x_direction = 1
                    y_direction = 0
                    LEFT=False
                    RIGHT=False
                    UP = True
                    DOWN = True
        if keyboard.is_pressed("a") and RIGHT == True:#right
                if position_snake[0] > 0:
                    x_direction = -1
                    y_direction = 0
                    RIGHT= False
                    LEFT = False
                    UP = True
                    DOWN = True
        if y_direction > 0 and x_direction == 0 and position_snake[1] > 0:
            old_position_snake[1] = position_snake[1]
            old_position_snake[0] = position_snake[0]
            position_snake[1] =  position_snake[1] - 1
            if background[position_snake[1],position_snake[0]] == snake:
                vie = False
            all_old_position.append(str(old_position_snake))
        if y_direction < 0 and x_direction == 0 and position_snake[1] < 24:
            old_position_snake[1] = position_snake[1]
            old_position_snake[0] = position_snake[0]
            position_snake[1] =  position_snake[1] + 1
            if background[position_snake[1],position_snake[0]] == snake:
                vie = False
            all_old_position.append(str(old_position_snake))
        if y_direction == 0 and x_direction > 0 and position_snake[0] < 49:
            old_position_snake[0] = position_snake[0]
            old_position_snake[1] = position_snake[1]
            position_snake[0] =  position_snake[0] + 1
            if background[position_snake[1],position_snake[0]] == snake:
                vie = False
            all_old_position.append(str(old_position_snake))
        if y_direction == 0 and x_direction < 0 and position_snake[0] > 0:
            old_position_snake[0] = position_snake[0]
            old_position_snake[1] = position_snake[1]
            position_snake[0] =  position_snake[0] - 1
            if background[position_snake[1],position_snake[0]] == snake:
                vie = False
            all_old_position.append(str(old_position_snake))
        if longueur > 0:
            background[old_position_snake[1],old_position_snake[0]] = snake
        background[position_snake[1],position_snake[0]] = snake
        #background[old_position_snake[1],old_position_snake[0]] = snake
        background[position_pomme[1],position_pomme[0]] = pomme
        if position_snake[0] == 0:
            vie = False
        if position_snake[0] == 49:
            vie = False
        if position_snake[1] == 0:
            vie = False
        if position_snake[1] == 24:
            vie = False
        for x in range(haut):
            for y in range(50):
                print(background[x,y],end='')
            print(':')
        for loop in range(25):
            print('..',end='')
        print(':\n')
        print("\t Score :",score)
        print("\t Longueur :", longueur+1)
        print('')
        for x in range(haut):
            for y in range(long):
                background[x,y] = ' '
        time.sleep(.1)
        os.system('clear')
    print('\t YOU LOST \n')
    print('\t Play again ? press enter or ctrl \n')
    print('\t Score : ',score)
    print("\t Longueur :", longueur+1)
    while final_decision == True:
        if keyboard.is_pressed("enter"):
            vie = True
            score = 0
            final_decision = False
            os.system('clear')
        if keyboard.is_pressed("ctrl"):
            final_decision = False
            vie = False
            partie = False

import os
import time
import random
import keyboard
sh,sw=30,30
engine={}
empty,snk,apl='░░','▓▓','▒▒'
apple=[random.randint(0,29),random.randint(0,29)]
length=2
snakeX,snakeY=sw/2,sw/2
snake=[[snakeX,snakeY],[snakeX,snakeY-1],[snakeX,snakeY-2]]
press=False
if __name__=="__main__":
    last=' '
    while True:
        time.sleep(.1)
        os.system('clear')
        for y in range(sh):
            for x in range(sw):
                engine[x,y]=empty
            print()
        new_head = [snake[0][0], snake[0][1]]
        if keyboard.is_pressed('w') and last!='s':
            last='w'
        elif keyboard.is_pressed('s') and last!='w':
            last='s'
        elif keyboard.is_pressed('a') and last!='d':
            last='a'
        elif keyboard.is_pressed('d') and last!='a':
            last='d'
        if last=='w':
            new_head[0] -= 1
        elif last=='s':
            new_head[0] += 1
        elif last=='a':
            new_head[1] -= 1
        elif last=='d':
            new_head[1] += 1
        snake.insert(0, new_head)
        del snake[length:]
        engine[apple[1],apple[0]]=apl
        if snake[0][0]==apple[0] and snake[0][1]==apple[1]:
            apple=[random.randint(0,29),random.randint(0,29)]
            length+=5
        for i in range(len(snake)):
            engine[snake[i][1],snake[i][0]]=snk
        for y in range(sh):
            for x in range(sw):
                print(engine[x,y],end='')
            print()
        if last!=' ':
            if snake[0][0] in [-1, sh] or snake[0][1] in [-1, sw] or snake[0] in snake[1:]:
                break

    print("t'es une bite")

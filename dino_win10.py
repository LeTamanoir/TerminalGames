import time
import os
import keyboard
def game():
    t2 = 0
    t1 = 0
    score = 0
    best_score = 0
    os.system('cls')
    val =0
    ligne_1 = "────────────────────────────────────────────────────────────────"
    sol1 = "─────────────────████────────────────────────────────────"
    sol2 = "████████████████████████████████████████████████████████████████"
    dino = ['──────────','──────────','──────────','────▄████▄', '────██▄███', '────█████▀', '───▄███───', '█▄█████▀█─', '─▀████────', '──█▄─█▄','']
    vie = True
    partie = True
    while partie == True:
        while vie == True :
            for i in range(11):
                ligne = ligne_1
                ligne = ligne[10:]
                ligne = dino[i] + ligne
                if i == 0:
                    ligne = ligne[len(str(score)) + 3:] + "█" + " " + str(score)
                if i == 1:
                    a = '█'
                    for loop in range(len(str(score))+ 2):
                        a = a + "▄"
                    ligne = ligne[len(str(score)) + 3:] + a
                if i == 8:
                    ligne = ligne + '────'
                if i == 9:
                    ligne = dino[i] + sol1
                    sol1 = sol1[2:]
                    sol1 = sol1 + sol1[0:2]
                if i == 10:
                    ligne = sol2
                if val == 1:
                    dino.remove(dino[-1])
                    dino.remove(dino[-1])
                    dino.append('──█▄─▀▀')
                    dino.append('')
                    val = 0
                else:
                    dino.remove(dino[-1])
                    dino.remove(dino[-1])
                    dino.remove(dino[-1])
                    dino.append('─▀█▀▀█')
                    dino.append('──▀▀─█▄')
                    dino.append('')
                    val =1
                print(ligne)
                condition = 1
                if sol1[1] == "█" or sol1[2] == "█" or sol1[3] == "█" or sol1[4] == "█" or sol1[5] == "█" or sol1[6] == "█":
                    for loop in range(20):
                        if keyboard.is_pressed("space") and condition == 1:
                            t1 = time.time()
                            condition = 0
                            os.system('cls')
                            score = score + 1
                            start_time = time.time()
                            seconds = .5
                            ligne_1 = "────────────────────────────────────────────────────────────────"
                            sol1 = "──────────████──────────────────────────────────────────────────"
                            sol2 = "████████████████████████████████████████████████████████████████"
                            dino = ['────▄████▄', '────██▄███', '────█████▀', '───▄███───', '█▄█████▀█─', '─▀████────',
                                    '──█▄─█▄', '', '──────────', '──────────', '──────────']
                            while True:
                                current_time = time.time()
                                elapsed_time = current_time - start_time
                                for b in range(11):
                                    ligne = ligne_1
                                    ligne = ligne[10:]
                                    ligne = dino[b] + ligne
                                    if b == 0:
                                        ligne = "".join(reversed(ligne))
                                        ligne = ligne[len(str(score)) + 3:]
                                        ligne = "".join(reversed(ligne))
                                        ligne =  ligne + "█" + " " + str(score)
                                    if b == 1:
                                        a = '█'
                                        for loop in range(len(str(score)) + 2):
                                            a = a + "▄"
                                        ligne = "".join(reversed(ligne))
                                        ligne = ligne[len(str(score)) + 3:]
                                        ligne = "".join(reversed(ligne))
                                        ligne = ligne + a
                                    if b == 5:
                                        ligne = ligne + '────'
                                    if b == 6:
                                        ligne = ligne + '───'
                                    if b == 7:
                                        ligne = ligne + '──────────'
                                    if b == 9:
                                        ligne = sol1
                                        sol1 = sol1[2:]
                                        sol1 = sol1 + sol1[0:2]
                                    if b == 10:
                                        ligne = sol2
                                    if val == 1:
                                        for loop in range(5):
                                            dino.remove(dino[-1])
                                        dino.append('──█▄─▀▀')
                                        dino.append('')
                                        for loop in range(3):
                                            dino.append('──────────')
                                        val =0
                                    else:
                                        for loop in range(6):
                                            dino.remove(dino[-1])
                                        dino.append('─▀█▀▀█')
                                        dino.append('──▀▀─█▄')
                                        dino.append('')
                                        for loop in range(3):
                                            dino.append('──────────')
                                        val=1
                                    print(ligne)
                                time.sleep(.1)
                                os.system('cls')
                                if elapsed_time > seconds:
                                    sol1 = "─────────────────────────────────────────────────────████"
                                    dino = ['──────────', '──────────', '──────────', '────▄████▄', '────██▄███',
                                            '────█████▀', '───▄███───', '█▄█████▀█─', '─▀████────', '──█▄─█▄', '']
                                    break
                        if keyboard.is_pressed('space'):
                            while keyboard.is_pressed('space'):
                                y = 1
                            t2 = time.time()
                        if t2 - t1 > .75:
                            score = 0
                            vie = False
                if sol1[0] == "█" :
                    if score > best_score:
                        best_score = score
                    vie = False
            time.sleep(.1)
            os.system('cls')
        for a in range(6):
            print(ligne_1)
            if a == 2 and t2 - t1 < 0.75:
                print("──────────────────────────GAME──OVER────────────────────────────")
            if a == 2 and t2 - t1 > 0.75:
                print("─────────────────────YOU─HAVE─BEEN─SPOTTED──────────────────────")
            if a == 4 and t2 - t1 > 0.75:
                print("───────────────────────MATCH─TERMINATED─────────────────────────")
        final_decision = True
        ligne2 = ligne_1[len(str(score)):]
        ligne2 = ligne2[0:len(str(ligne_1))//2]
        if len(str(score))%2 == 0:
            print(ligne2[(10+len(str(score)))//2:],"score :",score,ligne2[(10+len(str(score)))//2:])
        if len(str(score))%2 != 0:
            print(ligne2[(9+len(str(score)))//2+1:],"score :",score,ligne2[(9+len(str(score)))//2:])
        print(ligne_1)
        ligne6 = ligne_1[len(str(best_score)):]
        ligne6 = ligne6[0:len(str(ligne_1))//2]
        if len(str(best_score))%2 == 0:
            print(ligne2[(15+len(str(best_score)))//2+1:],"best score :",best_score,ligne2[(15+len(str(best_score)))//2:])
        if len(str(best_score))%2 != 0:
            print(ligne2[(15+len(str(best_score)))//2:],"best score :",best_score,ligne2[(15+len(str(best_score)))//2:])
        print(ligne_1)
        print("──────would you like to play again ? press enter or ctrl────────")
        for loop in range(2):
            print(ligne_1)
        while final_decision == True:
            if keyboard.is_pressed("enter"):
                vie = True
                t2 = 0
                t1 = 0
                score = 0
                final_decision = False
                os.system('cls')
                sol1 = "──────────────────────────────────────────────────────████"
            if keyboard.is_pressed("ctrl"):
                final_decision = False
                vie = False
                partie = False
game()

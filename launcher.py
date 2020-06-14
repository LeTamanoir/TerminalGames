import os
print("Hello ! are you on windows or linux ? answer by windows or linux\n")
var1 = input()
if var1 =='linux':
    print("Do you want to install all requirements ? yes or no\n")
    if input()=='yes':
        os.system('sudo pip3 install keyboard')

elif var1 =='windows':
    print("Would you like to install all requirements ? yes or no\n")
    if input()=='yes':
        os.system('pip3 install keyboard')

print("\n You can now play all the games, \n to do so just open a terminal (linux) or command prompt (win10)\n in the games' repertory and type :\n sudo python3 *the name of the game* and press enter (linux) \n python3 *the name of the game* and press enter (win10) \n Have Fun ! ")

print("\nLeTamanoir\n")

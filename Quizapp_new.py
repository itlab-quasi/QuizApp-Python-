import random
import csv
from datetime import datetime

def quiz(data, vocabs, answers):
    que = random.sample(range(0,len(data)),len(data))
    life = 10
    
    for x in range(0,len(data)):
        debagflag = False
        lifecount(life)
        print("No", x + 1,":",vocabs[que[x]])
        que2 = [que[x]]
        que3 = [num for num in range(0, len(data))]
        que3.remove(que[x])
        que3 = random.sample(que3, 3)
        que2 += que3
        random.shuffle(que2)

        for y in range(0,4):
            print(y+1,":", answers[que2[y]])
        
        while True:
            myans = input("your answer: ")
            if ('1'<= myans <='4' and 1 <= int(myans) <= 4):
                if que2[int(myans) - 1] == que[x]:
                    if x == (len(data) - 1):
                        print("Correct! Great job! This is the end of the test!")
                    else:
                        print("Correct! Go on to the next vocab.")
                        print("*************************************************")
                    break
                else:
                    print("Wrong Answer. Try again.")
                    print("*************************************************")
                    life -= 1
                    if life == 0:
                        print("You have no more life...\nGAME OVER!!!!\n")
                        debagflag = True
                        break
                    lifecount(life)
                    print("No", x + 1,":",vocabs[que[x]])
                    for y in range(0,4):
                        print(y+1,":", answers[que2[y]])
            elif myans == "quit":
                print("forcingly closing the app")
                debagflag = True
                break
            else:
                print("Invalid input. Please input numbers 1~4")
        if debagflag == True:
            break


def list(data):
    for i in range(0, len(data)):
        print("[" , i + 1, "] word: ", data[i][0], "\n    meaning: ", data[i][1])


def lifecount(life):
    print("life: ", end ="")
    for clife in range(0,10):
        if(clife < life):
            print("○", end ="")
        else:
            print("-", end ="")
    print()


if __name__ == '__main__':
    file_name = input("input unit file: ")
    
    data = []
    vocabs = []
    answers = []
    f = open(file_name, 'r')
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)
    f.close

    for i in range(0,len(data)):
        vocabs.append(data[i][0])
        answers.append(data[i][1])
    while True:
        print("Menu:\n[q]:Start Quiz\n[v]:List all Vocab\n[n]:Change CSV file\n[e]:End app")
        mode = input("Select Mode: ")
        if mode == "q":
            print("<<Starting Quiz>>")
            quiz(data, vocabs, answers)
        elif mode == "v":
            print("<<Listing all vocabulary>>")
            list(data)
        elif mode == "n":
            file_name = input("input new unit file: ")
            del data[::]
            del vocabs[::]
            del answers[::]
            f = open(file_name, 'r')
            reader = csv.reader(f)
    
            for row in reader:
                data.append(row)
            f.close
    
            for i in range(0,len(data)):
                vocabs.append(data[i][0])
                answers.append(data[i][1])
        elif mode == "e":
            print("Closing the app. Thanks for using! Come back soon!")
            break
        else:
            print("Invalid input!")

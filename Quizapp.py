import random
import csv

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

que = random.sample(range(0,len(data)),10)

for x in range(0,len(data)):
    print("No", x + 1,":",vocabs[que[x]])
    que2 = [que[x]]
    que3 = [num for num in range(0, 10)]
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
                if x == 9:
                    print("Correct! Great job! This is the end of the test!")
                else:
                    print("Correct! Go on to the next vocab.")
                print("*************************************************")
                break
            else:
                print("Wrong Answer. Try again.")
                print("*************************************************")
                print("No", x + 1,":",vocabs[que[x]])
                for y in range(0,4):
                    print(y+1,":", answers[que2[y]])
        else:
            print("Invalid input. Please input numbers 1~4")

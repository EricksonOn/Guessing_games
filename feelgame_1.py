
def rateme(numberchoices2,first):
    if first==True:
        numberchoices2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        first=False
    else:
        pass
    print("WELCOME \n")
    my_name = input("PLAYER ONE, ENTER NAME: \n\t\t")
    your_name = input("PLAYER TWO, ENTER NAME: \n\t\t")
    print(my_name)
    print(your_name)
    print(("CHOOSE A NUMBER TO SHOW HOW YOU FEEL ABOUT {0}").format(your_name))
    print("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]")
    choices=None
    while type(choices)!="int":
        try:
            choices =int(input("ENTER NUMBER TO CHOOSE HOW YOU FEEL ABOUT ME: \n\t\t\t"))
            break
        except ValueError:
            print("Please type numbers between 1-15 only!")
    if choices==numberchoices2[0]:
        print(my_name, "HATES", your_name)
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[1]:
        print("I STUPIDLY HATE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[2]:
        print("I DESPICE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[3]:
        print("I LOVE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[4]:
        print("I ADORE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[5]:
        print("I ADMIRE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[6]:
        print("I SOMEHOW LIKE YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[7]:
        print("I RARELY WANT TO BE NEAR YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[8]:
        print("I SERIOUSLY DO NOT WANT YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[9]:
        print("I YOU AMAZE ME\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[10]:
        print("I DETEST YOU\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[11]:
        print("YOU DISGUST ME\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[12]:
        print("IT'S JUST A FEELING I HAVE FOR YOU BUT.... \n YOU NEED TO GUESSE IT FROM MY EYES\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[13]:
        print("NEVER ASK ME THAT\n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
    elif choices==numberchoices2[14]:
        print("ASK AGAIN! \n")
        numberchoices2=[numberchoices2[3],numberchoices2[5],numberchoices2[0],numberchoices2[10],numberchoices2[2],numberchoices2[7],numberchoices2[13],numberchoices2[4],numberchoices2[9],numberchoices2[1],numberchoices2[12],numberchoices2[14],numberchoices2[6],numberchoices2[8],numberchoices2[11]]
        rateme(numberchoices2,first)
numberchoices2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
first=True
rateme(numberchoices2,first)

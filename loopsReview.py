def main():
    #ex1()
    #ex2()
    ex3()
    #bonus()



def ex1():
    for x in range(7):
        if x==3 or x==6:
            continue
        print(x)

def ex2():
    evenNums= 0
    oddNums= 0
    for x in range(10):
        if x%2==0:
            evenNums += 1
        else:
            oddNums += 1
    print("The number of even numbers: ",evenNums," The number of odd numbers: ",oddNums)


def ex3():
    userlist= ""
    while True:
        string= input("Enter a movie you like. Just hit enter to quit")
        if string == "":
            break
        userlist=userlist+ (string+"\n")
    print(userlist)

























if __name__ == '__main__':
    main()
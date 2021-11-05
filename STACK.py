# because of the liquid nature of lists, they can be used to create stacks and queues
#they are LIFO data structures , to add into a stack you push and to remove you pop it off
stack=[]
def pushit():
    stack.append(input("enter a new string:").strip())
    #strip removes white spaces in a string in user inputs or file object manipulation outputs

def popit():
    if len(stack)==0:
        print("can`t pop from an empty stack")
    else:
        print(stack.pop())

def viewstack():
    print(stack)  #calls str internally

cmds={'u':pushit,'o':popit,'v':viewstack}
def showMenu():
    pr='''
    p(U)sh
    p(O)P
    (V)iew
    (Q)uit
    
enter choice: '''
    while True:
        while True:
            try:
                chce=input(pr).strip()[0].lower() #to indicate that the first letter is lowercase
            except(EOFError,KeyboardInterrupt,IndexError):
                chce='q'
            print('\nYou picked, [{0}]'.format(chce))
            if chce not in 'uovq':
                print("invalid option , try again")
            else:
                break
        if chce=='q':
            break
        cmds[chce]()#this is to indicate that the content inside the content inside the dict are functions
showMenu()
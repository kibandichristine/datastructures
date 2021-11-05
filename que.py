queue=[]
def addQ():
    queue.append(input("enter what you want").strip())

def delq():
    if len(queue)==0:
        print('wacha ujinga hakuna kitu')
    else:
        print('you have deleted [',queue.pop(0),']')

def viewq():
    print(queue)
#then the functions
funcs = {'A':addQ,'D':delq,'V':viewq}

def showmenu():
    pr='''
    (A)ddQ
    (D)delq
    (V)iewq
    (q)uit
    
    enter choice
    '''
    while True:
        while True:
            try:
                choice=input(pr).strip()[0].upper()
            except(EOFError,KeyboardInterrupt,IndexError):
                choice='q'
            print('\n your choice is  [',choice,']')
            if choice not in 'ADVQ':
                print('jaza vizuri nani')
            else:
                break
        if choice=='q':
            break
        funcs[choice]()
showmenu()



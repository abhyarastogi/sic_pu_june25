import sys as s
def inserting():
    ele = int(input('Enter element:'))
    list1.insert(0, ele)
def popping():
    if len(list1) > 0:
        result=list1.pop(0)
        print(result)
    else:
        print('Stack is empty.')
def display():
    if len(list1)>0:
        print(list1)
    else:
        print('Stack is empty.')
def exiting():
    s.exit('Exiting...')
list1 = []
opertion_dic = {1: inserting,
                2: popping,
                3: display,
                4: exiting
                }
operation_choice = 1
while operation_choice != 4:
    print('1.Inserting\n2.Popping\n3.Display\n4.Exiting')
    operation_choice = int(input('Enter your choice:'))
    if operation_choice > 4 or operation_choice < 1:
        print('Invalid Input')
    opertion_dic[operation_choice]()


#Remove the duplicates in a list of size n
def removing_duplicates(list):
    list2 = []
    for i in list:
        if i not in list2:
            list2.append(i)
    print(list2)
list1 = []
input_size = int(input('Enter the size of list :'))
for i in range(input_size):
    element = int(input('Enter the element :'))
    list1.append(element)
removing_duplicates(list1)
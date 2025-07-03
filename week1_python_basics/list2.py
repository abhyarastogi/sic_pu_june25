#Find the frequency an element in a list of n elements.
def finding_frequency(list):
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        print(i,':',dict[i])
list1 = []
n = 0
number_of_elements = int(input('Enter the size of the list :'))
while n < number_of_elements:
    elements = int(input('Enter the element :'))
    n += 1
    list1.append(elements)
finding_frequency(list1)
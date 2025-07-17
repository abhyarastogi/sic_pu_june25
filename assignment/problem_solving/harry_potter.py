def harry_potter(n, coin_value, number_of_instructions, x):
    index = 0
    bag = []
    for i in range(number_of_instructions):
        instruction = input('Enter harry/remove :')
        if instruction == 'harry':
            bag.append(coin_value[index])
            index += 1
        elif instruction == 'remove':
            del bag[-1]
            index -= 1
        if x == sum(bag):
            print(len(bag))
            return
    print('-1')
n = int(input('Enter number of coins harry has :' ))
coin_value = list(map(int,input('Enter value for each coin :').split()))
number_of_instructions, x = map(int, input('Enter number of instructions and value for x :').split())
harry_potter(n, coin_value, number_of_instructions, x)            
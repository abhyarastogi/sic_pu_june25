
# Complete the getMinimumCost function below.
#import pdb
#pdb.set_trace()
def getMinimumCost(k, c):
    minimum_cost = 0
    c.sort(reverse = True)
    i = 0
    j = 0
    l = 1
    while i < len(c):
        if i < k:
            minimum_cost += c[i]
        else:
            if j < k:
                minimum_cost += (l + 1)*c[i]
            else:
                l+=1
                j=0
        #j+=1      
        i+=1
    return minimum_cost

if __name__ == '__main__':

    nk = input('Enter number of flowers and number of buyers').split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input("Enter the prices for all flowers").rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)


import random

'''A naive recursive implementation of 0-1 Knapsack Problem  
Returns the maximum value that can be put in a knapsack of capacity '''  


def knapSack(Weight, value, capacity, numberOfObjects):
    if(numberOfObjects==0 or capacity == 0):
        return 0

    # If weight of the nth item is more than Knapsack of capacity, 
    # then this item cannot be included in the optimal solution. 

    elif(Weight[numberOfObjects-1] > capacity):
        return knapSack(Weight, value, capacity, numberOfObjects-1)

    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
        
    else:
        return max(
            value[numberOfObjects-1] + knapSack(
                Weight, value, capacity - Weight[numberOfObjects -1], numberOfObjects -1),
            knapSack(Weight, value, capacity, numberOfObjects -1))



if __name__ == '__main__':
    capacity = int(input('Enter Capacity of bag: '))
    n = int(input('Enter the number of items: '))
    weight = [random.randint(1,20) for x in range(n)]
    value = [random.randint(1,100) for x in range(n)] 
    print('Weights are : {}\nvalues are: {}\nCapacity of Bag:{}'.format(weight,value,capacity))

    print('The maximum profit: {}'.format(knapSack(weight,value,capacity,n)))

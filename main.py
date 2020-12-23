def solution(numBottles,numExchange):
    finalsum = numBottles
    emptyBottles = numBottles
    numBottles = 0
    while (emptyBottles >= numExchange):
        numBottles = emptyBottles // numExchange
        emptyBottles -= emptyBottles // numExchange * numExchange
        finalsum += numBottles
        emptyBottles += numBottles
    print (finalsum)



numBottles = int(input("numBottles = "))
numExchange = int(input("numExchange = "))
solution(numBottles,numExchange)
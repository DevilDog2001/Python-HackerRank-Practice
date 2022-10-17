def getMinimumOperations(item):
    items = [6,5,9,7,3]
    a = items[3]/2
    items =[6,5,4,7,1]
    b = items[5]/2
    items = [6,5,4,7,0]
    c = items[5]/2
    list = (a,b,c)
    print(min(list))
    
getMinimumOperations(item)
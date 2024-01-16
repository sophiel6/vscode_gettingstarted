# sorting method 

numList = [32,8,7,560,0, -4,-6,1]



def bubble_sort(array):
    n = len(array)

    for i in range(n):
        print("i = "+str(i))
        fully_sorted = True 
        for j in range(n-i-1):
            print("j = "+str(j))
            print("array[j] = "+str(array[j])+", array[j+1] = "+str(array[j+1]))
            if array[j] > array[j+1]:
                x = array[j]
                array[j] = array[j+1]
                array[j+1] = x
                print(array)

                fully_sorted = False
        if fully_sorted: break
    return array 

print(bubble_sort(numList))
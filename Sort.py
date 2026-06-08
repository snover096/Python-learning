def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(0,len(list)-i-1):
            if  list[j]>list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j]  = temp   # Swap the elements.                   


def quickSort(list):
    index = 0



if __name__ == "__main__": 
     list = [64,34,25,12,22,11,3]     
     bubbleSort(list)   # Call the function to sort.      
     print ("Sorted array is:", end=" ") 
     for i in range (len(list)):         
         print("%d" % list[i],end = " ")        # Print sorted elements     
   

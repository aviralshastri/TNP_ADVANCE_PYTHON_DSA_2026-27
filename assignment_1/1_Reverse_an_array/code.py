array=[1,2,3,4,5]

def reverse_array(array):
    temp=0
    
    for i in range(len(array)//2):
        temp=array[len(array)-1-i]
        array[len(array)-1-i]=array[i]
        array[i]=temp

    return array

if __name__=="__main__":
    print(reverse_array(array))

input("Press any key to exit !")

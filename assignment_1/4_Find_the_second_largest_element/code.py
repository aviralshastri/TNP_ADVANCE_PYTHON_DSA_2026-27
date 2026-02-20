array=[1,5,2,6,2,3]


def second_largest(array):
    curr_max=0
    second_max=0
    for i in array:
        if curr_max<i:
            second_max=curr_max
            curr_max=i
            
    return second_max
    

if __name__=="__main__":
    print(second_largest(array))

input("Press any key to exit !")

array=[1,2,3,4,5,6]

def check_sorted(array):
    for i in range(len(array)-1):
        if array[i+1]<array[i]:
            return False
    return True

if __name__=="__main__":
    print(check_sorted(array))

input("Press any key to exit !")

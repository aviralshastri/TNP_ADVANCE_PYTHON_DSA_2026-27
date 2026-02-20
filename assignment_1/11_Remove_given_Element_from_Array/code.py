array=[1,7,4,3,6,2,6,4]

def remove_ele(array,ele):
    for i in range(len(array)):
        if array[i]==ele:
            ind=i
            array.pop(ind)
            return ind
    return False


if __name__=="__main__":
    print(remove_ele(array,6))

input("Press any key to exit !")

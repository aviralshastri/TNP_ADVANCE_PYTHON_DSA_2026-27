array=[1,5,2,6,2,3]


def arr_sum(array):
    s=0
    for i in array:
       s+=i
    return s


if __name__=="__main__":
    print(arr_sum(array))

input("Press any key to exit !")

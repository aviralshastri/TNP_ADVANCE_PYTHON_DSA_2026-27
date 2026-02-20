array=[1,4,5,7,9,3,2,2,6,7]

def dupli_check(array):
    dupli=set()
    freq={}
    for i in range(len(array)):
        if not freq.get(array[i],0):
            freq[array[i]]=1
        else:
            freq[array[i]]=+1
            dupli.add(array[i])
    return dupli

if __name__=="__main__":
    print(dupli_check(array))

input("Press any key to exit !")

array1=[1,5,4,5,8]
array2=[2,3,0,9]

def union(array1,array2):
    freq={}
    max_len=max(len(array1),len(array2))
    i=0
    while i<max_len:
        if i<len(array1):
            if not freq.get(array1[i],0):
                freq[array1[i]]=1
            
        if i<len(array2):
            if not freq.get(array2[i],0):
                freq[array2[i]]=1
        i+=1
    return list(freq.keys())

if __name__=="__main__":
    print(union(array1,array2))

input("Press any key to exit !")

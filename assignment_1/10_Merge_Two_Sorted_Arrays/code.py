array1=[1,2,5,6,8,9]
array2=[3,3,10,11,15]

def merge_sorted_arrays(nums1, nums2):
    i = j = 0
    merged = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    return merged


if __name__=="__main__":
    print(merge_sorted_arrays(array1,array2))

def merge_array(nums1:list, nums2:list, len1:int, len2:int) -> str:
    """ len1:int = len(nums1)
    len2:int = len(nums2) """
    last:int = len1 + len2 - 1
    while len1 > 0 and len2 > 0:
        if nums1[len1 -1] > nums2 [len2 -1]:
            nums1[last] = nums1[len1 - 1]
            len1 -= 1
        else:
            nums1[last] = nums2[len2 - 1]
            len2 -= 1
        last -= 1
    # if the least value in nums2 is greater than nums1
    while len2 > 0:
        if nums2[len2 -1] > nums1[len1 -1]:
            nums1[last] = nums2[len2]
            last -= 1 
            len2 -= 1
    return f"New merged array is {nums1}"

def merge_array2(nums1:list, nums2:list) -> str:
    for num in nums2:
        nums1.append(num)
    nums1 = sorted(nums1)
    return nums1
def main():
    nums1:list = [1,2,3,0,0,0]
    len1:int = 3
    nums2:list = [2,4,5]
    len2:int = 3
    # need to manually have their previous lenght for this to work
    print(merge_array(nums1,nums2,len1,len2))
    #print(merge_array2(nums1,nums2))
if __name__ == "__main__":
    main()
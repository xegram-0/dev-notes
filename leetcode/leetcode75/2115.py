class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set()
        set4 = set()
        for num in set2:
            if num not in set1:
                set3.add(num)
        for num in set1:
            if num not in set2:
                set4.add(num)
            
        answer.append(list(set4))
        answer.append(list(set3))
        return answer


# Better version
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [
            list(set1 - set2),
            list(set2 - set1)
        ]

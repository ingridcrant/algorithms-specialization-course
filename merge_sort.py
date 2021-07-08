# merge sort
# python implementation from Tim Roughgarden's Algorithms course
def merge_sort(nums):
    if len(nums) > 1:
        half = len(nums)//2

        a = merge_sort(nums[:half])
        b = merge_sort(nums[half:])

        i = 0
        j = 0

        for k in range(len(nums)):
            if i < len(a) and j < len(b):
                if a[i] < b[j]:
                    nums[k] = a[i]
                    i += 1
                else:
                    nums[k] = b[j]
                    j += 1
            else:
                if i == len(a):
                    nums = nums[:k] + b[j:]
                else:
                    nums = nums[:k] + a[i:]
                break
        print(nums)
    
    # base case: size of nums is 1
    return nums
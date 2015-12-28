class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        if len(numbers) < 3:
            return result

        sorted_array = sorted(numbers)
        # a[i] is the first one
        # a[j] is the middle one
        # a[k] is the last one
        for i in range(len(sorted_array)):
            j = i+1
            k = len(sorted_array)-1

            while j<k:
                if sorted_array[i] + sorted_array[k] + sorted_array[j] > 0:
                    k -= 1
                elif sorted_array[i] + sorted_array[k] + sorted_array[j] < 0:
                    j += 1
                else:
                    # found the target
                    # if not duplicated, append it.
                    if [sorted_array[i], sorted_array[j], sorted_array[k]] not in result:
                        result.append([sorted_array[i], sorted_array[j], sorted_array[k]])
                    # move j to next unduplicated pos
                    if sorted_array[j] != sorted_array[j+1]:
                        j += 1
                    else:
                        while j < len(sorted_array)-1 and sorted_array[j] == sorted_array[j+1]:
                            j += 1
                    # move k to next unduplicated pos
                    if sorted_array[k] != sorted_array[k-1]:
                        k -= 1
                    else:
                        while k > 0 and sorted_array[k] == sorted_array[k-1]:
                            k -= 1
        return result

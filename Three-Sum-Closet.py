class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if numbers == None or len(numbers) == 0:
            return 0
        diff = sys.maxint
        result = 0
        sorted_array = sorted(numbers)

        for i in range(len(numbers)):
            j = i+1
            k = len(numbers)-1
            while j<k:
                tmp_sum = sorted_array[i] + sorted_array[j] + sorted_array[k] 
                if abs(tmp_sum - target) < diff:
                    diff = abs(tmp_sum-target)
                    result = tmp_sum
                if tmp_sum == target:
                    return result
                elif tmp_sum > target:
                    k -= 1
                else:
                    j += 1
        return result

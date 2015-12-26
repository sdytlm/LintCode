class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        result = []
        hash_map = dict()
        if numbers == None:
            return result
        # Create hash_map: <numbers[i], i>
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i+1
        
        for front in numbers:
            if hash_map.has_key(target-front) and hash_map[front] < hash_map[target-front]:
                result.append(hash_map[front])
                result.append(hash_map[target-front])
        return result


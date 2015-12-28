class Solution: 
    """ 
    @param numbers : An array of Integer 
    @param target : target = numbers[index1] + numbers[index2] 
    @return : [index1 + 1, index2 + 1] (index1 < index2) 
    Space: O(N)
    Time: O(N)
    """ 

    def twoSum(self, numbers, target): 

        result = []
        # Create hash_map: [numbers[i], i]
        hash_map = dict()
        # sorted_array:
        sorted_array = sorted(numbers)

        # Create hash_map
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i+1

        front = 0
        end = len(numbers)-1

        while front < end :
            if sorted_array[front]+sorted_array[end] < target:
                front += 1
            elif sorted_array[front]+sorted_array[end] > target:
                end -=1 
            else:
                # Real index is stored in hash_map
                first = hash_map[sorted_array[front]]
                second = hash_map[sorted_array[end]]
                if first < second:
                    result.append(first)
                    result.append(second)
                else:
                    result.append(second)
                    result.append(first)
                    
                return result

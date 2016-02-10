def comparator(x,y):
    x_y = x+y
    y_x = y+x
    if y_x > x_y:
        return 1
    else:
        return -1
class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    # write your code here
    def largestNumber(self, num):
        # write your code here
        if num == None:
            return None
        string_list = []
        # change int to strings
        for i in range(len(num)):
            string_list.append(str(num[i]))
        # remove duplicate in the strings
        
        string_list.sort(comparator)
        result = ""
        for i in string_list:
            result += i
        
        # case "0,0"
        index = 0
        while index < len(string_list) and string_list[index] == "0":
            index += 1
        if index == len(string_list):
            return "0"
        
        return result

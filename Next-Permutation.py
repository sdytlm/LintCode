class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        if num == None or len(num) < 2:
            return num
        end = len(num)-1
        front = end-1
        
        # find the element who breaks the rule
        while front>=0:
            if num[front] < num[end]:
                break
            else:
                front -= 1
                end -= 1
        if front==-1:
            num.sort()
        else:
            # find the smallest element(element>num[front])
            end = len(num)-1
            while end > front:
                
                if num[end] > num[front]:
                    break
                else:
                    end -= 1
                
            # swap the front, end   
            num[front],num[end] = num[end],num[front]
            num[front+1:] = sorted(num[front+1:])
        return num

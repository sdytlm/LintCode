class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if gas == None or cost == None:
            return -1

        # if sum(gas) < sum(cost), then no solution
        sum_gas = 0
        for i in gas:
            sum_gas += i
        sum_cost = 0
        for i in cost:
            sum_cost += i

        if sum_cost > sum_gas:
            return -1

        # Otherwise, there is a solution
        remain_gas = 0
        start_index = 0

        for i in range(gas):
            diff = gas[i] - cost[i]
            if remain_gas >= 0:
                remain_gas += diff
            else:
                # [0,i] can be passed, need to update start_index
                start_index = i
                remain_gas = diff
        return start_index
                


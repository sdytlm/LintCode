class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        """
        L: The maximum length of the small pieces (0<L<max(L[i]))
        if sum(L[i]/L) >= k, then L is the maximum length we want
        This problems is to find propoer L from range(0,max(L[i])), which can satisfy the above condition
        """
        # length > pieces
        if sum(L) < k:
            return 0

        max_L = max(L)
        
        sorted_L = sorted(L)

        front = 0
        end = max_L

        while front<=end:
            mid = (front+end)/2
            sum_pieces = sum([each_L/mid for each_L in sorted_L])
            # case 1: mid is too large to make k pieces
            if sum_pieces < k:
                end = mid-1
            # case 2: mid is too small that make more than k pieces
            elif sum_pieces > k:
                front = mid+1
            # case 3: exact k pieces, but we know not if other mid can also make 7 pieces
            else:
                front = mid+1

        # result should be either "front" or "end"
        if sum([l/end for l in L]) >= k:
            return end
        else:
            return front

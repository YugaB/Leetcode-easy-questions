class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        for i in J:
            if(i in S):
                count+=1
        return count
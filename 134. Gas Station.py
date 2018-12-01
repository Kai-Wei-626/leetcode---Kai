'''
brute force, almost exceed time limit
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        offset = [x-y for x,y in zip(gas, cost)]
        depth = 0
        
        if len(offset) == 0:
            return -1
        if len(offset) == 1:
            if offset[0] >= 0:
                return 0
            else:
                return -1
        
        for i in range(len(offset)):
            if offset[i] >= 0:
                new = offset[i+1:]
                new.extend(offset[:i])
                startGasLeft = offset[i]
                depth = 0  # reset depth to 0
                
                for j in range(len(new)):
                    startGasLeft += new[j]
                    if startGasLeft >= 0:
                        depth += 1
                        continue
                    else:
                        break
            
            if depth == len(offset) - 1:
                return i
        
        return -1
 
 
 '''
 better solution, for start to end, only require linear time
 '''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        offset = [x-y for x,y in zip(gas, cost)]
        if sum(offset) < 0:
            return -1

        depth = 0
        next_Level = 0
        cur_level = 0

        for i in range(len(offset)):
            #print(i, cur_level,next_Level)
            if cur_level <= next_Level:
                depth = i
                next_Level = cur_level

            cur_level += offset[i]

        return depth        
                              

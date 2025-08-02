class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nextMax = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                nextMax[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return nextMax

""" 
simple pseudocode [3, 4, 5, 1, 0, 2, 6, 3]
stack => [3, ]
curr = 4
-> start popping
-> pop until stacktop is >= curr
  -> while popping -> set their nextmaxes to curr 
"""
        






class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decStack = []
        nextMax = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while decStack and temperatures[i] >= temperatures[decStack[-1]]:
                decStack.pop()
            nextMax[i] = decStack[-1] - i if decStack else 0
            decStack.append(i)
        
        return nextMax



            
                


            
                

        
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []

        for op in operations:
            if op == "+":
                #can get last value of array by doing -1
                scoreStack.append(scoreStack[-1] + scoreStack[-2])
            
            elif op == "D":
                scoreStack.append(2 * scoreStack[-1])
            
            elif op == "C":
                scoreStack.pop()
            else:
                scoreStack.append(int(op))
        return sum(scoreStack)

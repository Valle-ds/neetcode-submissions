class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        output = 0
        for i in range(len(operations)):
            a = operations[i]
            aa = 0
            if a == '+':
                aa = ans[-1] + ans[-2]
                ans.append(aa)
            elif a == 'C':
                aa = -(ans.pop())
            elif a == 'D':
                aa = ans[-1]* 2
                ans.append(aa)
            else:
                aa = int(a)
                ans.append(aa)
            output += aa
        return output

            
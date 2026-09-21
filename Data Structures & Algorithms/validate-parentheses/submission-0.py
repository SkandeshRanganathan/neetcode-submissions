class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(' : ')', '[' : ']' , '{' : '}'}
        for i in s:
            if i in dic:
                stack.append(dic[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return not stack
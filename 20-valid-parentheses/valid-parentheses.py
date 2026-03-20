class Solution(object):
    def isValid(self, input_str):
        """
        :type s: str
        :rtype: bool
        """
        valid = {
        "{": "}", 
        "[": "]", 
        "(": ")"
        }
        stack = []
        for char in input_str:
            if char in valid.keys():
                stack.append(char)
            elif char in valid.values():
                if not stack:
                    return False
                last_open = stack.pop()
                if valid[last_open] != char:
                    return False
            else:
                return False
        return len(stack) == 0
        
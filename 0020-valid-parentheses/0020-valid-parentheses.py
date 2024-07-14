class Solution(object):
    def isValid(self, s):
        # valid_brack = [('(', ')'), ('{', '}'), ('[', ']')]
        # stack = []
        # for c in s:
        #     if len(stack)>0 and (stack[-1], c) in valid_brack:
        #         stack.pop()
        #     else:
        #         stack.append(c)
        # return len(stack)==0
        
        string_dict = {"(" :")", "[" :"]", "{":"}"}
        stack = []
        for char in s:
            if char in string_dict:
                stack.append(char)
            else:
                if not stack or string_dict[stack.pop()] != char:
                    return False
        return len(stack) == 0
                    
                
            
        
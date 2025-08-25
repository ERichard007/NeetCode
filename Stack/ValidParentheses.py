class Solution:
    #1.) Every open bracket is closed by the same type of close bracket.
    #2.) brackets are closed in the correct order.
    #3.) Every close bracket has a corresponding open bracket of the same type.

    # [] = true
    # ([{}]) = true
    # [(]) = false
    def isValid(self, s: str) -> bool:
        myStack = []

        for chr in s:

            print(chr)

            if chr == ")":
                if len(myStack) == 0 or myStack.pop() != "(":
                    return False
            elif chr == "]":
                if len(myStack) == 0 or myStack.pop() != "[":
                    return False
            elif chr == "}":
                if len(myStack) == 0 or myStack.pop() != "{":
                    return False
            else:
                myStack.append(chr)

        if len(myStack) == 0:
            return True
        else:
            return False


mySolution = Solution()
print(mySolution.isValid("[(])"))

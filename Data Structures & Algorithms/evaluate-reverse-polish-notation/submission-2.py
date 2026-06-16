class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        oper = ["+","-","*","/"]

        for i in tokens:
            if i not in oper:
                stack.append(int(i))
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if i == "+":
                    stack.append(op1 + op2)
                if i == "-":
                    stack.append(op1 - op2)
                if i == "*":
                    stack.append(op1 * op2)
                if i == "/":
                    stack.append(op1 / op2)
        return int(stack.pop())
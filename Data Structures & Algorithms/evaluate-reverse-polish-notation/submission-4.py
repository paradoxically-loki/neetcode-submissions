class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1: return int(tokens[0])

        stack = []

        for ch in tokens:

            if ch not in '+-*/':
                stack.append(ch)

            else:

                second = int(stack.pop())
                first = int(stack.pop())

                if ch == '+':
                    stack.append(first + second)
                elif ch == '-':
                    stack.append(first - second)
                elif ch == '*':
                    stack.append(first * second)
                elif ch == '/':
                    stack.append(int(first / second))
        
        return stack[0]
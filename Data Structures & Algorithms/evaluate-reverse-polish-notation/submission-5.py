class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for ch in tokens:

            if ch not in '+-*/':
                stack.append(int(ch))

            else:

                second = stack.pop()
                first = stack.pop()

                if ch == '+':
                    stack.append(first + second)
                elif ch == '-':
                    stack.append(first - second)
                elif ch == '*':
                    stack.append(first * second)
                elif ch == '/':
                    stack.append(int(first / second))
        
        return stack[0]
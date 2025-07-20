class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for char in tokens:
            if char.lstrip('-').isnumeric():
                stack.append(int(char))
            else:
                print(f"{stack=}, {char=}")
                second = stack.pop()
                first = stack.pop()

                if char == '+':
                    stack.append(first+second)
                elif char == '-':
                    stack.append(first-second)
                elif char == '*':
                    stack.append(first*second)
                else:
                    stack.append((-1 if first*second < 0 else 1) * (abs(first)//abs(second)))
        
        return stack[-1]

        # [17,"5","+"] 
        
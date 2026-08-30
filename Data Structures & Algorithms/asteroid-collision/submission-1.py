class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0: # curr is stronger than the top
                    stack.pop()
                elif diff > 0: # curr is weaker than that top
                    a = 0
                else: # curr and top are equally strong
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)
        return stack


        
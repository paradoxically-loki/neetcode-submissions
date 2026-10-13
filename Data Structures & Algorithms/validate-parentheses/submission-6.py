class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        map = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                st.append(c)
            else:
                if not st:
                    return False
                else:
                    if st.pop() != map[c]:
                        return False

        return len(st) == 0
        
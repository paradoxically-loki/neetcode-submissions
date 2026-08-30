class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1

            elif b == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False

            else:
                change = 15
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        
        return True
        
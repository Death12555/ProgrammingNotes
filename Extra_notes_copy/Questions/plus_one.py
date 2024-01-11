class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1]+= 1

        for i in range(len(digits)-1, 0, -1):
            if digits[i]>9:
                digits[i-1]+= digits[i]//10
                digits[i]%= 10

        if digits[0]>9:
            digits[0]= digits[0]//10
            digits.append(0)

        return digits

class Solution:
    def isHappy(self, n: int) -> bool:
        check_list = []
        while True:
            sum_n = 0
            for i in list(str(n)):
                sum_n += int(i)**2
            
            n = sum_n
            if sum_n == 1:
                return True

            if sum_n in check_list:
                return False
            check_list.append(sum_n)
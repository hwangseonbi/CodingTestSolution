class Solution:
    def findNthDigit(self, n: int) -> int:
        answer = 0
        range_class = 1

        start_num = 0
        end_num = 9
        while True:
            next_n = n - (end_num - start_num + 1)*range_class
            if next_n <= 0:
                break
            n = next_n

            start_num = end_num + 1
            range_class += 1
            end_num = 10**range_class - 1

        value, res = divmod(n,range_class)
        number = value + start_num
        answer = int(str(number)[res])
        return answer

    def test(self):
        assert self.findNthDigit(1000) == 3
        assert self.findNthDigit(3) == 3
        assert self.findNthDigit(10) == 1
        assert self.findNthDigit(11) == 0
        assert self.findNthDigit(12) == 1

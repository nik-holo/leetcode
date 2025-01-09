class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        l, r = 1, x
        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1

        return r


def main():
    print(Solution().mySqrt(2888888888))

main()

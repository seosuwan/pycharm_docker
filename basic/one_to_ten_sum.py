'''
파이썬에서 루프 형태는 3가지가 있다.
'''
from icecream import ic
class OneToTenSum():

    def one_to_ten_sum_1(self):
        # example 1
        sum = 0
        for i in range(1, 11):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        return sum(i for i in range(1, 11)) #내장함수일때만 리스트컴프레션이 된다.

    def one_to_ten_sum_3(self):
        return sum(range(1,11))

if __name__ == '__main__':
    a = OneToTenSum()
    ic(a.one_to_ten_sum_1())
    ic(a.one_to_ten_sum_2())
    ic(a.one_to_ten_sum_3())


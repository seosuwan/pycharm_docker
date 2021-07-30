import unittest

from basic.reverse_string import Reverse


class ReverseTest(unittest.TestCase):

    reverse = Reverse()

    def str_to_list_test(payload: str) -> []:
        return [i for i in payload if i.isalnum()]


    def reverse_string_test(s: []) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


    def list_to_str_test(self) -> str:
        pass

if __name__ == '__main__':
    unittest.main()

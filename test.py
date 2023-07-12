from whiteboard import solution
import unittest 


class TestSolution(unittest.TestCase):
    def test_one(self):
        arr = [1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(solution(arr), [2, 3])

    def test_two(self):
        arr = [5,2,7,7,2]
        self.assertEqual(solution(arr), [2, 7])

    def test_three(self):
        arr = [3,3,8,9,3,8,6,8,9,9]
        self.assertEqual(solution(arr),  [3, 8])


if __name__ == '__main__':
    unittest.main()
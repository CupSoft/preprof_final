import unittest
from algo import algorithm


tests = [
    [
        {
            "SH": 56, 
            "distance": 44
        }
    ],
    [
        {
            "SH": 4088, 
            "distance": 28
        }, 
        {
            "SH": 504, 
            "distance": 43
        }, 
        {
            "SH": 120, 
            "distance": 20
        }
    ],
    [
        {
            "SH": 6, 
            "distance": 10
        }, 
        {
            "SH": 3, 
            "distance": 19
        }
    ]
]



expected_output = [
    
]


class TestMethods(unittest.TestCase):

    def test_algorithm(self):
        for i in range(len(tests)):
            self.assertEqual(algorithm(tests[i]), expected_output[i])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
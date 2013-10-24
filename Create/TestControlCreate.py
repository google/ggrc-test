'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestControlCreate(BaseTestCreate):
    def testControlCreate(self):
        self._create_test("Control")


if __name__ == "__main__":
    unittest.main()

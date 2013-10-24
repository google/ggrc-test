'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestSystemCreate(BaseTestCreate):
    def testSystemCreate(self):
        self._create_test("System")


if __name__ == "__main__":
    unittest.main()

'''
Created on Jul 16, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestProgramCreate(BaseTestCreate):
    def testProgramCreate(self):
        self._create_test("Program")


if __name__ == "__main__":
    unittest.main()

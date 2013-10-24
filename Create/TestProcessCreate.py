'''
Created on Jul 23, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestProcessCreate(BaseTestCreate):
    def testProcessCreate(self):
        self._create_test("Process")


if __name__ == "__main__":
    unittest.main()

'''
Created on Jul 17, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestContractCreate(BaseTestCreate):
    def testContractCreate(self):
        self._create_test("Contract")


if __name__ == "__main__":
    unittest.main()

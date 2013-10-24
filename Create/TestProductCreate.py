'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestProductCreate(BaseTestCreate):
    def testProductCreate(self):
        self._create_test("Product")


if __name__ == "__main__":
    unittest.main()

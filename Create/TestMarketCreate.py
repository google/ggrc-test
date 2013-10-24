'''
Created on Jul 23, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestMarketCreate(BaseTestCreate):
    def testMarketCreate(self):
        self._create_test("Market")


if __name__ == "__main__":
    unittest.main()

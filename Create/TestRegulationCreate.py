'''
Created on Jul 18, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestRegulationCreate(BaseTestCreate):
    def testRegulationCreate(self):
        self._create_test("Regulation")


if __name__ == "__main__":
    unittest.main()

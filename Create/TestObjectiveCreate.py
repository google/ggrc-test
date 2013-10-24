'''
Created on Oct 17, 2013

@author: silas@reciprocitylabs.com
'''

from CreateBase import BaseTestCreate


class TestObjectiveCreate(BaseTestCreate):
    def testObjectiveCreate(self):
        self._create_test("Objective")


if __name__ == "__main__":
    unittest.main()

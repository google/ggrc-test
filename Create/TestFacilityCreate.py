'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestFacilityCreate(BaseTestCreate):
    def testFacilityCreate(self):
        self._create_test("Facility")


if __name__ == "__main__":
    unittest.main()

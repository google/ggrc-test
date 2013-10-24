'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestOrgGroupCreate(BaseTestCreate):
    def testOrgGroupCreate(self):
        self._create_test("OrgGroup")


if __name__ == "__main__":
    unittest.main()

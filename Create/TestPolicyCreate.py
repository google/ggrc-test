'''
Created on Jul 18, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestPolicyCreate(BaseTestCreate):
    def testPolicyCreate(self):
        self._create_test("Policy")


if __name__ == "__main__":
    unittest.main()

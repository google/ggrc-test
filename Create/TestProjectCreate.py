'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate


class TestProjectCreate(BaseTestCreate):
    def testProjectCreate(self):
        self._create_test("Project")


if __name__ == "__main__":
    unittest.main()

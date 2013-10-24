'''
Created on Jul 24, 2013

@author: diana.tzinov
'''

from CreateBase import BaseTestCreate

class TestDataAssetCreate(BaseTestCreate):
    def testDataAssetCreate(self):
        self._create_test("DataAsset")


if __name__ == "__main__":
    unittest.main()

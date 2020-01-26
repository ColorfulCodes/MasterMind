import unittest
from game import minWindow 


class TestAPI(unittest.TestCase):
    #test length of api return
 
    def testApiLength(self):
        self.assertEquals(randomApi(), 4)
    


if __name__ == '__main__':
    unittest.main()
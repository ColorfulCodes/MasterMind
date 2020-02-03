import unittest
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/codegem/code/masterMind/game')
import easy
from game import difficulty


class TestAPI(unittest.TestCase):
    #test length of api return
 
    # def testApiLength(self):
    #     self.assertEquals(len(randomApi()), 4)

    # def testPlaying(self):
    #     self.assertEquals(playing())

    def testDifficulty(self):
        result = difficulty('easy')
        print(result)
        self.assertTrue(len(result[0]) == 4 and result[1] == 0 and result[2] == 'four' and result[3]==10)
    
    


if __name__ == '__main__':
    unittest.main()
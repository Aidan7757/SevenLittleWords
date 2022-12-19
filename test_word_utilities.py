import unittest
from word_utilities import WordUtilities

class TestWordUtilities(unittest.TestCase):
    
    def test_slicer(self):
        util = WordUtilities()
        list1 = util.slicer("hellos")
        list1words = []
        for i in list1:
            list1words.append(str(i))
        self.assertEqual(["HEL", "LOS"], list1words)
        
        list2 = util.slicer("pray")
        list2words = []
        for i in list2:
            list2words.append(str(i))
        self.assertEqual(["PR", "AY"], list2words)
        
        list3 = util.slicer("prays")
        list3words = []
        for i in list3:
            list3words.append(str(i))
        self.assertEqual(["PRA", "YS"], list3words)

if __name__ == "__main__":
    unittest.main()
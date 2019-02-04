import unittest
from myFunctions import *
#from myFunctions import myFirstFunction
class TestMyFunctions(unittest.TestCase):

    def test_myFirstFunction(self):
        myFunctionsObj = myFunctions()
        self.assertTrue(myFunctionsObj.myFirstFunction())

    def test_reverseFunction(self):
	myFunctionsObj = myFunctions()
	string1 = "cars"
	string2 = "BART"
	string3 = "Isaac"		
	self.assertEqual(myFunctionsObj.reverseFunction(string1), "srac")
	self.assertEqual(myFunctionsObj.reverseFunction(string2), "TRAB")	
	self.assertEqual(myFunctionsObj.reverseFunction(string3), "caasI")	

    def test_acronymOf(self):
	myFunctionsObj = myFunctions()
	self.assertTrue(myFunctionsObj.acronymOf("My Aching Back") == "MAB")
	self.assertTrue(myFunctionsObj.acronymOf("The bees knees") == "TBK")
	self.assertTrue(myFunctionsObj.acronymOf("cat Scratch boogy") == "CSB")
	self.assertTrue(myFunctionsObj.acronymOf("Bay Area Rapid Transit") == "BART")

#    def test_triangleType(self, triangle):
#	myFunctionsObj = myFunctions()
#    def test_scrabble(self, word):
#	myFunctionsObj = myFunctions()
#    def test_standardizePhoneNumber(self, phoneNumber):
#	myFunctionsObj = myFunctions()
#    def test_occurrencesOf(self, phrase):
#	myFunctionsObj = myFunctions()

if __name__ == '__main__':
    unittest.main()

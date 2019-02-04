"""----------------------
Program: myFunctions.py
Date: 01/15/2019

Purpose: This file stores a number of methods that
    are tested using the unittest package (using driver)
-----------------------"""
class myFunctions():
   
    """
    * "None" is a special keyword in python equivalent to a null value
    * Make this method return True
    """
    def myFirstFunction(self):
        return None

    """
    * 1. write a method that reverses a String. 
    * Example: reverse("example"); -> "elpmaxe"
    """
    def reverseFunction(self, string):
        return None

    """
    * 2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
    * Acronyms)! Help generate some jargon by writing a program that converts a
    * long name like Portable Network Graphics to its acronym (PNG).
    * In the spirit of acronyms make sure the result in UPPER-CASE
    """
    def acronymOf(self, phrase):
        return None

#    """
#    * 4. Given a word, compute the scrabble score for that word.
#    * 
#    * --Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
#    * C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
#    * "cabbage" should be scored as worth 14 points:
#    * 
#    * 3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
#    * point for E And to total:
#    * 
#    * 3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14
#    """
#    def scrabble(self, word):
#        return None
#
#    """
#    * 5. Clean up user-entered phone numbers so that they can be sent SMS messages.
#    * 
#    * The North American Numbering Plan (NANP) is a telephone numbering system used
#    * by many countries in North America like the United States, Canada or Bermuda.
#    * All NANP-countries share the same international country code: 1.
#    * 
#    * NANP numbers are ten-digit numbers consisting of a three-digit Numbering Plan
#    * Area code, commonly known as area code, followed by a seven-digit local
#    * number. The first three digits of the local number represent the exchange
#    * code, followed by the unique four-digit number which is the subscriber
#    * number.
#    * 
#    * The format is usually represented as
#    * 
#    * 1 (NXX)-NXX-XXXX where N is any digit from 2 through 9 and X is any digit
#    * from 0 through 9.
#    * 
#    * Your task is to clean up differently formatted telephone numbers by removing
#    * punctuation and the country code (1) if present.
#    * 
#    * For example, each of the inputs:
#    * +1 (613)-995-0253 
#    * 613-995-0253 
#    * 1 613 995 0253 
#    * 613.995.0253 
#    *
#    * should all produce the output
#    * 
#    * 6139950253
#    * 
#    * Note: As this exercise only deals with telephone numbers used in
#    * NANP-countries, only 1 is considered a valid country code.
#    """
#    def standardizePhoneNumber(self, phoneNumber):
#        return None
#
#    """
#     * 6. Given a phrase, count the occurrences of each word in that phrase.
#     * 
#     * For example for the input "olly olly in come free" olly: 2 in: 1 come: 1
#     * free: 1
#     * 
#    """
#    def occurrencesOf(self, phrase):
#        return None


if __name__ == "__main__":
    myf = myFunctions()
    print myf.myFirstFunction()

    result = myf.reverseFunction("cool")
    print result
    result = myf.reverseFunction("racecar")
    print result

    result = myf.acronymOf("Know Your Neighbor")
    print result
    result = myf.acronymOf("Salt Lake City")
    print result

    

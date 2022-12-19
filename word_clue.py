"""Word clue class script.

This script contains the word class as well as different methods
that are contained inside the class. It uses the world utilities
class in the script.

Author: Aidan Chadha
Version: 12/4/2022
"""

from word_utilities import WordUtilities


class WordClue:
    """Word clue class.
    
    Attributes:
        MIN_WORD_LENGTH (int): minimum length of the word.
        MAX_CLUE_LENGTH (int): max length of the clue.
    """
    
    def __init__(self, word, clue):
        """Word clue constructor.

        Args:
            word (str): provided word.
            clue (str): clue for the word.
        """
        self.MIN_WORD_LENGTH = 4
        self.MAX_CLUE_LENGTH = 40
        self.word_slice = []
        
        if word is None or len(word) == 0:
            self.word = "DEFAULT"
        elif len(word) < self.MIN_WORD_LENGTH:
            self.word = "DEFAULT"
        else:
            self.word = word
        
        if clue is None or len(clue) == 0:
            self.clue = "DEFAULT CLUE"
        elif len(clue) > self.MAX_CLUE_LENGTH:
            self.clue = "DEFAULT CLUE"
        else:
            self.clue = clue

    def __eq__(self, other):
        """Equals method for the word clue class.

        Args:
            other: other word clue being checked.
        
        Returns:
            bool: if the words are equal or not.
        """
        lower1 = self.word.lower()
        lower2 = other.word.lower()
        return lower1 == lower2
    
    def get_clue(self):
        """Gets the clue from the object.

        Returns:
            clue (str): the objects clue.
        """
        return self.clue
    
    def get_first_letter_hint(self):
        """Returns first letter of the objects word.

        Returns:
            hint (str): first letter of the objects word.
        """
        first = self.word[0]
        hint = first.upper()
        return hint
    
    def get_first_slice_hint(self):
        """Returns the first slice of the objects word.

        Returns:
            hint (str): first slice of the objects word.
        """
        util = WordUtilities()
        list_slices = util.slicer(self.word)
        hint = str(list_slices[0]).upper()
        return hint
    
    def get_whole_word_hint(self):
        """Returns the whole word as a hint.

        Returns:
            word (str): the word.
        """
        return self.word.upper()
    
    def get_slices(self):
        """Obtains the slices for the given word.

        Returns:
            word_slice (list): the list of the word slices.
        """
        util = WordUtilities()
        list_slices = util.slicer(self.word)
        for i in list_slices:
            self.word_slice.append(i)
        return self.word_slice
    
    def get_word(self):
        """Gets the objects word.

        Returns:
            word (str): returns the string version of the word.
        """
        return str(self.word)
    
    def __str__(self):
        """String representation of the word clue class.

        Returns:
            string1 (str): string representation of the word clue class.
        """
        string1 = ""
        string1 += f'{self.word}-{self.clue}\n'
        list_slices = self.get_slices()
        for i in list_slices[:-1]:
            string1 += f'{str(i)} '
        string1 += f'{str(list_slices[-1])}\n'
        return string1


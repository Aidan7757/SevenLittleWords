"""Word utilities script.

This script creates the word utilities class and creates it's method
of slicer for creating the word slices.

Author: Aidan Chadha
Version: 12/2/2022
"""
from word_slice import WordSlice


class WordUtilities:
    """Word utilities class."""
    
    def slicer(self, word):
        """Slicer method.
        
        This method takes in a word and depending on the length of the word, creates
        different word slices.
        
        Args:
            word (str): word given.
            
        Returns:
            word_slice_objects (WordSlice[]): list of word slice objects.
        """
        word_slices = []
        word_slice_objects = []
        word_slice_strings = []
        length = len(word)
        word_upper = word.upper()
        
        if length % 3 == 0:
            amount_slices = length / 3
            num_slices = int(amount_slices)
            num_start = 0
            for i in range(num_slices):
                word_slices.append(word_upper[num_start:num_start+3])
                num_start += 3    
        elif length % 2 == 0:
            amount_slices = length / 2
            num_slices = int(amount_slices)
            num_start = 0
            for i in range(num_slices):
                word_slices.append(word_upper[num_start:num_start+2])
                num_start += 2 
        else:
            word_slices.append(word_upper[0:3])
            amount = (length - 3) / 2
            num_slices = int(amount)
            num_start = 0
            for i in range(num_slices):
                word_slices.append(word_upper[num_start+3:num_start+5])
                num_start += 2
        for i in word_slices:
            word = WordSlice(i)
            word_slice_objects.append(word)
    
        return word_slice_objects


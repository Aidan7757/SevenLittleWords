"""Script to create the information of the game class.

Author: Aidan Chadha
Version: 12/5/2022
"""


from file_utilities import FileUtilities
from word_utilities import WordUtilities
from word_clue import WordClue


class GameInfo:
    """Game info class, contains all information for the game.

    Attributes:
        NUMBER_OF_WORDS (int): number of words allowed.
        complete (bool): if the game is done or not.
        word_slices (list): list of word slices.
        cluelist (list): list of the clues that can be given.
        list_lines (list): lines read from the file.
    """
    
    def __init__(self, filename):
        """Game info constructor.

        Args:
            filename (str): name of file inputted.
        """
        self.NUMBER_OF_WORDS = 7
        self.complete = False
        self.word_slices = []
        self.cluelist = []
        self.list_lines = FileUtilities.read_lines_from_file(filename, self.NUMBER_OF_WORDS)
        
        util = WordUtilities()
        for i in self.list_lines:
            word_list = i.split("-") 
            self.word_slices.append(util.slicer(word_list[0]))
 
        for i in self.list_lines:
            word_list = i.split("-")
            clue = WordClue(word_list[0], word_list[1])
            self.cluelist.append(clue)
        
    def get_slices(self):
        """Method for accessing the slice strings for the board.

        Returns:
            slices (list): list of strings of the slices.
        """
        slices = []
        for i in self.word_slices:
            for j in i:
                slices.append(j)
        return slices
    
    def get_word_clues(self):
        """Method for accessing the clue strings for the board.
        
        Returns:
            cluelist (list): list of clues.
        """
        return self.cluelist
    
    def __str__(self):
        """String method for the game info class.
    
        Returns:
            string1 (str): the string representation of the game info class.
        """
        string1 = ""
        string1 += "Cluelist\n"
        for i in self.list_lines:
            string1 += f"{i}\n"
            
        string1 += "\nSlices\n"
        for i in self.word_slices:
            for j in i:
                string1 += f'{str(j)}\n'
        return string1
                
    def is_complete(self):
        """Method for making the game complete."""
        self.complete = True
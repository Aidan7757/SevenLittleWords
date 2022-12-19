"""Word slice class script.

This script creates the word slice class as well as its different methods
that are able to be used on a word slice.

Author: Aidan Chadha
Version: 12/2/2022
"""


class WordSlice:
    """Word slice class.

    Attributes:
        text (str): text of the word slice.
    """
    
    def __init__(self, text):
        """Initialize the word slice object.

        Args:
            text1 (str): text given for word slice.
        """
        self.used = False
        self.text = text
    
    def is_used(self):
        """Returns the used attribute of the object.
        
        Returns:
            self.used (bool): used attribute.
        """
        return self.used
    
    def reset(self):
        """Sets the used attribute to false."""
        self.used = False
    
    def __str__(self):
        """String representation of the object.

        Returns:
            str: blank if used, text attribute of object if unused.
        """
        if self.used:
            return ""
        else:
            return self.text
        
    def use(self):
        """Sets used attribute to true."""
        self.used = True
        
   
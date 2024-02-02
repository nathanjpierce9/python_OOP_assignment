"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    """ reads source file and reports # of words read"""
    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print (f"{len(self.words)} words read")

    """parse dict_file => list of words"""
    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    """ Return random word"""
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
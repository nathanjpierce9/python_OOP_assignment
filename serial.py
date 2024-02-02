"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """ Creates a new generator that begins at start. If start is not defined start is at 0 """
    def __init__(self, start=0):
        self.start = self.next = start

    """show repesentation"""
    def __repr__(self):
        return f"<SerialGenerator start = {self.start} next = {self.next}>"
    
    """ Return next serial number"""
    def generate(self):
        self.next += 1
        return self.next - 1

    """Reset serial number back to start"""
    def reset(self):
        self.next = self.start
        

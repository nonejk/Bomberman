""" has basis of all elements of the game
"""
class blocks():
    """ because pylint asked for it
    """
    tyype = 0
    symb = ''
    bombing = False
    destroyable = True

    def __init__(self):
        pass

    def set_attrs(self):
        """ returns whether element of particular type can be destroyed by bomb or not
        """
        des_dict = {
            0: True,
            1: False,
            2: True,
            3: True,
            4: False,
            5: True,
            6: False,
            7: False,
            8: False}
        self.destroyable = des_dict[self.tyype]

    def set_symb(self):
        """ setting the symbol to the element based on its type
        """
        sym_dict = {
            0: ' ',
            1: 'X',
            2: '%',
            3: 'E',
            4: '^',
            5: 'B',
            6: '3',
            7: '2',
            8: '1'}
        self.symb = sym_dict[self.tyype]


class elements(blocks):
    """ basic element functions
    """
    rowPosition = 0
    columnPosition = 0

    def def_element(self, number, row, column):
        """ defining the element type to be something
        """
        self.tyype = number
        self.rowPosition = row
        self.columnPosition = column
        self.set_attrs()
        self.set_symb()

    def element_type(self):
        """ returns the type of the element
        """
        return self.tyype

    def get_posi(self):
        """ because pylint asked for it
        """
        return (self.rowPosition, self.columnPosition)

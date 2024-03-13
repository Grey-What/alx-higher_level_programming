#!/usr/bin/python3
"""contains class definition"""


class MyInt(int):
    """subclass with inverted operators"""
    def __eq__(self, other):
        """represents the ++ operator and its boolean return

        Args:
             other (): value self will be compared too
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """represents the != operator and returns boolean of comparison

        Args:
             other (): value that will be compared too, using operator
        """
        return super().__eq__(other)

# -*- coding: utf-8 -*- 

from .parsers.parser import CsvMapParser

class Converter(object):
    """
    This is csv converter.
    """

    def __init__(self):
        self.__csv_map_parser = CsvMapParser()

    def convert(self, lines, start_row = 1, title_row = 0):
        """
        Parse lines of titles and data to array map.

        :Args
        - lines - two dimensional array of string.
        - start_row - start parsing data row index.
        - title_row - title row index.
        """
        return self.__csv_map_parser.parse(lines, start_row = start_row, title_row = title_row)


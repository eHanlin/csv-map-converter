# -*- coding: utf-8 -*- 

from .parser.CsvMapParser import CsvMapParser

class Converter(object):

    def __init__(self):
        self.__csv_map_parser = CsvMapParser()

    def convert(self, lines, start_row = 1, title_row = 0):
        return self.__csv_map_parser.parse(lines, start_row = start_row, title_row = title_row)


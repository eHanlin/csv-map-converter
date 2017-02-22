
#import csv
from .converter import Converter

converter = Converter()

def convert(lines, start_row = 1, title_row = 0):

    #if isinstance(type(lines), str):
    #    lines = [for line in csv.reader(lines)]

    return converter.convert(lines, start_row, title_row)


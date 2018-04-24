#!/bin/usr/python3

"""Extends the funtionality of the `ls` to Finder tags

Can read and output the colored tags of all files in the current directory or
of a given directory or file.
"""

class Tags:

    def __init__(self, file_path):
        self.tags = self.read(file_path)


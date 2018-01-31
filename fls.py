#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
fls.py

Terminal command that expands on the functionality of the `ls` command by grouping files
by their tags.

Attributes:
    TAGS_REF (string): the url of the `.plist` file containg the user's tags, and relevant
        tag info.
"""

import os
import sys

# import plistlib
# TAGS_REF = "~/Library/SyncedPreferences/com.apple.finder.plist"

def main(args):
    """ """


def parse_input(args):
    """ Determine the user intent by parsing the arguments passed """


def validate_flag(flag, args):
    """ Given a list of all valid flag patterns validate the user's passed
        flag """


def validate_input(args):
    """ Determine if the user's argument is a valid file or directory
        name """

def read_metadata(file_name):
    """ Execute a subprocess to read the metadata of a file or directory """


def output_help(context = None):
    """ Provide information about the module and it's functionality given
        some or no context to the user's intent """


def output_tags(TaggedObject):
    """ Tags a TaggedObject and ouputs its formatted tags to the shell """


class TaggedObject(object):
    
    def __init__(self, item_name):
        self.name = item_name
        self._tags = self.get_tags(item_name)
        self.tags = self.format_tags(self._tags)


    def get_tags(entity):
        """ Get the tags of a given file or directory """


    def format_tags(tag_string):
        """ Convert a given list of tags to the formated output for a file """


if __name__ == "__main__":
    main(sys.argv)    


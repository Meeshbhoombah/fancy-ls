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
import plistlib

TAGS_REF = "~/Library/SyncedPreferences/com.apple.finder.plist"

def read_file(file_url):
    """ Reads in a file as a file object

    Args: 
        read_file (string): takes in a string and reads in a file at that url's path
    Returns:
        file (file_object): returns a file as a file object
    """
    with open("~/Library/SyncedPreferences/com.apple.finder.plist", "r") as f:
        return f


def read_plist(file_object):
    """ Returns the contents of a file
   
    Args:
        file_object (file object): the file object to read contents from
    Returns:
        contents (list):
    """
    contents = file_object.read()
    return contents


if __name__ == "__main__":
    contents = read_plist(read_file(TAGS_REF))
    print(contents)


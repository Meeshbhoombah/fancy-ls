#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
fls.py

Terminal command that expands on the functionality of the `ls` command by grouping files by 
their tags.

Attributes:
    args (list): a list of the arguments passed in by the user where each argument is a string
        in the collection
"""

import os
import sys
import subprocess

def main(args):

    # get only the first argument, can be file/dir
    # path or help tag
    user_input = args[1]

    # tag
    if user_input[0] == "-":
        print("Help")

    # file or directory
    elif os.path.isdir(user_input) or os.path(user_input):
        # readability
        path = user_input

        # call mdls on file path
        file_metadata = subprocess.check_output(["mdls", path])

        # find all tags from metadata
        try:
            tags_index = file_metadata.find("kMDItemUserTags")
        except ValueError:
            print(ValueError)

        # get only tags
        tags = file_metadata[tags_index:]

        # parse tags metadata
        tags = tags.split()

        # remove ending delimiter
        tags.pop()

        # get only tags and ending delimiter
        tags = tags[3:]
       
        # print all the tags
        for tag in tags:
            print(tag)
        
    else:
        print("Not a valid argument, file or directory required.")

if __name__ == "__main__":
    main(sys.argv)    


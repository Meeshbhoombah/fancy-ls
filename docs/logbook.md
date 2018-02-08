# Fancy ls
For programmers, the terminal is more than just a tool. It's our home. For some, it's our de
facto interface of choice. Give us access to your version of that familiar black screen 
with it's friendly flashing cursor and we'll find endless hours of joy and gigabytes of 
information about you that you probably never wanted us to know.

After generally being mistified by its exitance we come to love our shells. Do you have a 
favorite terminal command? Perhaps reconsider your priorities if your answer to that question 
was yes, but before you do that, let me recount my findings on my favorite terminal command, 
`ls`, and how I extended its functionality with my groundbreaking project:

**fls**

Did that intro  feel overhyped? Kind of like most ICOs out there right now. I'm just playing 
the game.

## Inception
Like most great ideas, fls was birthed out of sheer necessity. I had work due for a class in
less than twenty-four hours and it was absolutely necessary for me to find  a way to 
procrastinate and prevent myself from completing that work. I have such self-distructive 
habits. 

Luckily, I had recently been on an organization binge and had developed a tagging system 
for my files that utilzied OS X's in-built tagging system. However, More often than not, I
would be typing away at my terminal. The Finder tagging system would go underutilized. All 
my effort was lost as there was no way to display tags in the shell.

The combination of my incessant want to organize and incredulous need to procastinate spurred
me to action, I  quickly found out that there were ways to programatically access the tags 
of files in a directory, so I decided that I had to implement the ability to categorize
files in a directory by their tags. I had initally thought that I wanted to extend the 
functionality of `ls`, perhaps using a flag to display the unique format, but I decided
to opt for a whole new command instead, `fls`, or **FANCY ls** because it would mean
less overall keystrokes (`ls -f` vs `fls`). 

## BUT FIRST... `ls`: A History
Before I dove into messing around with the `ls` command I decided to honor its legacy by
taking a look at its past. Where did `ls` come from?

1. http://www.tldp.org/LDP/LG/issue48/fischer.html
2. https://en.wikipedia.org/wiki/Ls

## Pre-Processing
I build projects incrementally as I find it is the easiest way for me to not get lost in
the multistep process and complete tasks as effectively and succintly as possible. Here 
are the incremental steps I decided on:

1. `fls` in any dir prints "Hello World!"
2. `fls` prints the tags of current dir
3. `fls` categorizes files by tags and prints them
4. `fls` looks aesthetic

## Implementation
Given that I was looking to get this done quickly, my goal with the first pass of the project
was to build a workable version that accomplished the tasks in mind. I plan to optimize my
project later after I build it the first time.

After creating a new directory, `fls`, and initalizing Git, I added Vim extensions to my
`.gitignore`. I then created a virtual environment to work in using `virtualenv`.
```bash
$ virtualenv venv
New python executable in /Users/rohan/Desktop/venv/bin/python
Installing setuptools, pip, wheel...done.
```
Which I can then activate
```bash
$ source venv/bin/activate
New python executable in /Users/rohan/Desktop/venv/bin/python
Installing setuptools, pip, wheel...done.
(venv) $ |
```
Afterwards I created a new file inside `fls` named `fls.py`. 

I like to follow Google's [Doctring example](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) 
and [Python Style Guide](https://google.github.io/styleguide/pyguide.html). As such, the first
thing I added to the file was the docstring. Clean code >> and often revisiting projects has
given me this habit.
```python
# -*- encoding: utf-8 -*-

"""
fls.py

Terminal command that expands on the functionality of the `ls` command by grouping files
by their tags.
"""
```

###  "Hello, World!"
After that I decided to tackle the first incremental step:
1. **`fls` in any dir prints "Hello World!"**
2. `fls` prints the tags of current dir
3. `fls` categorizes files by tags and prints them
4. `fls` looks aesthetic

Let's break it down further:
1. Running `python fls <args>` should print all args passed.
```bash
$ python fls.py "Hello, World!"
fls.py
"Hello, World!"
```
2. Running `fls <args>` in any directory should print args.
```bash
$ fls "Hello, World!"
"Hello, World!"
```

Using the in-built `sys` module made the first step simple to solve.
```python
import sys

def print_input(args):
    """ Print Hello World to the Terminal"""
    print(arg)

if __name__ == "__main__":
    for arg in sys.argv:
        print_input(arg)
```

Executing the command in any terminal would require me to mark the Python script as an 
executable file in the system.
```bash
$ chmod +x fls.py
```
This would be like right-clicking on a script and clicking **Properties** > **Permissions** >
**Allow executing file as program**. 

Now I can run the file from the command line.
```
$ ./fls "Hello, World!"
```
The command is prefixed with a `./` because the current directory is not a part of the 
Unix `PATH` environment variable. The `PATH` variable tells the shell which directories should
be searched in order to find commands in response to the command issued by the user.

The file is not a part of the shell like `ls`, `cd`, etc. These commands are called 
`built-ins` and can be easily found by the shell. However, `executables`, which can take form
as a shell script or a compiled program, require further direction to be found 
by the shell. 

My file is a compiled program, therefore, I need to provide the shell with
more information in order for it to find the command. The `PATH` variable does not include
subdirectories of the `root` directory, which it can access. The shell can be informed in
an abbreviated way through the usage of the `./` command.

I could just append a `./` to the start of my `PATH` enviroment variable, as it would tell
the shell to also search the current directory, but this should be avoided for security 
concerns and well as safety. If I were to inadverdently create a command that has the same
name as an existing shell command the shell may accidentally execute the command I created,
which probably would result in **absolute chaos**. I am normally a fan of **abosolute chaos**,
but today I am feeling neutral good.

However, when I ran the command to execute my file.
```bash
$ ./fls "Hello, World!"
```

I instead got a gnarly error.
```bash
./fls.py: line 8: 
fls.py

Terminal command that expands on the functionality of the LICENSE
fls.py
logbook.md
readme.md
venv command by allowing tagged
sorting of cateogries.
: command not found
./fls.py: line 10: import: command not found
./fls.py: line 12: syntax error near unexpected token `('
./fls.py: line 12: `def print_input(args):'
```
Weird, right? Seems like the command is really confused as to what my file is, and how to
execute it. 

That's because I have not informed the shell to execute my file as Python script.
Wow, we really have to conform to the shell's rules. I guess you could say it runs this whole
**shebang**, which is a great transition to the next step.
```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
...
```
Adding a **shebang** to `fls.py`.

Whenever a file is ran on a Unix based system (like my Mac, which has macOS Sierra), the
interpreter checks the file for an interpreter directive, which are also known as shebangs
in Unix jargon. 

I'm using the enviroment to load the Python interpreter because it allows me to run the script
on different systems, where Python may be installed in a different location. Running the file
should work as expected.
```bash
$ ./fls.py "Hello, World"
./fls.py
"Hello, World"
```

Using the shebang also allows me to drop the `.py` file extension, which makes **fls** look
even more like a terminal command.
```bash
$ ./fls "Hello, World"
./fls
"Hello, World"
```

The final step to making **fls** look real is to add it to my `PATH` so that it can be ran by
simply typing `fls`. To avoid naming conflictions and other issues, and to group this command
with other commands I plan to create in the future, I will create a seperate `bin` in my `HOME`
directory. Not doing this could also cause me to break my installation of my operating system.
Better safe than sorry.
```bash
$ mkdir -p ~/bin
```

I'll copy my script there.
```bash
cp fls ~/bin
```

Then add `~/bin` to my `PATH`. To make this command available across terminal sessions I 
need to create to `export` the path each time the terminal fires, which I can do easily by
adding it to my `.bash_profile`.
```bash
export PATH=$PATH":$HOME/bin"
```
After restarting the shell I can then run the command.
```bash
$ fls Hello, World
/Users/rohan/bin/fls
Hello, 
World
```

[Here's what my script looks like up to this point.](https://github.com/Meeshbhoombah/fls/blob/146409a305fb9c16a44d48625f6679b8a030dacb/fls.py)
Magical.

## Tag City
Now that I can run the command in any directory it is time for me to tackle the second step:
1. `fls` in any dir prints "Hello World!"
2. **`fls` prints the tags of current dir**
3. `fls` categorizes files by tags and prints them
4. `fls` looks aesthetic

### Breakdown
1. `fls <file_name>` should list all the tags of that file
```bash
$ fls go/
workspace
```

2. Running `fls` without a specefied `<file_name>` prints out all the files in the current 
directory in alphabetical order.
```bash
Rohan-MacBook-Pro:working rohan$ fls
augment
cs
fls
go
lab
makeschool
```

3. Running `fls -t` prints out all the tags of files in the current directory in alphabetical
order.
```bash
Rohan-MacBook-Pro:working rohan$ fls
makeschool
personal
workspace
```

### Hacker, not Pefectionist 💀
First, I need to locate the tags. After some Googling I found a built in mac command,
`mdls`, which stands for "metadata list." This lists, as one might guess, the metadata 
attributes of a given file. I feel like it would be wise to try it out in the shell before 
I started working with it in Python.

In my root directory I have a subdirectory called `working` where I store all my code. I have
this divided into three seperate branches Here's
what it looks like in Finder.

![finder preview](https://github.com/Meeshbhoombah/fls/blob/dev/docs/imgs/finder_preview.png)

Doing mdls <directory_name> in this directory returns a the values of that file's Core Service
Constants, which are variable's used by macOS to access and manage key operating system
services, such as launch or identity services.
```bash
Rohans-MacBook-Pro:working rohan$ mdls fls/
_kMDItemOwnerUserID            = 501
kMDItemContentCreationDate     = 2018-01-21 19:58:15 +0000
kMDItemContentModificationDate = 2018-01-30 09:01:32 +0000
...
kMDItemKind                    = "Folder"
kMDItemUserTags                = (
    personal
)
```
These constants provide details about certain file attributes. The `kMDItemContentCreationDate`
is the `DateTime` value of when the file was created, and as you can see here, we 
also have a list of the tags that the file has through the `kMDItemUserTags` constant.

Using the `subprocess` module, which is a part of Python's standard library, I can execute
terminal commands inside a script and read in their ouput as a series of lines. The `subprocess`
module allows me to run a new instance of the shell, it specfically contains the function
`check_output` which allows me to pass in a command and an argument and then recieve the 
result of the argument as a string. Through this, I can parse the `kMDItemUserTags` constant,
and output its list of values to the terminal.
```python
...
import os
import sys
import subprocess
```
The `os` module has a function to help me validate a file or foldername. This will give my 
command line tool better usability. Before I do this I'll restructure the arguments input to
provide better functionality for users as well as a help function. 

I've reset the file down to it's barebones file structure save:
```python
...
import subprocess

def main(args):
    """ Parse user input and execute command """


if __name__ == "__main__":
    main(sys.argv)    
```

First I will parse the arguments passed in by the user to get the directory or file that we
need to extract the text of, or to print information to the user if they require help.
```python
def main(args):
    ...
    # get only the first argument, can be file/dir
    # path or help tag
    user_input = args[1]
```

For now, I just want my command line tool to print some general help text, so I'll check if
a tag is passed and print the help text if it is. I'll use "Help" as a placeholder for now.
```python
user_input = args[1]

# tag
if user_input[0] == "-":
    print("Help")
```

If that's not the case, I'll check if it's a file or directory using the `os` module which
I had mentioned earlier.
```python
    ...
    print("Help")

# file or directory
elif os.path.isdir(user_input) or os.path(user_input):
```

In the case that it is not, I want to inform the user that the argument passed was not a valid
file or directory.
```python
...
else:
    print("Not a valid argument, file or directory required.")
```

Now I'll go back to my `elif` statement and call `mdls` on my path using the `subprocess`
using the function from the `subprocess` module. I'll store the output of the call.
```python
...
elif os.path.isdir(user_input) or os.path(user_input):
    # readability
    path = user_input

    # call mdls on file path
    file_metadata = subprocess.check_output(["mdls", path])
```

I know, from calling `mdls` on files and directories in my shell, that the constant I am
looking for, `kMDItemUserTags`, generally appears at the end of the list of constants. To 
speed up the process of splitting the outputs, which were returned to me as a string, I'll
call `rfind` as opposed to the normal `find` method. This starts searching for a given pattern
from the rightmost character of the string.
```python
...
# find all tags from metadata
    try:
        tags_index = file_metadata.rfind("kMDItemUserTags")
    except ValueError:
        print(ValueError)
```
Good error handling saves lives. I would like to also point out that good is subjective, as
I know some may have complaints about the way I handled this error.

The methods `find` and `rfind` return the index at where the pattern matches, so I used
that to split the metadata output.
```python
    ...
    print(ValueError)

# get only tags
tags = file_metadata[tags_index:]
```

After that I split the string further which enabled me iterate over each tag and print it out 
to the user.
```python
...
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
```

After I copy the contents of the script to the executable I created located at `~/bin/`, I 
can run `fls` and print the tags of any file.
```bash
$ cp fls.py ~/bin/fls
$ fls ../fls/
personal
```
Great! The script prints the tags of a given file or directory.

#### Virtual Environment Bug
I decided to take a break after implementing this and deactivated the virtual environment in
which I had been writing my code. After running my command without a virutal environment
I got an error that would not occur in an active virtual environment.
```bash
$ python fls.py ../fls/
Traceback (most recent call last):
  File "fls.py", line 63, in <module>
    main(sys.argv)    
  File "fls.py", line 39, in main
    tags_index = file_metadata.rfind("kMDItemUserTags")
TypeError: a bytes-like object is required, not 'str'
```
From the error, I guessed that the method `check_output` in the `subprocess` module, which I
used to call the `mdls` function may not have been doing what I thought it did. I decided to
check Python's standard documentation again to affirm this.

![check output](https://github.com/Meeshbhoombah/fls/blob/dev/docs/imgs/check_output_screenshot.png)

Oops. Luckily this is a quick fix, I can convert the bytes-like object (a bytes string) 
to a string after the `check_output` call.
```python
...
file_metadata = subprocess.check_output(["mdls", path])

# convert bytes string to string
file_metadata = str(file_metadata, "utf-8")
```
Running the command in the terminal now prints the expected output. When I copied the contents
of the file over to my `bin` the script worked as expected.
```bash
$ python fls.py ../fls/
personal
```
How the fuck was it working before?

#### Regularly Scheduled Programming
I need to print all files in the current directory if no `<file_name>` is passed as an
argument. The simplest way to do this is to use the `glob` module to return an iterator of
all the files and directories in a given directory.
```python
def main(args):

    # check if args are passed
    try:
        args[1]
    except IndexError:
        # if no args are passed print every file in 
        # cwd (current working directory)
        cwd = os.getcwd()
        
        for file_name in glob.iglob(cwd + "/*"):
            print(file_name)
        
        return

    # get only the first argument, can be file/dir
    # path or help tag
    user_input = args[1]
    ...
```
This grabs all the files in the current working directory but also grabs the entire filepath
to for each file. I want to just print the file name.
```python

```


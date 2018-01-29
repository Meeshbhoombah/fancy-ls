# Fancy ls
For programmers, the terminal is more than just a tool. It's our home. For some, it's our de
facto interface of choice. Give us access to your version of that familiar black screen 
with it's friendly flashing cursor and we'll find endless hours of joy and gigabytes of 
information about you that you probably never wanted us to know.

After generally being mistified by its exitance we come to love our shells. Do you have a favorite 
terminal command? Perhaps reconsider your priorities if your answer to that question was yes, 
but before you do that, let me recount my findings on my favorite terminal command, `ls`, and how
I extended its functionality with my groundbreaking project:

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

## Implmentation
After creating a new directory, `fls`, and initalizing Git, I added Vim extensions to my
`.gitignore`. Afterwards I created a new file inside `fls` named `fls.py`. 

I like to follow Google's [Doctring example](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) 
and [Python Style Guide](https://google.github.io/styleguide/pyguide.html). As such, the first
thing I added to the file was the docstring. Clean code >> and often revisiting projects has
given me this habit.
```python
# -*- encoding: utf-8 -*-

"""
fls.py

Terminal command that expands on the functionality of the `ls` command by allowing tagged
sorting of cateogries.
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
$ fls.py
$ "Hello, World!"
```
2. Running `fls <args>` in any directory should print args.
```bash
$ fls "Hello, World!"
$ "Hello, World!"
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

Executing the command in any terminal would require me to mark the Python script as an executable
file in the system.
```bash
$ chmod +x fls.py
```
This would be like right-clicking on a script and clicking **Properties** > **Permissions** >
**Allow executing file as program**. 

Now I can run the file from the command line.
```
./fls "Hello, World!"
```
The command is prefixed with a `./` because the current directory is not a part of the 
Unix `PATH` environment variable. The `PATH` variable tells the shell which directories should
be searched in order to find commands in response to the command issued by the user.

The file is not a part of the shell like `ls`, `cd`, etc. These commands are called 
`built-ins` and can be easily found by the shell. However, `executables`, which can take form
as a shell script or a compiled program, require further direction for them to be found 
by the shell. My file is a compiled program, therefore, it we need to provide the shell with
more information in order for it to find the command. The `PATH` variable does not include
subdirectories of the `root` directory, which it can access. The shell can be informed in
an abbreviated way through the usage of the `./` command.


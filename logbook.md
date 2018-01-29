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

## Implementation
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

Executing the command in any terminal would require me to mark the Python script as an executable
file in the system.
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

Here's what my script looks like up to this point.

Magical.

# Tag City
Now that I can run the command in any directory it is time for me to tackle the second step:
1. `fls` in any dir prints "Hello World!"
2. **`fls` prints the tags of current dir**
3. `fls` categorizes files by tags and prints them
4. `fls` looks aesthetic

First, I need to locate the tags. After some Googling I found that **tags** are located in a
`.plist` file at `~/Library/SyncedPreferences/com.apple.finder.plist`. Opening this in Vim
gave me a ton of gibberish. So I decided to use Python's in-built module to access `.plist`
files. I also need to `import os` so that I can work with files.
```python
import os
import sys
import plistlib
...
```
I know right? What **can't** Python do? I'm just as suprised as you are.


# Fancy ls
For programmers, the terminal is more than just a tool. It's our home. For some, it's our de
facto interface of choice. Give us that familiar black screen with it's friendly flashing cursor
and we'll find endless hours of joy and gigabytes of information about a person we probably 
never wanted to know (pro-tip: don't poke around other people's computer's because you'll 
be horrified).

Such a tool can really find it's way into our hearts. Do you have a favorite terminal command? 
Perhaps reconsider your priorities if your answer to that question was yes, but before you do 
that, let me tell discourse my findings on my favorite terminal command, `ls`, and how
I extended its functionality with my groundbreaking project:

**fls**

Did that feel overhyped? Sorry, I promise this isn't an ICO. Maybe next time. 

## Inception
Like most great ideas, fls was birthed out of sheer necessity. I had work due for a class in
less than twenty-four hours and it was absolutely necessary that I found a way to procrastinate
and prevent myself from completing the work. I have such self-distructive habits. I had
recently been on an organization binge and had developed a tagging system for my files
that utilzied OS X's in-built tagging system. 

But more often than not, I was using Terminal over Finder. I am a programmer after all, or so
I like to think. All my effort was lost as there was no way to display tags in the shell.

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
are the incremental steps I decided on for **fls**:

1. `fls` in any dir prints "Hello World!"
2. `fls` prints the tags of current dir
3. `fls` categorizes files by tags and prints them as dicts
4. `fls` looks aesthetic

I had never built a terminal application before so after doing some Googling around I found
a command line tool called [Click](http://click.pocoo.org/5/), which is a Python 
library written by the creator of Flask, [Armin Ronacher](https://twitter.com/mitsuhiko). 
Click stands for "Command-line Creation Kit". Those words matched some of the words 
I had in my brain when thinking about building this so I guess it is a good fit.


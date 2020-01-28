# How to set up your development environment

You will need to install several programs in order to create an environment in which you can write code.

* A terminal/command line
* `git` for version control
* `ssh` for SSH keys
* `python3` for programming
* `make` (optional) for running test suite, documenting/automating commands
* A text editor like `vi`, `emacs`, `pico`, Notepad, Sublime, TextWrangler, TextMate or an IDE (integrated development environment) like PyCharm, Microsoft VSCode, Spyder

Most of the examples I show will use the command line, but it may be possible to use graphical user interfaces (GUIs) for some of these such as Git Desktop instead of `git`.
Note that the `~` is a shortcut to your `$HOME` directory.

# Terminal

If you are on a Mac, then you can use the native `Terminal` application.
Alternatively, you might find the `iTerm2` terminal app a bit nicer.

If you are on a Windows machine, you should install some sort of command line:

* Cygwin: https://www.cygwin.com/
* Windows Subsystem for Linux https://docs.microsoft.com/en-us/windows/wsl/install-win10

# Installing Python

It's quite likely you already have Python installed.
Execute this to see if it is, and, if so, what version you have:

```
$ python3 --version
Python 3.7.3
```

Python version 2 moved to "end of life" at the end of 2019, meaning that version of the language will no longer be maintained and updated.
Still, it's quite likely that if you execute `python` on your system, it will be version 2:

```
$ python --version
Python 2.7.16 :: Anaconda, Inc.
```

Therefore I will always use `python3` to invoke the language.
If you have `python3` version 3.6 or higher, you're (probably) fine.
The latest version is 3.8, and it has some nice features you may eventually need.
I don't believe any of the material will require anything newer than 3.6.

If you don't have Python installed, then you can download Python from https://www.python.org/downloads/ and install using the instructions there.

You may also like to use the Anaconda distribution at https://www.anaconda.com/distribution/. 
I personally like Anaconda because of the `conda` tool that helps you install modules and also because it includes many non-standard modules like Pandas and Sci-Kit Learn by default, none of which we need for this class.
The full Anaconda distribution also includes the "Spyder" tool to help you write and debug Python code.

# Installing Python modules

We will use some tools and modules that may not be installed on your system including:

* `pytest`: a module for finding and running code tests
* `pylint`: a "linting" tool to help find problems in your code and suggest improvements
* `flake8`: another linter
* `mypy`: a tool for analysing Python's optional type hints

Each of these should be installable using Python's `pip` module, e.g.:

```
$ python3 -m pip install pytest pylint flake8 mypy
```

If you used the Anaconda distribution, you can use the `conda` tool, e.g.:

```
$ conda install flake8
```

# Editing code

Python code must be written as _plain text_, so you cannot use something like Microsoft Word.
Your choice of editor is a deeply personal one, and religious wars typically result from claiming that your editor is in any way better than someone else's.
Ken's personal preference is for `vi`, a terminal-based editor, but most people would prefer something fancier like VSCode or Spyder.
You should try different tools and choose the one that works best for you.
I might suggest you start with VSCode as it works on both Windows and Mac quite well.

IDEs:

* PyCharm
* VSCode
* Spyder

Editors:

* Spyder
* TextWrangler
* Sublime Text
* TextMate
* Notepad++ (Windows)

# Indentation

Python uses whitespace to denote code structure.
Indentation is used to group individual statements into "blocks."
You can indent either with Tab characters or spaces, but you must be consistent.
I would strongly recommend you only use spaces, but, again, this is territory for religious wars.
Any sufficiently advanced code editor can turn the press of the `Tab` key into spaces.

The number of spaces thou shall indent is four.
Four is the number of spaces, and the number of the spaces is four.
Five thou shalt not indent, neither indentest thou three unless, of course, thou proceedest to four.
Six is right out!

# `new.py`

In your clone of the repo, there is a `bin` directory that contains the program `new.py`.
You can use this program to create new programs.
You can execute it by giving the full path to the program, e.g., to create the `crowsnest.py` program:

```
$ cd ~/work/biosystems-analytics-2020/exercises/crowsnest
$ ~/work/biosystems-analytics-2020/bin/new.py crowsnest.py
```

Alternately, there is an environmental variable called `$PATH` on your system which is a colon-delimited list of directories where the operating system will look for programs.
You can copy `new.py` to one of those directories, and then you should be able to execute `new.py` from any directory without having to reference the full path.

Another option is to add the directory where `new.py` lives to your `$PATH`.
E.g., if the program is located in `~/work/biosystems-analytics-2020/bin`, then edit your `~/.bashrc` to add it like so:

```
export PATH=$HOME/work/biosystems-analytics-2020/bin:$PATH
```

As you write and install more programs that you wish to use, you may find yourself adding many directories to `$PATH`.
In that case, it may be nicer to create something like `~/.local/bin` for the programs and adding that as above.

If you don't wish to use `new.py`, you can copy `exercises/template/template.py` to start off a new program, e.g.:

```
$ cd ~/work/biosystems-analytics-2020/exercises/crowsnest
$ cp ~/work/biosystems-analytics-2020/template/template.py crowsnest.py
```

You can, of course, choose to start from nothing.
The `new.py` and `template.py` options are there to save you from typing common boilerplate code that will be expected of every program.

# Assignments

The procedure for assignments:

* `cd ~/work/biosystems-analytics-2020`
* `git pull upstream master`
* `cd assignments/new_assigment`
* Write the new program, pass all the tests.
* `git add new_program.py`
* `git commit -m passing new_program.py`
* `git push`

Verify that you can see `new_program.py` in _your repository_ on GitHub.com.

# Slack

Slack is a chat program.
If students would like, we can create a Slack channel for the class to make it easier for us to communicate with each other.
Your instructors are generally on Slack, so it's a more immediate way to interact than email.
You can also chat with each other.
We encourage you to discuss the material with each other, but *we strongly discourage sharing solutions*!
Please do not cheat on assignments.

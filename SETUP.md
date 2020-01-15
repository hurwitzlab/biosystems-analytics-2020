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

# GitHub Account

* Go to http://github.com and create an account.
* Email your GitHub username to your instructors (bhurwitz, kyclark).

# Set up SSH Keys

SSH stands for "secure shell" and is a protocol for encrypting communications with remote systems.
You will need an SSH key pair which can be found in two text files that contain your "public" and "private" keys.
We will add your public key to your GitHub settings so that you can securely communicate with the GitHub.com server without having to authenticate with a username and password.

* Open a terminal
* Execute `ls ~/.ssh`
* If you see `No such file or directory`, then execute `ssh-keygen`, hit `Enter` to accept all defaults
* You should have two files at least like `id_rsa` and `id_rsa.pub` which represent an SSH key pair. The `.pub` file contains the _public_ key which you need to copy to GitHub. The other file is your _private_ key that you should never touch, copy, use, or email. If that key is compromised, you should delete the files and use `ssh-keygen` to generate a new pair. You can generate as many pairs as you like, saving them into different files.
* Copy the contents of `~/.ssh/id_rsa.pub`. On a Mac, you can do `pbcopy < ~/.ssh/id_rsa.pub`. Otherwise, you can use `cat ~/.ssh/id_rsa.pub` to "concatenate" the contents to the screen, then copy the text to your clipboard.
* On GitHub.com, go to your user settings by clicking on your name/icon in the upper-right corner to view a drop-down list. Click on "Settings" (2nd from the bottom of the list).
* In the left side, there is a table. Click on "SSH and GPG keys".
* Click on the big green "New SSH Key".
* Give your key a name like "laptop" and paste in the _public_ key value. 
* Click the big green "Add SSH key" button.

# Forking the repo

* Go to https://github.com/hurwitzlab/biosystems-analytics-2020
* Click on the "Fork" button in the upper-right of the page, just below the big black bar.
* Fork into _your_ repository.
* Verify that you have something like https://github.com/id/biosystems-analytics-2020 where `<id>` is _your GitHub username_.

# Install `git`

`git` is a source-code versioning tool.
It keeps track of your code and all the changes you make to it.
You will use `git` to get access to all course materials including assignments.
You will also use `git` to turn in your work, so you must learn how to use `git`!
It's unlikely you have this program installed.
There at least two options:

* Use https://desktop.github.com/
* Use `git` directly on the command line

If you are on a Mac, you will probably need to install XCode in order to use `git` on the command line.
Try to execute `git` and see what you get. 
If you are prompted to install XCode, do so.
If you see something like `usage: git`, then you're good to go.

If you are on a Windows machine, see https://git-scm.com/download/win.

# Clone the repo 

* Use GitHub Desktop to clone your repo onto your machine

Alternate instructions for command line:

* Go to _your_ GitHub repo for the class, e.g., https://github.com/id/biosystems-analytics-2020. Be sure it is _NOT THE HURWITZLAB_ repo.
* Click on the green "Clone or download" button.
* Choose the SSH URL if you have set up SSH keys; otherwise choose the HTTPS version.
* Open a terminal
* You are likely in your `$HOME` directory, AKA `~` (twiddle)
* Decide where you will put your work, e.g., I always use `~/work`
* Create that directory if you do not have it, e.g., `mkdir ~/work`
* Change into that directory, e.g., `cd ~/work`
* Execute `git clone <URL>` where `<URL>` is the SSH or HTTPS URL that you copied from the "Clone or download" interface
* You should now have a `biosystems-analytics-2020` directory, e.g., `ls ~/work/biosystems-analytics-2020` should show you the contents of the directory.

# Set an upstream repository to get updates

In order to get updates from the HurwitzLab copy of the repo, you must set it as an "upstream" repository.

* Change into your local repo checkout, e.g., `~/work/biosystems-analytics-2020`
* Execute `git remote add upstream https://github.com/hurwitzlab/biosystems-analytics-2020.git`

# Using `git`

Whenever you need to get updates from the HurwitzLab version of the repo, e.g.,to get the latest assignments, you will execute `git pull upstream master` in your local repository.
This will "pull" any changes from the HurwitzLab repo into your fork.

To turn in your assignments, you will need to add the programs you create.
For instance, for the "Crow's Nest" exercise, you will create a program called `crowsnest.py`.
To add this file to your repo, you will do:

```
$ git add crowsnest.py
```

If you make any changes to that program, you will will `git add` it again.
You can and should do this often as each `add` creates a new version of the program in `git`, meaning you can see how you changed the program over time.

When you are ready to turn in your assignment, you will commit all the changes:

```
$ git commit -m "passing all tests" crowsnest.py
```

`git` requires a commit message.
It's easiest to supply one with the `-m` option.
If you fail to supply this, you will most likely be put into an editor to create a commit message that will be used once you save and exit the program.
The prompt will look something like this:

```

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#       new file:   foo
#
# Untracked files:
#       ../../SETUP.md
#
```

The editor is likely to be `vi` (or `vim`), and you will probably have no idea how to save and exit the text.
If you want to use `vi`, then press `i` to enter the "insert" mode, type some text, press `Esc` to enter "command" mode, then type `ZZ` to save and exit.
Or just type `EscZZ` to exit without saving anything and go back and use the `-m` option.

The actions of `add` and `commit` affect only your _local_ repository.
You still need to "push" your commits to GitHub:

```
$ git push
```

**If you cannot see your commits in the web interface at GitHub.com, then you haven't turned in your work yet.**

To grade your assigments, I will use `git pull` to pull down the changes from GitHub.com to my machine.
I will run the test suite.
Your grade will be the percentage of passing tests, so if you passed 80% of the tests, then your grade is 80% of the points for the assignment.

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

# Editing code

Python code must be written as _plain text_, so you cannot use something like Microsoft Word.
Your choice of editor is a deeply personal one, and religious wars typically result from claiming that your editor is in any way better than someone else's.
Ken's personal preference is for `vi`, a terminal-based editor, but most people would prefer something fancier like VSCode or Spyder.
You should try different tools and choose the one that works best for you.
I might suggest you start with VSCode as it works on both Windows and Mac quite well.

# Indentation

Python uses whitespace to denote code structure.
Indentation is used to group individual statements into "blocks."
You can indent either with Tab characters or spaces, but you must be consistent.
I would strongly recommend you only use spaces, but, again, this is territory for religious wars.
Any sufficiently advanced code editor can turn the press of the `Tab` key into spaces.

The number of spaces you indent should be four.
Four is the number of spaces, and the number of the spaces is four.
Five thou shalt not indent, neither indentest though three unless, of course, you proceedest to four.
Six is right out!

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

# Intro to Git

We will use a source code versioning system called Git that was created by Linus Torvalds, the creator of the Linux operating system, to manage the source code for Linux.
It's a deeply complex and powerful system with a dizzying number of commands and options, very few of which we'll use (cf https://xkcd.com/1597/).

TL;DR:

* `git clone`: to initially checkout a repository from a remote location like GitHub.com
* `git add`: to add a new or modified file to the index.
* `git commit`: to tell Git to commit a new version of the file. Do this often!
* `git push`: to send your changes from your laptop to a remote repository like GitHub.com
* `git pull`: to import changes from a remote location like the course GitHub repo
* `git status`: tells you info on your repo
* `git stash`: if you have local changes that conflict with changes you are trying to pull, you can "stash" your local mods and let the `pull` continue
* Merge conflict: if two people have modified the same file in the same place, Git is unable to merge the changes into one unified file. This creates a "merge conflict" where all the changes are put into the one file and you must sort out the lines to keep.

## GitHub Account

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

# Add collaborators

You will need to add your instructors as "Collaborators" on the course repo.

* At GitHub.com, select your "biosystems-analytics-2020"
* Choose the "Settings" for the repository (not your personal settings"
* Choose "Collaborators" from the left-hand menu
* Type GitHub IDs "bhurwitz33" and "kyclark" into box, click "Add collaborator"

# Using `git`

Whenever you need to get updates from the HurwitzLab version of the repo, e.g.,to get the latest assignments, you will execute `git pull upstream master` in your local repository.
This will "pull" any changes from the HurwitzLab repo into your fork.

## Pulling from the course repo (upstream)

As I will be updating the repo from which you are pulling, `git pull` will often tell that changes from the remote repository need to be "merged" into your repo.
If you have local changes that will conflict with the remote changes, Git will recommend you `commit` or `stash` your local changes.

To commit them, use `git commit -m "commit message here"`.
This will save your changes into your local index.
Files can then be merged with the remote changes.
You will be placed into an editor with a default message about how you are merging the remote changes.
If this editor is `vim`, then you can type `EscZZ` to save the default message and quit the editor.

NOTE: The editor that is chosen is determined by your `$EDITOR` environmental variable. If this is unset (and it usually is), then the OS will likely default to `vim` (or worse, the original `vi`). If you would like to set this to something else like `pico` or `emacs`, you can set `EDITOR` by adding this line to your `~/.bashrc` or `~/.bash_profile`:

```
export EDITOR=pico
```

If you don't need to save (commit) your local changes, you can use `git stash` to have Git tuck them away and overwrite the local files with the remote versions.
You can later use `git stash apply` to apply the stashed changes to the remote changes you pulled in.

## Adding new files (homework)

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

## Pushing your changes

The actions of `add` and `commit` affect only your _local_ repository.
You still need to "push" your commits to GitHub:

```
$ git push
```

**If you cannot see your commits in the web interface at GitHub.com, then you haven't turned in your work yet.**

To grade your assigments, I will use `git pull` to pull down the changes from GitHub.com to my machine.
I will run the test suite.
Your grade will be the percentage of passing tests, so if you passed 80% of the tests, then your grade is 80% of the points for the assignment.

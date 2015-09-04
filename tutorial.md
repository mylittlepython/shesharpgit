Let's assume OS agnostic and Git is installed
http://git-scm.com/book/en/v2/Getting-Started-Installing-Git

-> git config --global user.name "A name"
-> git config --global user.email aname@example.com
this information backs any commits immutably (need again configuration
to change)

you need to do this only once if you pass the --global option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the --global option when you’re in that project.

example: you want to have a different email address for a particular project (a personal project on your work computer, perhaps?), just run this command inside that project's folder:

git config user.email "you@example.com"
It's the same command as before, this time just omitting the --global.

http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

default text editor for Git is set to Vim
else: git config --global core.editor yourEditor

-> config --list
user.name=A name
user.email=aname@example.com

->to add more keys (example colors when working from terminal with Git),
edit the .gitconfig file (path is subject to OS)

check what Git holds for a specific key value:
-> git config <key>
ex. git config user.name

http://git-scm.com/book/en/v2/Getting-Started-Getting-Help

==================================
http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository

case 1: existing project

lets assume: https://github.com/mylittlepython/shesharpgit.git

-> git clone https://github.com/mylittlepython/shesharpgit.git
we can work with the cloned project from our device
let's assume we don't like the cloned project name
git clone https://github.com/mylittlepython/shesharpgit.git favoriteName

->git status -s (s stands for short)

->transfer protocols (https, git, ssh)

case 2: new project

-> mkdir yourProject
-> git init
creates .git directory that represents a Git repository skeleton

let's assume we create our src files and readme, etc.
"add this content to the next commit" cmd
-> git add <file>
example: assume we have numerous python files: git add *.py
-> git commit -m 'this is our commit'

-> git push origin branch_name 
assuming is the master branch, becomes: git push origin master


====================================
http://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository

but Git is inherently distributed :) this means friends from all around
the globe work together simultaneously
->git pull origin master to get latest project updates

exercise:
-> echo 'some message' > README.md
now the readme file has changed
let's observe what happens when we echo this file in parallel

case: I modified file and committed. Before pushing I need
to modify again the commit:

i. git reset HEAD <file>

or

ii. we will have to commit...push...and stage again the modified
file (naah...)

what we have changed, but not staged, simply type:
git diff

there are files that we don't want to stage at all (ex. log files,
auto-generated src files). Edit a .gitignore file and let Git know what to stage and what not, example:
cat /path/to/.gitignore
*.[pyc] #any files that end in ".pyc"

continue here with branching/..

in the slides include screenshots (ex. where to clone, ssh)
update: instead of slides help interactively

auto-completion and other tips: https://git-scm.com/book/en/v1/Git-Basics-Tips-and-Tricks

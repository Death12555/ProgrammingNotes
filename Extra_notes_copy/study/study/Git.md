Git:

It is a version control system.(A system that helps us keep track of our files)

## Features:

1. Easily recoverable files.

2. Who introduced an issue and where.

3. Roll back to previously working state.

---


History of VCS:

i) Local VCS -> DataBase- to keep track of files(everything in the computer itself)

Pros:

-> can keep track of files and rollback.

Cons:

-> If you lose your files hard disk, everything is lost.

  

ii) Centralized VCS-> Server is used to keep files-files can be pulled to work on them by multiple people simultaneously.

Pros:

-> Files can be pulled to work on them and then pushed back to the server when work is done.

-> Copy of the file in centralised server is considered as the final copy.

-> Damage to the file prevented since multiple people can own the file

Cons:

-> If centralised server gets damaged the final version of the file maybe lost.

-> All data is on the server and may get lost if the server is damaged.

  

iii) Distributed VCS-> Similar to Centralized except every user gets the entire history of files on the server as a repository to use along with the project as backup. It is a smart system that doesn’t take to much space.

Pros:

-> Since everyone has backup only source code files are pulled.

-> Only the changes made are saved instead of saving the entire file/project again(The system is smart that way).

  

Git is Distributed Version Control System.

  

Git, GitHub, GitLab, BitBucket,

  

Features:

-> Captures snapshots and not differences(stores different versions of the file, to use or used for recovery stored locally in folder named ‘.git’).

-> Almost every operations are local.

-> Git has integrity(uses checksum(string (SHA-1 checksum) is used for checking integrity)).

-> Git generally only adds data.

  
Commands:

-> git config user.name “nam_of_user”:
(used to change the name and see user’s name).

-> git config user.email “email_of_user”:
(same as name).

-> git config —global core.editor “emacs”:
(used to choose editor).

-> git status :
(checks status/whether a git repository exists in the current directory or not).

(If it gives ‘On branch master’ know that it means the branch is the master/main branch)

(’No commits yet’ imply no snapshots/versions are put in the directory/repository).

(Untracked files(files in the repository that are not committed).

(Tracks modifications made in the file too, in any are made then they need to be added separately, since each change is a new version for the repository to commit individually).

Nothing to commit, working tree clean means all files/versions are committed and working tree is clean

-> git init:
(to create/initialize a new git repository).

-> git add --a:
(add all files in the repository to the staging area).
(We can also use git add . to do the same).

-> git add file_name_with_extension:
(adds the specified file to the staging area).

-> git commit -m “message_with_the_commit”:
((to commit files with message) if only git commit is typed then a text editor is opened).
(commit is used to tell about the changes/fixes made nothing else).

-> git log:
(used to see what we have committed. Shows the message we have given along with the files).

(Gives strings/hashes according to the number of commits, Each string is used for logging).

(Gives the log of changes made by other users who have downloaded the repository too).

-> rm -rf .git:
(used to stop tracking files in a folder, and removes/deletes all files in a folder).

(Deletes .git folder).

-> git clone url_of_git_repository:
(used to clone a git repository from GitHub).

(If we need to name the folder as something else then all we need to do is add name after the url e.g.: git clone url_of_git_repository repository_name).

-> touch .gitignore:
(used to create a file to ignore files that are untracked. All we have to do is input the name of the file in .gitignore(use any text editor to do so)).

(If we want to add all files of a certain type to be ignored, all we have to do is use *.file_type to ignore files of those type, e.g.: if we want to ignore all log files in the directory then just use *.log)

(This can also be used to ignore directories inside the repository by just adding them in .gitignore, e.g.: for putting directory dir all we have to do is input dir/ in the .gitignore file (note: This will make it so that any folder named dir will get ignored, to make only the one specific dir to be ignored all we have to is input /dir/ instead of dir/. If we want to make the specific dir inside lets say folder static then we have to input static/dir in .getignore instead of dir/)).

(Blank folders are ignored by default and if there is a folder inside that is already considered to be ignored then git status will ignore everything inside the blank folder(the folder inside the blank folder may have some content but since it is input in .gitignore that file's contents are ignored too)).

-> git diff:
(compares working directory with staging area).
(The lines were in the staging and the lines in green are in the working directory)
(If the result from the function/command is blank this means that the staging area and the working directory are the same)

-> git diff --staged:
(compares the previous commit with the staging area)

-> git commit -a -m "message_to_commit":
(is used to stage tracked files and commit them directly).
(The untracked files won't be able to be committed though).

-> git rm file_name_with_extension:
(is used to remove/delete files. Use directory_name/file_name_with_extension to remove file from a specific folder).

-> git mv file_name_with_extension new_file_name_with_extension:
(is used to rename files. Use folder name/ file name to go into specific folder).

(mv is actually used to move files, but it can also be used to rename files, more like moving a file into a new named file).

-> git rm --cached file_name:
(is used to untrack files tracked files).
(use folder_name/file_name to untrack from a specified folder).

(It is done because just putting the files in the .gitignore won't make gti stop tracking the already tracked files. To do that they need to be untracked first).

-> git log -p:
(shows all the commits along with their diffs(changes in the directory) in the repository)

(if we add -number along with the the command/function then it will show the last 'n' number of commits according to the number specified. e.g.: if we want to see the last 3 commits along with their diffs, then it will be git log -p -3).

-> git log --stat:
(gives a short summary about the changes made with each commit like the number insertions, deletions, updations etc. of files/data in files etc.).

-> git log --pretty=form_in_which_we_want_the_commit/details:
(gives a short summary of commits according to the format specified e.g.: oneline or short or full(this gives the commit along with the author)(git --pretty=oneline or git --pretty=short or git --pretty=full)).

(Note: Author is the one who made the file while Committer is the one changed/made fixes to the file).

-> git log --since=number_of_days/weeks/months/years.days/weeks/months/years:
(Gives the changes made in the last 'n' number of days/weeks/months/years, e.g.: git log --since=2.days, gives the changes made in the last 2 days).

-> git log --pretty=format:"%h -- %ae" : (%H: commit hash, %h: abbreviated commit hash, %an: author name, %ae: author email etc.):
(shows commits according to format specified).

-> git commit --amend:
(is used change commits made previously by someone)

-> git restore --staged file_name:
(used to unstage staged files).

(add file path in repository if necessary).

-> git checkout -- file_name:
(used to unmodify/revert any changes to the back the previous one).

(add file path if necessary).

-> git checkout -f:
(used to revert changes made to multiple files).

(brings back to a clean working state).

-> git remote add origin git@github.com:url_name
(this means git remote add a url whose name is origin(name can be changed but default should be origin git@github.com:git_repository))

-> git remote -v:
(shows 2 urls one to push files/code etc. to and the other to pull data/files/code from)

-> git push -u origin master:
(used push files/data/code into an existing repository using the origin link).

(-u is only used once to set upstream(here upstream is origin))

(All other changes will be pushed through git push origin master/git push origin branch_name (for pushing changes to branch node)).

(if we want to us a different name for the remote branch from the local branch node in our system, then we need to include it after the command with a ':' e.g.: git push origin branch_name:different_branch_name)

-> git config --global alias.shortcut_name command:
(used to make alias/short_forms for commands, e.g.: git config --global alias.st status, will make an alias for status named st, git config --global alias.unstage 'restore --staged --', will make an alias for unstaging. git config --global alias.last 'log -p -1' will make alias for the command to show the last commit entry.)

-> git checkout -b branch_name:
(used to create a new branch for the repository(-b means to create a new branch) e.g.: git checkout -b develop, will create a new branch named develop the branch will have all the files of the master branch to develop itself/work on it parallel to the master branch).

(Note: Any changes made to files specified in .gitignore will get ignored including changing of file locations/deletion/updation/copying etc. to a different folder in the repository).

(Any changes made to other files in the branch node will remain contained to the branch node).

-> git checkout master:
(used to switch to master node).

-> git checkout branch_name:
(used to switch to branch node).

-> git pull origin master:
(used to pull files/data/code etc. from GitHub/BitBucket etc.)

-> git branch -d branch_name:
(used to delete branches when they are no longer useful).

(Gives warning if branch isn't merged).

-> git branch -D branch_name:
(used to delete branches when they are no longer useful).

(Gives no error/warning during deletion).

(-D means to delete)

-> git branch:
(used to see all branches in the repository).

-> git merge brach_name:
(used to merge branch with the current working).

-> git branch -v:
(gives the same output as git branch along with the last commit hash and commit message).

-> git branch --merged:
(shows all branches that we have already merged(already merged branches) along with the branch we are in).

-> git branch --no -merged:
(shows all the not already merged branches).

-> git push -d branch_name:
(used to delete remote branches on GitHub/GitLab/BitBucket etc.)

Commit:

Capturing versions/snapshots of source codes to save them as different versions to use and for backup.

  

Git’s Three Stage Directory:

Local Operations:

1. Working Directory:

The directory(the one we access through windows explorer/finder etc.) that we open to see its contents(files, executables, source code etc.)

  

2. Staging Area:

This contains those files that we want to push in the upcoming commit.

  

3. Git Directory:

‘.git’ named hidden folder/directory that contains compressed files/versions of our files of our programs that gives the users the files that they need.

  

‘.git’ gives files of the working directory.

  

File Status Lifecycle:

1. Untracked: When a new directory is converted into working directory/repository then the files at the time are still not added to the staging area.

  

git add is also used to make the untracked into unmodified files before they are sent to the staging area.

  

Unmodified means Now tracking.

  

2. Unmodified: After adding files to the staging area, they become unmodified. From here they are sent to the staging area.

  

3. Modified: After changing/editing them they become modified. Due to making changes their newer versions will need to be added to the staging area.

  

4. Staged: Using git add after these 2 will get the files staged.

  

After getting staged they are committed they become unmodified again.

  

We can even remove/untrack the file from there. If we want.

In Git,

- pull means to get code from GitHub to our system along with all of its commits, changes, code etc. and....
- push means to put our code, files etc. to the remote repository in GitHub etc.
- remote means a website/repository on the internet. It could be hosted on GitHub, GitLab, etc.


<<<(for original)/= = =((the spaces don't exist but in obsidian multiple ='s is a command)for incoming changes)/>>>(for new lines/code/files etc.): These are called conflict resolution markers.
VS code uses this to ask which one do we want to keep after merging.

git add file_name is also used to mark merge conflicts as resolved when necessary.

git only saves the changes made in the new commit and puts a pointer that points to the older commit to point to.

star/asterisk along with highlighting the current working branch with colour green, points to the branch we are in currently.


Branching Workflow:

- Long Running Branches:
	The branches that are always being worked on are called long running branches.
	They exist till the completion of the project/for the entire lifecycle of the project.
	e.g.: -> master
	     -> develop
	     ->Proposed_Update(or PU)

- Topic Branches:
	The branches that are short lived. i.e.: they exist till the topic/idea isn't completed so that it can be integrated.
	e.g.: -> Replace text with typed JS
		   TypedJSInt(branch name)
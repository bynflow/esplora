# Filegm

    TITLE
Tool with a simple graphical interface to find lost files, and duplicate files, within the filesystem.

    DESCRIPTION
"Filegm" is the name of a tool with a simple graphical interface that aims to trace files according to 2
guidelines which are the type of format and a precise or approximate date when the file was created in memory.
The interface has 2 fields, which are the input field (left) in which the user will enter the precise date
or two date range in which the files being searched are assumed to have been stored in the machine in use,
and the output field (right) within which the eventual results of the search with their addresses in memory
will be shown according to the alphabetical order of the files. Each of the results is also a direct link to
open each file. At the bottom of the left field are two buttons: the first on the left is used to start the
file search, the second on the right starts the search for only duplicate files that may exist based on the
extensions and dates entered. One or more extensions can be entered in the extension entry field.
I used Python because it is an open source, straightforward and powerful language; for the GUI I enjoyed using
Tkinter, which I also chose because it is supported by several well-done and comprehensive tutorials. I did not
encounter any particular difficulties in the implementation except for a few moments of impasse in the logical
part to implement the alphabetical order based on the filename, while in the graphical part I had to do some
more research to figure out for example how to get the highlighting of result links on mouseover as well as the
highlighting of the same after they have been used (this mechanism by the way would need to be perfected).
"Filegm", this little tool, has so much potential, interesting functions can be added: for example when
searching for images created in a given time frame, if the result consists of several items they could be
displayed and scrolled as slides in a virtual directory, same for audio files which could be listened to
sequentially in a playlist. But my priority challenge is to implement parallel computing in the application,
without which the program suffers from major limitations due to the fact that each task is stacked on a single
process. I am trying to figure out how I can apply multithreading in the application code as it is now.

    INSTALL AND RUN
Filegm is a Python3 application and runs on Linux OS, to start it you need to install python3-tk. The command
to run, for example, on Debian-based systems is: sudo apt-get install python3-tk


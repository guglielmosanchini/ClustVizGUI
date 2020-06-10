# App version

This branch contains a restructured version of the master branch, 
used to build an app through [fbs](https://build-system.fman.io/),
which helps building PyQt5 apps automating some PyInstalle tasks.
Basically, all the code has been moved inside ```src/main/python```, 
a ```base.py``` script has been added, which makes the ```ApplicationContenxt```
visible to all other scripts, every path reference has been modified 
using ```appctxt.get_resource()```, and all the pics and other files have been
moved to ```src/main/resources/base```.
The ```target ``` folder contains the result of the execution of 
```fbs freeze``` and ```fbs installer```.

## Useful links

https://github.com/mherrmann/fbs-tutorial

https://github.com/pyinstaller/pyinstaller/issues/3753

https://stackoverflow.com/questions/26176169/pyinstaller-os-x-app-runs-from-command-line-but-not-finder-window
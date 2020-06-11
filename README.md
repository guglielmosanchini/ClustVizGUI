# ClustVizGUI

<img src="https://raw.githubusercontent.com/guglielmosanchini/ClustViz/master/data/clustviz_logo.png" width="200" height="200">

## 2D Clustering Algorithms Visualization

#### Check out [ClustViz](https://github.com/guglielmosanchini/ClustViz), too!

<img src="https://raw.githubusercontent.com/guglielmosanchini/ClustVizGUI/master/data/README_pics/pic1_gui.JPG" width="450" height="350">

<img src="https://raw.githubusercontent.com/guglielmosanchini/ClustVizGUI/master/data/README_pics/pic2_gui.JPG" width="450" height="350">

<img src="https://raw.githubusercontent.com/guglielmosanchini/ClustVizGUI/master/data/README_pics/pic3_gui.JPG" width="450" height="350">


This repository contains a GUI version of the [clustviz](https://github.com/guglielmosanchini/ClustViz) package, built with PyQt5.
The app was built using [fbs](https://build-system.fman.io/),
which helps building PyQt5 apps automating some PyInstaller tasks.
Basically, all the code has been moved inside ```src/main/python```, 
a ```base.py``` script has been added, which makes the ```ApplicationContenxt```
visible to all other scripts, every path reference has been modified 
using ```appctxt.get_resource()```, and all the other non-code files have been
moved to ```src/main/resources/base```.
The ```target ``` folder contains the result of the execution of 
```fbs freeze``` and ```fbs installer```.

It is still not available as app; if you would like to use it now, just clone the repo, install the requirements
and run the script ```src/main/python/guy.py```. Currently, it works only on MacOS.

## Useful links

https://github.com/mherrmann/fbs-tutorial

https://github.com/pyinstaller/pyinstaller/issues/3753

https://stackoverflow.com/questions/26176169/pyinstaller-os-x-app-runs-from-command-line-but-not-finder-window
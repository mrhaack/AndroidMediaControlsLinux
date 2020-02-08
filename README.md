# Android Headset Media Controls for Linux
Python script that hacks in support for Android headset media control for Linux.

For more details on how this works, see the associated [blog post](http://www.roligheten.no/blog/programming/2018/07/02/media-controls-windows.html) (Windows)

# Work is not guaranteed. Tested on Lenovo IdeaPad 330-15ARR laptop with Kubuntu 19.10 and Manjaro Linux

## Installation
Required for Linux:
1. Python 3 or 2.7 (untested) installed on the system.
2. The packages pynput, numpy and sounddevice, installable via `pip install pynput numpy sounddevice` or `pip3 install pynput numpy sounddevice`.

### Linux
1. Download a copy of this repository from [here](https://github.com/mrhaack/AndroidMediaControlsLinux/archive/master.zip)
2. Extract to an appropriate location on your system, where doesn't matter as long as you don't accidentally delete it.
3. Navigate to the extracted directory.
4. Open the terminal in the directory.
5. Run with `python run.py` or `python3 run.py`.
6. Optionally, add the script to the startup of your OS

### Windows
You can download the script from the original repository [here](https://github.com/Catuna/AndroidMediaControlsWindows)

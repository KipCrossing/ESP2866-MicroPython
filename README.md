# ESP8266 with Micropython

## QuickStart

```
git clone https://github.com/KipCrossing/ESP2866-MicroPython

pip3 install adafruit-ampy --upgrade

ampy --port /dev/ttyUSB0 put main.py

./upyrun-esp8266.sh
```

_Note: only edit files in the /BoardFiles directory_

## REPL over USB

To connect to the REPL over USB, use:

```
picocom /dev/ttyUSB0 -b115200
```

## Copy and remove python files to the ESP8266

Import Ampy

```
pip3 install adafruit-ampy --upgrade
```

Copy the files using the put command

```
ampy --port /dev/ttyUSB0 put test.py
```

Or copy an entire directory

```
ampy --port /dev/ttyUSB0 put BoardFiles
```

Check if the file has been put onto the ESP8266 via REPL

```python
>>> import os
>>> os.listdir()
['boot.py', 'test.py']
```

Or using Ampy

```
comp:~/ESP2866-MicroPython$ ampy --port /dev/ttyUSB0 ls
/boot.py
/test.py
```

Run the script

```python
>>> import test
Test script working!
```

remove files

```
ampy --port /dev/ttyUSB0 rm test.py
```

remove directories

```
ampy --port /dev/ttyUSB0 rmdir BoardFiles
```

For more on [Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy#upgrade-ampy) see [here](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/file-operations)

## Quick deploy method

The idea here is to set up the file structure for rapid prototyping. Fri-st create a directory called BoardFiles and put `__init__.py` and `main.py` files inside. This will be where you do all of your coding.

Second, in the parent directory, add a `main.py` file with the following code:

```python
from BoardFiles import main
```

Put this file on the board

```
ampy --port /dev/ttyUSB0 put main.py
```

Now, whenever you want to run new code on the board, simply edit the `/DoardFiles/main.py` file and put it on the board:

```
ampy --port /dev/ttyUSB0 rmdir BoardFiles
ampy --port /dev/ttyUSB0 put BoardFiles/
ampy --port /dev/ttyUSB0 run main.py
```

This has been put into the upyrun-esp8266.sh scrip for easy run:

```
comp:~/ESP2866-MicroPython$ ./upyrun-esp8266.sh
```

Takes about 4 seconds to run

Otherwise, enter into REPL mode:

```
picocom /dev/ttyUSB0 -b115200
```

and reset board with CTRL+D

To exit picocom use CTRL+A+X

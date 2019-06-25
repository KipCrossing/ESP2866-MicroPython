# ESP8266 with Micropython

## REPL over USB

To connect to the REPL over USB, use:

```
picocom /dev/ttyUSB0 -b115200
```

## Ampy

### Copy python files to the ESP8266

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
ampy --port /dev/ttyUSB0 put test_dir
```

Check if the file has been put onto the ESP8266

```python
>>> import os
>>> os.listdir()
['boot.py', 'test.py']
```

Run the script

```python
>>> import test
Test script working!
```

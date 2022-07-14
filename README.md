# Ping IP address parallely using Python Multithreading

## Python Version

`python3 -V`

current python version: **3.10.4**

## How to create a virtual environment

syntax is `python3 -m venv` <enviornment name>

In this case, the example is given below.

* Step 1: Execute the command using `python3 -m venv env`

* Step 2: Activate using the command `source ./env/bin/activate`

* Step 3: Verify using the command `where python`

## Install dependencies in Virtual environment

### Ensure proper version of PIP
In the virtual environment use the following command,

`pip list`

After executing, you may get the following details.

>(env) E:\pydev-1-2020\projectDependencyInstall>pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
>

### Upgrade PIP version
Execute the following command to upgrade to higher version of pip.

`python3 -m pip install --upgrade pip`


### Final step to install dependencies

After activating the virtual environment, execute the following command

`pip install -e .`

or

`pip install .`

### How to run

In VSCode, Eclipse or Pycharm, run the file `Main3.py`


### Performance Benchmark

**For the two subnets of 506 IP Addresses, parallel execution using Python Multi Processing and Multireading **

Multi-Thread Pool Size = 300, Total Time Taken:  30.680755729999873  seconds
Multi-Process Pool Size = 200, Total Time Taken:   47.99978301899998  seconds
Sequential 1 at a time, Total Time Taken:  7156.473847672  seconds
### Additional Features
MultiprocessingPing.py - allows to multiprocessing instead of multithreading, but it is slower
SequentialPing.py - allows for sequential scan which is unbearably slow.

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

>pip list

Package            Version
------------------ -------
- ansible            5.8.0
- ansible-core       2.12.6
- atomicwrites       1.4.0
- attrs              21.4.0
- cffi               1.15.0
- click              8.1.3
- cryptography       37.0.2
- Flask              1.1.1
- importlib-metadata 4.11.4
- itsdangerous       2.0.1
- Jinja2             3.1.2
- MarkupSafe         2.1.1
- more-itertools     8.13.0
- packaging          21.3
- ping3              4.0.3
- pip                22.1.2
- pluggy             0.13.1
- py                 1.11.0
- pycparser          2.21
- pyparsing          3.0.9
- pytest             5.0.1
- PyYAML             6.0
- resolvelib         0.5.4
- setuptools         60.10.0
- wcwidth            0.2.5
- Werkzeug           2.1.2
- wheel              0.37.1
- zipp               3.8.0

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

** For the two subnets of 506 IP Addresses, parallel execution using Python Multi Processing and Multireading and sequentially one IP Adress at a time **
- We exclude 192.168.1.0 and 192.168.2.0, because they are the Network IDs
- We exclude 192.168.1.255 and 192.168.2.255, because they are network broadcasts

1. Multi-Thread Pool Size = 300, Total Time Taken:  30.680755729999873  seconds
2. Multi-Process Pool Size = 200, Total Time Taken:   47.99978301899998  seconds
3. Sequential 1 at a time, Total Time Taken:  7156.473847672  seconds
### Additional Features

1. MultiprocessingPing.py - allows for multiprocessing instead of multithreading, but it is slower
2. SequentialPing.py - allows for sequential scan which is unbearably slow.

# Internet Monitor

## Description

This script is designed to test the availability of internet connection using the `speedtest-cli` library by Ookla (which -I think- is an industry standard). It can be used to monitor the availability of service and identify any potential issues.

### Personal note
This script was created out of my frustration, not been able to prove to my ISP that my internet was not working from time to time. As every time I called the ISP, they would say that my internet was working fine, measuring during the call, so, I had to find a way to catch the connection problems and prove that I was not an elephant...

## Installation
This script is tested on Linux and Windows, with Python 3.11. There is no particular reason for it not to be able to run on other Python >3.6 versions, but -to be honest- I have not tested it.

It is highly recommended to use a virtual environment to run this script. I use `conda` for this purpose and it is highly recommended to use it.

Once you have Python installed and [optionally] your virtual environment activated, you can install the required packages by running the following command:
```
pip install -r requirements.txt
```


## Usage
```shell
 Usage: python runner.py [OPTIONS]

╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --iterations                           INTEGER  [default: 10]               │
│ --delay                                INTEGER  [default: 2]                │
│ --create-excel    --no-create-excel             [default: no-create-excel]  │
│ --help                                          Show this message and exit. │
╰─────────────────────────────────────────────────────────────────────────────╯
```

## Example
```python
python runner.py --create-excel --iterations 10
```

Author: [@spitoglou](https://github.com/spitoglou)
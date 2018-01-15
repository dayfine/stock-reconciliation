# Stock Reconciliation

This is a simple python program that takes text report of initial positions, transactions, and ending positions, and reconcile the changes.

## Installation
To install, simply clone this repo.

```bash
git clone https://github.com/dayfine/stock-reconciliation.git
```


## To Use
- Note: the program was written and tested in Python3. A minimum test has been performed with Python2 as well. To use with Python2, simply remove the 3 from all the commands below.

```bash
$ python3 -m recon filename
```

In your CLI, use `python3 -m recon filename` command in the root directory. The filename can be either a relative or absolute path.

The program will read the given file, reconcile it, and output the result to both the terminal and an output file. The output file will be saved to the same directory where the input file is, and it will be named as the input file name followed by 'output'.

For example:

```bash
$ python3 -m recon tests/test1.txt
Reading and reconciling tests/test1.txt
===================
Please review the reconciled differences:
-------------------
GOOG 10.0
Cash 8000.0
TD -100.0
MSFT 10.0
-------------------
```



## API
### **Class Report**
**Usage**
```python
from recon import Report

report = Report()
report.read_file(mytextfile)
difference1 = report.reconcile()

another_report = Report(beg_pos, transactions, end_pos)
difference2 = another_report.reconcile()
```

**Properties**

All three properties below can either be initiated by passing arguments into the construcotr, or later built from the `read_file` or `read_text` methods.

- **beg_pos: Dict**

  Represents portoflio position at the beginning of the day.

- **transactions: List**

  Represents all transactions(each an array of four elements) of the day.

- **end_pos: Dict**

  Represents begining portoflio at the end of the day.

**Methods**
- **read_file: (filename: String) => void**

  Reads text file that contains data for beginning position, transactions, and ending position of the day, and parse all the data into the corresponding properties.

- **reconcile: () => differences: Dict**

  Calculates expected ending position of the day using given information, and compares it against the reporting end position. Note that the result is a dict.

- **read_text: (text: String/List) => void**

  Works the same as `read_file`, except that the input is expected to be either a long string literall with all the data, or a list of lines splitted from such a string literal.



## Tests
To test, make sure you have [pytest](https://docs.pytest.org/en/latest/getting-started.html) installed. Then, simply run the command below:

```bash
$ python3 -m pytest
```


# Python CLI (Command Line Interface)

---

## Table of contents

- [Commands and usage](#commands-and-usage)
- [Configuration](#configuration)
  - [Settings](#settings)
  - [Output](#output)
- [Output file](#output-file)
- [Examples](#examples)
  - [General command format](#general-command-format)
  - [For typical use](#for-typical-use)
  - [For specific Columns](#for-specific-columns)
  - [For specific operations](#for-specific-operations)
  - [For output destination path](#for-output-destination-path)
- [Modules used](#modules-used)
- [References](#references)

---

## Commands and usage

- Usage

      main.py/main.exe [-h] [-c COLUMNS [COLUMNS ...]] [--sum] [--mean] [--median] [--mode] [--max] [--min] [--count] [-d DESTINATION] path

- Positional arguments

  `path`                  the path of the file to compute

- Options

  `-h, --help`            show this help message and exit

  `-c COLUMNS [COLUMNS ...], --columns COLUMNS [COLUMNS ...]` Command with list of optional columns to display separated by space

  `--sum`                argument to compute the Sum of the given column.

  `--mean`                argument to compute the Mean of the given column.

  `--median`              argument to compute the Median of the given column.

  `--mode`                argument to compute the Mode of the given column.

  `--max`                 argument to compute the Max of the given column.

  `--min`                 argument to compute the Min of the given column.
  
  `--count`                 argument to compute the Count of the given column.

  `-d DESTINATION, --destination DESTINATION`                 argument to store the report to specified destination path.

---

## Configuration

The configurations w.r.t the exe file can be done with the help of the config.ini file present parallelly with the working exe file.

The Sections present in the file are- Settings and Output

### Settings

It consists of the Parameters:

- header - (default = true)

True if the file has a column header as apply false.

- save_report - (default = true)

True if you want to save the report file to the specified directory else false.

### Output

It consists of the Parameters:

- destination- (default = null)

Contains the output report storage file path, else a blank space can be specified to store in the current working directory.

Here are the initial configurations that are present in config.ini :-

```ini
[settings]
#if the given source file has header row
header = true
report_save = true


[output]
#leave empty to store in current working directory
destination = 
```

 > Note: Absence of config.ini leads to the usage of default configuration settings.

---

## Output file

The result gets stored in a .txt file containing the desired results. The two output files are getting stored: -  

- Report.txt

The report.txt contains the full log along with the computed output as displayed in the CLI.  

- Data.txt

The data.txt contains the result specific report of computed output along with the column numbers and calculated parameters and values.

Both files consist of a report along with the date of its generation.

The output report file is not generated if it explicitly mentioned in configuration file as false in report_save parameter.

If the destination path being mentioned in command line arguments then the output report  will be generated irrespective to the config file.

> The priority of the execution is given to command line arguments over default config.ini file.

---

## Examples

### General command format

```cmd
main.py/main.exe [-h] [-c COLUMNS [COLUMNS ...]] [--sum] [--mean] [--median] [--mode] [--max] [--min] [--count] [-d DESTINATION] path
``` 

### For typical use

    main.py/main.exe {csv file path} 

The above command results in the reading of the mentioned file and displaying the resulted output. Along with storing the file.  

### For specific Columns

    main.py/main.exe {csv file path} [-c COLUMNS [COLUMNS ...]] 

The above command computes or performs operation on the mentioned list of columns only, the columns are verified and selected after proper presence of computational values to compute, and output is displayed. To select all the columns the the optional flag is not mentioned in the command line  .

### For specific operations

    main.py/main.exe {csv file path} [--mean] 

The above command computes the mentioned optional flag –mean and displays the result of mean only. You can mention any number of optional flags or leave a blank to display all computed operations.
The other options that are available are: -
`--sum`, `--mean`, `--median`, `--mode`, `--max`, `--min`, `--count`

### For output destination path

    main.py/main.exe {csv file path} [-d DESTINATION] 

The above command specifies the destination file path with an specifier –d followed by the path. The flag generates the output report in the specified fie path even if save_report is mentioned as false in config file. Specified path folder if not present will lead to creation before storing the output file. Invalid file path returns results with a warning.  

---

## Modules used

- Execution_1: handles the opening and phrasing of file

```
Inital execution function to pharse the given file

Args:
    args (object)          : argparse object
    target_dir (path)      : path of source file to compute
    destination_dir (path) : path of the destination file
    REPORT (string)        : String of report to be printed
```

- Execution_2: handles the required computations on the phrased data

```
Checking the available columns in the pharsed data and perform required operations on them

Args:
    df (dataframe)         : pharsed data from execution_1
    args (object)          : argpharse object
    destination_dir (path) : path of the destination file
```

- File save: Saves the file report output if specified or uses default settings.

```
Function to save the file

Args:
    destinations_dir (path) : _description_
    REPORT (string)         : string containing the required report
    DATA (string)           : string containing the required result specific report
```

---

## References

- [Final app(exe file)](https://bitbucket.org/venkatagunasekhar/python_cli/src/master/Final_Deliverables/)

- [Documentation](https://bitbucket.org/venkatagunasekhar/python_cli/src/master/docs/)

- [Source Code](https://bitbucket.org/venkatagunasekhar/python_cli/src/master/Src/)

- [User manual](https://bitbucket.org/venkatagunasekhar/python_cli/src/master/README.md)

---

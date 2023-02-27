import argparse
from pathlib import Path
import pandas as pd
import os
from configparser import ConfigParser
import datetime

try:
    # creation of the Config parser object
    configur = ConfigParser()

    # Content of data to store in output report
    REPORT = """"""
    # Result specific report data without logging info/process steps
    DATA = """"""
    #!!!!---function_names, functionaccess, temp, functions - should be maintained in accordance to each other for the sake of smooth running without any errors---!!!!
    # list of function names and their access boolean permission
    function_names = ["--sum", "--mean", "--median", "--mode", "--max", "--min", "--count"]
    function_access = [True for _ in range(len(function_names))]

    try:
        # print(configur.read("config.ini"))
        configur.read("config.ini")
        # header flag variable for column head
        HEAD = configur.getboolean("settings", "header")
        #   REPORT_SAVE flag to say whether to store the file
        REPORT_SAVE = configur.getboolean("settings", "report_save")
        # destination path to store the output
        destination_dir = configur.get("output", "destination")
        if destination_dir == "":
            destination_dir = os.getcwd()
    except Exception as e:
        print("Exception during config file opening:-", e)
        print("Using default settings")
        HEAD = True
        REPORT_SAVE = True
        destination_dir = os.getcwd()
    else:
        # print(configur.getboolean('settings', 'header'))
        print(
            configur.get("output", "destination"),
            len(configur.get("output", "destination")),
        )


    def execution_1(args, target_dir, destination_dir, REPORT):
        """Inital execution function to pharse the given file

        Args:
            args (object): argparse object
            target_dir (path): path of source file to compute
            destination_dir (path): path of the destination file
            REPORT (string): String of report to be printed
        """
        # list of supported file formats and their functions to pharse the given file on
        s_files = [pd.read_excel, pd.read_csv]
        s_names = ["excel", "csv"]
        # loop to iterate on the given formats
        for i in s_files:
            REPORT += "trying to open as.. " + s_names[s_files.index(i)] + "\n"
            print("trying to open as.. ", s_names[s_files.index(i)])
            try:
                # try opening the file
                if HEAD:
                    df = i(target_dir)
                else:
                    df = i(target_dir, header=None)
                # print(df.head(8))
                REPORT += f"Detected the {s_names[s_files.index(i)]} file," + "\n\n"
                print(f"Detected the {s_names[s_files.index(i)]} file,", end="\n\n")
            except Exception as e:
                # in case of exception display the exception and continue loop
                REPORT += "Exception: " + str(e) + "\n"
                print("Exception: ", e)
                if s_files.index(i) == len(s_names) - 1:
                    REPORT += "Cannot pharse the file \n exiting.."
                    print("Cannot pharse the file\n exciting..")
                continue
            else:
                # in case of successfull pharsing, break the loop
                execution_2(df, args, destination_dir)
                break


    def execution_2(df, args, destination_dir):
        """Checking the available columns in the pharsed data and perform required operations on them

        Args:
            df (dataframe): pharsed data from execution_1
            args (object): argpharse object
            destination_dir (path): path of the destination file
        """
        # access the global report
        global REPORT
        # get the list of columns in the given file
        columns = [i for i in df.columns]
        if len(columns) == 0:
            # check on columns
            REPORT += "No columns found in the given file\n exiting.." + "\n\n"
            print("No columns found in the given file\n exiting..")
            return
        print(columns)
        REPORT += "list of columns = " + ",".join(list(map(str, columns))) + "\n\n"
        print("list of columns =", *columns, end="\n\n")
        if args.columns:
            # check if the custom columns given
            REPORT += (
                "selected column numbers == "
                + " ".join(list(map(str, args.columns)))
                + "\n\n"
            )
            print("select column number == ", args.columns)
            req_columns = []
            # loop to check and append those columns
            for i in args.columns:
                if i - 1 < len(columns):
                    req_columns += [i - 1]
                else:
                    print(f"Column number {str(i)} is out of range.")
            req_columns = [i - 1 for i in args.columns if i - 1 < len(columns)]
        else:
            req_columns = list(range(len(columns)))
        # accessing the global DATA
        global DATA
        # storing the result specific data
        DATA += (
            "Finalized selected column numbers == "
            + " ".join(list(map(str, [i for i in req_columns])))
            + "\n\n"
        )
        # printing the finalized list of columns
        REPORT += (
            "Finalized selected column numbers == "
            + " ".join(list(map(str, [i for i in req_columns])))
            + "\n\n"
        )
        print("Finalized selected column number == ", [i + 1 for i in req_columns])
        # loop to perform the required operation on the given data
        for j in req_columns:
            i = columns[j]
            # writing report into string DATA and REPORT
            DATA += f"Column-{columns.index(i) + 1} Name:- " + str(i) + "\n"
            REPORT += f"Column-{columns.index(i) + 1} Name:- " + str(i) + "\n"
            print(f"Column-{columns.index(i) + 1} Name:- ", i, end="\n\n")
            # converting the dataframe to numeric and skipping the NaN cells
            df1 = pd.to_numeric(df[i], errors="coerce").dropna()
            # check for count of numeric values
            if df1.count() == 0:
                DATA += "Column skipped due no presence of numeric date" + "\n\n"
                REPORT += "Column skipped due no presence of numeric date" + "\n\n"
                print("Column skipped due no presence of numeric date", end="\n\n")
                continue

            # list of functions to operate on df1-!! should be maintained in accordance with 'function_names'
            functions = [
                df1.sum,
                df1.mean,
                df1.median,
                df1.mode,
                df1.max,
                df1.min,
                df1.count,
            ]
            # access global list function_names
            global function_names
            # loop to enumerate on the list of available functions
            for i, j in enumerate(functions):
                # i-index value , j - function
                if function_access[i]:
                    # check for mode since its outpu is a list
                    if function_names[i] == "--mode":
                        DATA += (
                            function_names[i][2:].capitalize()
                            + ": "
                            + ", ".join(list(map(str, j().to_list())))
                            + "\n"
                        )
                        REPORT += (
                            function_names[i][2:].capitalize()
                            + ": "
                            + ", ".join(list(map(str, j().to_list())))
                            + "\n"
                        )
                        print(
                            function_names[i][2:].capitalize() + ": ",
                            *j().to_list(),
                        )
                        continue
                    DATA += function_names[i][2:].capitalize() + ": " + str(j()) + "\n"
                    REPORT += function_names[i][2:].capitalize() + ": " + str(j()) + "\n"
                    print(function_names[i][2:].capitalize() + ": ", j())
            DATA += "\n"
            REPORT += "\n"
            print()
        # calling function to store the output result
        file_save(destination_dir, REPORT, DATA)


    def file_save(destination_dir, REPORT, DATA):
        """Function to save the file

        Args:
            destinations_dir (path): _description_
            REPORT (string): string containing the required report
            DATA (string): string containing the required result specific report
        """
        # check whether to save the report
        if REPORT_SAVE:
            # check if the file already exists
            if os.path.isfile(str(destination_dir) + "\\report.txt"):
                REPORT += "Another output file already exists and overwriting it..\n"
                print("Another output file already exists and overwriting it..")
                # ask whether to overwrite
                if input("Do you want to overwrite?(y/n)") == "n":
                    REPORT += "Report written after overwriting the previous file."
                    print("Output report not saved\nexiting..")
                    return

            # get the current datetime
            x = datetime.datetime.now()
            x = "\nReport Generated on " + str(x.strftime("%d-%b-%Y, %a at %I:%M %p"))
            # append to the report and data
            REPORT += x
            DATA += x

            # save the report
            with open(str(destination_dir) + "\\report.txt", "w") as text_file:
                text_file.write(REPORT)
                print("Output report saved..")
            # save the result data
            with open(str(destination_dir) + "\\data.txt", "w") as text_file:
                text_file.write(DATA)
                print("Output result data saved..")

            print("\nexiting..")


    if __name__ == "__main__":
        # creation of the parser object
        parser = argparse.ArgumentParser()
        # Positional arguments--
        # argument for source file path
        parser.add_argument("path", type=str, help="CSV file path of the file to compute")
        # Optional arguments--
        # argument for columns
        parser.add_argument(
            "-c",
            "--columns",
            dest="columns",
            type=int,
            nargs="+",
            help="Command with list of optional columns to display separated by space",
        )
        # argument for functional computations
        for i in function_names:
            parser.add_argument(
                i,
                action="store_false",
                help=f"argument to compute the {i[2:].capitalize()} of the given column.",
            )
        # argument for the destination file
        parser.add_argument(
            "-d",
            "--destination",
            dest="destination",
            type=str,
            nargs=1,
            help="argument to store the report to specified destination path.",
        )
        # pharsing the arguments
        args = parser.parse_args()

        # list of functions to access the given argument operations-!! should be maintained in accordance with 'function_names'
        temp = [args.sum, args.mean, args.median, args.mode, args.max, args.min, args.count]
        # check for arguments call
        if False in temp:
            function_access = [(not (i)) for i in temp]
        #print("fn access --", function_access)
        # get the target dir
        target_dir = Path(args.path)
        # print(args)
        # check for the destination flag
        if args.destination:
            print("Using the given destination path")
            REPORT_SAVE = True
            destination_dir = os.path.abspath(Path(args.destination[0]))
            # make directory if not present
            os.makedirs(destination_dir, exist_ok=True)
        else:
            print("The default destination path used")
            # destination_dir = os.getcwd()
        try:
            # check the target and destination file path
            if not (os.path.isfile(target_dir)) or not (os.path.exists(destination_dir)):
                raise Exception("Sorry, invalid file path")
        except Exception as e:
            # return the exception
            REPORT += str(e) + "\n"
            print(e)
        else:
            # Execute if path is okay
            REPORT += "Source File path = " + str(target_dir) + "\n"
            print("Source File path = ", target_dir)
            REPORT += "Destination file path = " + str(destination_dir) + "\n\n"
            print("Destination file path = ", destination_dir, end="\n\n")
            REPORT += "Detecting the file type.. \n"
            print("Detecting the file type.. ")
            # call the function execution_1 for furthe steps
            execution_1(args, target_dir, destination_dir, REPORT)

except Exception as e:
    print(e)
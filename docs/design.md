# Design Documentation 


The design flow of the app is like the first the configuration file is fetched if present and then the settings are applied accordingly. If the default configuration file is not present, then the default settings are set. The **configparser** library are used for this purpose. 

Then the command arguments are set in for phrasing the command line arguments and they are fetched. The settings which are set are changed according with the **command line arguments**. After that, the path given is checked and verified, eventually the target path is checked. 

Then the arguments and paths are then sent to **execution_1**. In execution_1 the given target source data file then **phrased using the pandas** list of file functions and after successful phrasing the data frames is sent for computation into the function of **execution_2**.  

In **execution_2** the data frames of columns are separated and then the selected list of **columns is filtered** and then sent for execution. If the columns contain no numeric data or of no data, they are skipped from computation. The computations are carried out in according to the command line arguments. The list of functions is used for this purpose. The list variables – **function_names, function_access, temp, functions** - should be maintained in accordance with each other for the sake of smooth running without any errors. They contain Boolean and function names, and their function call which work in accordance with each other to do the required operations. This is done to enable future scalabilty of the application.

After computation and on execution of the **execution_2** function the **file_save** function is called. From the start, all the data and processes made are logged into command line and stored in the string called **REPORT**, and the result (in specific) data without computational log in **DATA** string global variable. This is then printed into an **.txt** file in accordance with the configuration file parameter save_report and the command line arguments.  

Hence this is the working flow execution of the given application.

---

# Design Flow

## main module

![main](/docs/images/Python%20CLI_page-0001.jpg)

## execution_1 module

![execution_1](/docs/images/Python%20CLI_page-0002.jpg)

## execution_2 module

![execution_2](/docs/images/Python%20CLI_page-0003.jpg)

## file_save module

![file_save](/docs/images/Python%20CLI_page-0004.jpg)
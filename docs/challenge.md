# Challenge Document  

## Challenges faced and their solutions that are implemented

- The initial challenge was faced at fetching the document and phrasing it, since the document can be in any format either in **excel** or **csv** and for both the formats have distinct functions to get executed, so a list of function for different file formats are used. *(Note: If needed the json and list can be added)*

- Reading the **config file** and proceeding accordingly was also a challenging task and for overcoming it the **configparser** library has been used.  

- The source and the destination paths have been taken as input, verified, and modified accordingly to save and fetch files properly without errors, the **os** library has been used for this purpose.  

- The challenge of filtering the columns with no data or without numeric data was also difficult, hence, to overcome it, after phrasing the columns, and the non-numeric columns are filtered irrespective of the user specified input and informed at the time of execution to the user. This is done by fetching the **count** of the numeric computable rows.  

- To make the app **more scalable**, the functions available for computations are structured in a list and the list can be modified accordingly afterwards for additional functionalities for calculations.  

- For the generation of the output file, the **report string** has been created for full and result specific outputs and generated in the form of .txt file.  

---
# Convert DBF to JSON and CSV

**COMMAND LINE FRONT** (CSV2JSON.py)
Single-file program that converts DBF files to JSON files and converts CSV files to JSON as well.
To my knowledge, one of the first programs that does this.


**APPLICATION FRONT** (DBF-CSV_JSON-APP.py) (Much easier than CSV2JSON.py)
  -Run "DBF-CSV_JSON-APP.py".
  
  -Enter the name of the first column (cell 0,0) in the text box next to the "First Column Name" Button
  
  -After the name is entered, click the "First Column Name" Button
  
  -Click the "Select a File" Button
  
  -Select the DBF file in the application window. 
  
  -That's it. A JSON and CSV file will be added to the directory. 

NOTE:
  In order to have this program work you must go into the "DBF.py" file (that is imported) and change the line 
  "ignore_missing_memofile=False" to "ignore_missing_memofile=True".
  
  **THIS IS NOT REQUIRED WITH THE APPLICATION FRONT SOLUTION

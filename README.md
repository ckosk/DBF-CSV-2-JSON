# DBF-CSV-2-JSON Converter

A Python-based tool for converting DBF (dBase) files to JSON and CSV formats. This project provides both a command-line interface and a user-friendly GUI application for data conversion tasks.

## Features

- **DBF to JSON**: Convert dBase files to JSON format (via CSV intermediate)
- **DBF to CSV**: Convert dBase files to CSV format
- **CSV to JSON**: Convert CSV files to JSON format (with configurable primary key)
- **Dual Interface**: Command-line tool and GUI application
- **Automatic File Naming**: Output files are automatically named based on input files
- **Primary Key Configuration**: Specify which column to use as the primary key for JSON output
- **Error Handling**: Basic error handling with user-friendly messages

## Prerequisites

- Python 3.6 or higher
- Required Python packages:
  ```bash
  pip install dbfread
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ckosk/DBF-CSV-2-JSON.git
   cd DBF-CSV-2-JSON
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Option 1: GUI Application (Recommended for Beginners)

The GUI application provides a user-friendly interface for converting DBF files:

1. Run the GUI application:
   ```bash
   python "DBF-CSV_JSON-APP.py"
   ```

2. Follow the on-screen instructions:
   - Enter the name of the first column (cell 0,0) in the text box
   - Click the "First Column Name" button
   - Click "Select a File" and choose your DBF file
   - The application will automatically generate both CSV and JSON files
   - **Note**: The first column name you specify will be used as the primary key for the JSON output

### Option 2: Command Line Interface

For advanced users or automation purposes, use the command-line tool:

1. Edit `CSV2JSON.py` and modify the file paths:
   ```python
   csvFilePath = r'your_file.csv'  # For CSV to JSON conversion
   jsonFilePath = r'output.json'   # Output JSON file name
   dbfFilePath = r'your_file.dbf'  # For DBF to JSON conversion
   ```

2. **Important**: Modify the primary key column name in the `make_json` function:
   ```python
   key = rows['PRTYPE_IDL']  # Change 'PRTYPE_IDL' to your desired column name
   ```

3. Run the script:
   ```bash
   python CSV2JSON.py
   ```

## Important Notes

### DBF File Handling
- **GUI Application**: Automatically handles missing memo files
- **Command Line**: You may need to modify the `dbfread` import settings in some cases
- **Note**: The command-line version has a hardcoded comment about modifying "BDF.py" but this appears to be outdated

### Limitations
- **DBF to JSON**: The tool converts DBF to CSV first, then CSV to JSON (two-step process)
- **Primary Key Requirement**: JSON output requires specifying a primary key column
- **Hardcoded Values**: The command-line version has hardcoded file paths and column names that must be manually edited

### File Output
- Output files are saved in the same directory as the input file
- CSV files use the same name as the input file with `.csv` extension
- JSON files use the same name as the input file with `.json` extension

## Project Structure

```
DBF-CSV-2-JSON/
├── CSV2JSON.py              # Command-line conversion tool
├── DBF-CSV_JSON-APP.py      # GUI application
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

## Dependencies

- **dbfread**: For reading and parsing DBF files
- **tkinter**: For the GUI application (included with Python)
- **csv**: For CSV file handling (included with Python)
- **json**: For JSON file handling (included with Python)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions:
1. Check the error messages in the application
2. Verify your input file format
3. Ensure all dependencies are properly installed
4. Open an issue on the GitHub repository
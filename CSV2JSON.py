import csv
import json
from dbfread import DBF 

#NOTE In this (BDF.py) .py file you have to change "ignore_missing_memofile=False" to "ignore_missing_memofile=True"
#NOTE (Line 85, in my case)

# Function to convert a CSV to JSON
def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        #Convert each row into a dict and add it to data
        for rows in csvReader:
            key = rows['PRTYPE_IDL'] #THIS IS THE PRIMARY KEY, PICK YOUR FIRST COLUMN
            data[key] = rows
    #Open json writer and dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def dbf_to_csv(dbf_table_pth):#Input a dbf, outputs a csv, same name and same path
    csv_fn = dbf_table_pth[:-4]+ ".csv" #Set csv file name
    table = DBF(dbf_table_pth)
    with open(csv_fn, 'w', newline = '') as f:#Create a csv file and fill with dbf content
        writer = csv.writer(f)
        writer.writerow(table.field_names)#Write column name
        for record in table:#Write rows
            writer.writerow(list(record.values()))
    return csv_fn #returns a csv file name, CAN be used in the make_json function
         
csvFilePath = r'example.csv' #IF CONVERTING FROM CSV this is the name of the csv file you want to convert, otherwise, not needed
jsonFilePath = r'finished.json' #NOTE This is where you pick the name of the JSON file that will be output
dbfFilePath = r'project.dbf' #NOTE This is the name of the DBF file you want to convert to JSON

make_json(dbf_to_csv(dbfFilePath), jsonFilePath) #INSTEAD OF "csvFilePath" PUT "dbf_to_csv(dbfFilePath)" IF TRYING TO CONVERT DBF

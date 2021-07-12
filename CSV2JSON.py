import csv
import json
from dbfread import DBF

# Function to convert a CSV to JSON
def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        #Convert each row into a dict and add it to data
        for rows in csvReader:
            key = rows['ID'] #THIS IS THE PRIMARY KEY, PICK YOUR FIRST COLUMN
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
         
csvFilePath = r'Products.csv'
jsonFilePath = r'HereYouGo.json'
dbfFilePath = r'Products.dbf'

make_json(csvFilePath, jsonFilePath) #INSTEAD OF "csvFilePath" PUT "dbf_to_csv(dbfFilePath)" IF TRYING TO CONVERT DBF

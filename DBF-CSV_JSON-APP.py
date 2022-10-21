from tkinter import *
from tkinter import filedialog
import csv
import json
from dbfread import DBF 
import os
import sys

def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        #Convert each row into a dict and add it to data
        for rows in csvReader:
            key = rows[str(sys.argv[1])] #THIS IS THE PRIMARY KEY, PICK YOUR FIRST COLUMN
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

jsonFilePath = r'finished.json' #NOTE This is where you pick the name of the JSON file that will be output

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open DBF file", 
        filetypes=(("DBF Files", "*.dbf"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)
    dbfFilePath = os.path.abspath(tf.name)
    make_json(dbf_to_csv(dbfFilePath), jsonFilePath) #INSTEAD OF "csvFilePath" PUT "dbf_to_csv(dbfFilePath)" IF TRYING TO CONVERT DBF
    txtarea.insert(END, "Complete, files added to directory.")
    tf.close()

ws = Tk()
ws.title("DBF -> JSON & CSV")
ws.geometry("400x300")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=5)
txtarea.pack(pady=40, side=TOP)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Select File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import csv
import json
from dbfread import DBF 
import os
import sys
import time

ws = Tk()
ws.title("DBF -> JSON & CSV")
ws.geometry("700x350")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=5)
txtarea.insert("1.0", "--Status Will Appear Here--\n")
txtarea.pack(pady=40, padx=10, side=TOP)

txtarea1 = Text(ws, width=70, height=5)
txtarea1.insert("1.0", "1. Enter cell 0,0 (First Column Name) in bottom-right text box\n2. Click First Column Name button\n3. Click Select File\n4. Select your DBF file\n4. Done. Status will appear in the top box")
txtarea1.pack(pady=10, padx=10, side=TOP)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        #Convert each row into a dict and add it to data
        for rows in csvReader:
            try:
                key = rows[get_input()] #THIS IS THE PRIMARY KEY, PICK YOUR FIRST COLUMN
                data[key] = rows
            except KeyError:
                print("**INCORRECT FIRST COLUMN NAME**")
                showinfo("Error", "Incorrect First Column Name\nCSV Generated\nInsert Correct Column Name to Generate JSON.")                
                time.sleep(1)
                exit()
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

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open DBF file", 
        filetypes=(("DBF Files", "*.dbf"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)
    dbfFilePath = os.path.abspath(tf.name)
    jsonFilePath = dbfFilePath[:-4]+ ".json"
    make_json(dbf_to_csv(dbfFilePath), jsonFilePath) #INSTEAD OF "csvFilePath" PUT "dbf_to_csv(dbfFilePath)" IF TRYING TO CONVERT DBF
    txtarea.insert(END, "Success\nCSV and JSON files added to directory.")
    tf.close()

Button(
    ws, 
    text="Select File", 
    command=openFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

def get_input():
   value = my_text_box.get("1.0","end-1c")
   return(value)

my_text_box=Text(ws, width=20, height=1)
my_text_box.pack(side=RIGHT, expand=True, fill=X, padx=20)

cell = Button(ws, text="First Column Name", command=lambda: get_input())
cell.pack(side = RIGHT)

ws.mainloop()

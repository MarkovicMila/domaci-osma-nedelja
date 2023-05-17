from klasa import *
from tkinter import *


root=Tk()
def search_and_export(naziv):
    t=Toplevel()
    
    excel=Button(t,text='Excel',command=lambda:a.export_excel_naziv(naziv))
    excel.grid(row=0,column=0)

    csv=Button(t,text='CSV',command=lambda:a.export_csv_naziv(naziv))
    csv.grid(row=0,column=1)

def export():
    t=Toplevel()
    naziv=''
    excel=Button(t,text='Excel',command=lambda:a.export_excel_all())
    excel.grid(row=0,column=0)

    csv=Button(t,text='CSV',command=lambda:a.export_csv_all())
    csv.grid(row=0,column=1)
    pass

naziv=Entry(root)
naziv.grid(row=0,column=1,columnspan=2)

b_se=Button(root,text='Search and export',command=lambda:search_and_export(naziv.get()))
b_se.grid(row=0,column=0)

e1_t=Entry(root)
e1_t.grid(row=0,column=1,columnspan=2)

b_e=Button(root,text='Export all',command=lambda:export())
b_e.grid(row=1,column=0)

root.mainloop()
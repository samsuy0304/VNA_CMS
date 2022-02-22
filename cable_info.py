import shelve

cable = shelve.open("cable.txt")

cable["102"] = ["80", "1", "34"]
cable["115"] = ["80", "3", "36G"]
cable["117"] = ["140", "3", "36G"]
cable["123"] = ["160", "4", "36G"]
cable["126"] = ["35", "2", "34G"]

from tkinter import *
from tkinter import ttk


class Cable_Info:

    def __init__(self, root):

        root.title("Add New Cable")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.number = StringVar()
        self.gauge = StringVar()
        self.type = StringVar()
        self.length = StringVar()

        number_entry = ttk.Entry(mainframe, width=7, textvariable=self.number)
        length_entry = ttk.Entry(mainframe, width=7, textvariable=self.length)
        type_entry = ttk.Entry(mainframe, width=7, textvariable=self.type)
        gauge_entry = ttk.Entry(mainframe, width=7, textvariable=self.gauge)

        number_entry.grid(column=2, row=1, sticky=(W, E))
        length_entry.grid(column=2, row=2, sticky=(W, E))
        type_entry.grid(column=2, row=3, sticky=(W, E))
        gauge_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Button(mainframe, text="Add", command=self.add).grid(column=1, row=5, columnspan=2, sticky=W+E)

        ttk.Label(mainframe, text="Cable Number: ").grid(column=1, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="Cable Length: ").grid(column=1, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="Cable Type: ").grid(column=1, row=3, sticky=(W, E))
        ttk.Label(mainframe, text="Gauge: ").grid(column=1, row=4, sticky=(W, E))

        number_entry.focus()
        length_entry.focus()
        type_entry.focus()
        gauge_entry.focus()

        root.bind("<Return>", self.add)

    def add(self, *args):
        cable.update({self.number.get(): [self.length.get(), self.type.get(), self.gauge.get()]})


root = Tk()
Cable_Info(root)
root.mainloop()


cable.close()


import tkinter as Tk
from tkinter import filedialog

from model.test import Test
from utils.utils import get_data_from_json


class LauncherUi(object):
    def __init__(self, window):
        self.root = window
        self.root.title('Test launcher')
        self.file_list = []
        self.btn_open = Tk.Button(text='Open',
                                  width=10,
                                  height=1,
                                  bg='gray',
                                  fg='black',
                                  command=lambda: self.openfile())

        self.btn_generate = Tk.Button(text='Generate',
                                      width=10,
                                      height=1,
                                      bg='gray',
                                      fg='black',
                                      command=lambda: self.generate())

        self.btn_advanced = Tk.Button(text='Advanced settings',
                                      width=10,
                                      height=1,
                                      bg='gray',
                                      fg='black',
                                      command=lambda: self.generate())

        self.lbl_description = Tk.Label(text='',
                                        width=80,
                                        height=4
                                        )
        self.text_box = Tk.Text(width=80, height=8, relief=Tk.RIDGE, borderwidth=2)
        self.btn_open.pack()

    def openfile(self):
        self.file_list = []
        filenames = filedialog.askopenfiles(mode='r', filetypes=[('JSON Files', '*.json')])
        for filename in filenames:
            if filename is not None:
                name = filename.name
                self.file_list.append(name)
                # print(name)
        if self.file_list:
            self.btn_generate.pack()

    def generate(self):
        for file in self.file_list:
            json_obj = get_data_from_json(file)
            test = Test(json_obj)
            print(test.get_str())
            self.lbl_description["text"] = ''.join(test.get_descr_str())
            self.text_box.delete('1.0', Tk.END)
            self.text_box.insert(Tk.END, test.get_cli_str())
        self.lbl_description.pack()
        self.text_box.pack()

    # def hide(self, event):
    #     event.widget.pack_forget()

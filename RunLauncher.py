import argparse
# import os
# import sys
#
# from configobj import ConfigObj
from dnf.pycomp import raw_input

from model.test import Test
from utils.utils import get_data_from_json

import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
button = tk.Button(text='Open',
                   width=10,
                   height=1,
                   bg='gray',
                   fg='black',
                   command=lambda: openfile())

lbl_description = tk.Label(text='',
                           # foreground="white",
                           # background="black",
                           width=80,
                           height=4
                           )


text_box = tk.Text(width=80, height=8, relief=tk.FLAT, borderwidth=0)


def openfile():
    filenames = filedialog.askopenfiles(mode='r', filetypes=[('JSON Files', '*.json')])
    for filename in filenames:
        if filename is not None:
            name = filename.name
            file_list.append(name)
            # print(name)

    for file in file_list:
        json_obj = get_data_from_json(file)
        test = Test(json_obj)
        print(test.get_str())
        lbl_description["text"] = ''.join(test.get_descr_str())
        text_box.insert(tk.END, test.get_cli_str())


def run_ui():
    button.pack()
    lbl_description.pack()
    text_box.pack()
    window.mainloop()


def create_parser():
    """"""""
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-f', '--file',
                            help='JSON file to read as source for test',
                            dest='filename',
                            nargs='+')
    cli_parser.add_argument('-u',
                            help='',
                            dest='ui')
    return cli_parser


def add_file(namespace):
    list_file = []
    for file_name in namespace:
        list_file.append(file_name)
    return list_file


def input_file():
    add_more = True
    list_file = []
    while add_more:
        try:
            file_name = raw_input("Please enter the file name: ")
            list_file.append(file_name)
        except Exception as e:
            print(e)
            pass
        more = str(raw_input("Do you want to add one more file? {y/n)")).lower()
        if more != "y":
            add_more = False
    return list_file


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    file_list = []

    # print(args.filename)

    # conf_file = "launcher.conf"  # os.path.join(str(Path.home()), "totp/.token.config")
    # if not os.path.isfile(conf_file):
    #     print("%s is missing" % conf_file)
    #     sys.exit(1)
    # config = ConfigObj(conf_file)

    if args.filename:
        file_list = add_file(args.filename)
    elif args.ui:
        run_ui()
    else:
        file_list = input_file()

    # for file in file_list:
    #     json_obj = get_data_from_json(file)
    #     test = Test(json_obj)
    #     print(test.get_str())

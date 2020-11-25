import argparse
# import os
# import sys
#
# from configobj import ConfigObj
from dnf.pycomp import raw_input

from model.test import Test
from ui.launcher_ui import LauncherUi
import tkinter as tk
from utils.utils import get_data_from_json


def run_ui():
    window = tk.Tk()
    window.geometry('800x300')
    app = LauncherUi(window)
    window.mainloop()


def create_parser():
    """"""""
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-f', '--file',
                            help='JSON file to read as source for test, this is required only in text mode',
                            dest='filename',
                            nargs='+')
    cli_parser.add_argument('-u',
                            help='"-u text" should be used for text mode, graphic mode is used by default',
                            dest='uimode')
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

    # conf_file = "launcher.conf"  # os.path.join(str(Path.home()), "totp/.token.config")
    # if not os.path.isfile(conf_file):
    #     print("%s is missing" % conf_file)
    #     sys.exit(1)
    # config = ConfigObj(conf_file)

    if args.filename and args.uimode == 'text':
        file_list = add_file(args.filename)
        for file in file_list:
            json_obj = get_data_from_json(file)
            test = Test(json_obj)
            print(test.get_str())
    elif args.uimode == 'text':
        file_list = input_file()
    else:
        run_ui()


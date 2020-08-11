import json
import os
import re


def openfile(filename):
    f = open(filename, 'r')
    return f


def open_json(filename):
    with open(filename) as json_file:
        try:
            return json.load(json_file)
        except Exception as e:
            print(e)
            return None


def get_data_from_json(json_path):
    """
    Get JSON data in json object
    :param json_path:
    :return: Success: JSON object
             Failure: Exit
    """
    try:
        with open(json_path) as fileHandle:
            try:
                return json.load(fileHandle)
            except ValueError as error:
                error_message = 'invalid json:\n' + str(error)
                return exit_method(1, error_message)
    except Exception as error:
        error_message = 'Error accessing json file:\n' + str(error)
        return exit_method(1, error_message)


def convert_to_json(json_obj):
    try:
        return json.loads(json_obj)
    except Exception as e:
        exit_method(-1, 'Json not loaded!' + str(e))
        return None


def exit_method(code, msg=''):
    print(msg)
    exit(code)


def exec_cli(cli):
    stream = os.popen(cli)
    return stream.read()


def clear_string(string, mask):
    string = re.sub(mask, '', string)
    return string

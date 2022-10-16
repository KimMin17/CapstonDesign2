from pathlib import Path
import os
import json

def find_json(path):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                find_json_file(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.json': 
                    modify_json(full_filename)
    except PermissionError:
        pass

def modify_json(path):
    for json_file in json_file_list:
    with open(json_file, 'r') as f:
        json_obj = json.load(f)
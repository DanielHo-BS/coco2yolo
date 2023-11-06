import os
from labelme2yolo import Labelme2YOLO

folder = '../datasets/label/20231106/form_text'
files = os.listdir(folder)
json_files = [f for f in files if f.endswith('.json')]  # get all json files

convertor = Labelme2YOLO(folder, False)
for json_file in json_files:
    convertor.convert_one(json_file)

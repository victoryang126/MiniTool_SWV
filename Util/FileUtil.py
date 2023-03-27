import os
import sys
import json
from dataclasses import dataclass
from dataclasses import asdict,field
from typing import List,Any


@dataclass
class File:
    dir:str=None
    file:str = None
    name_extension:str = None
    name:str = None
    extension:str = None


class FileUtil:

    def __init__(self):
        pass

    def init_file_bypath(self,file):
        """

        Args:
            file:

        Returns:

        """
        f = open(file, 'w', encoding='UTF-8')
        f.close()

    def init_file(self,directory,file_name):
        """

        Args:
            file:

        Returns:

        """
        file = os.path.join(directory,file_name)
        f = open(file, 'w', encoding='UTF-8')
        f.close()

    def get_extension(self,file):
        return os.path.basename(file).split(".")[1]

    def is_file(self,file):
        return os.path.isfile(file)

    def is_dir(self,directory):
        return os.path.isdir(directory)

    def is_dir_eixst(self,directory):
        return os.path.exists(directory)

    def create_dir(self,directory):
        if os.path.exists(directory):
            pass
        else:
            os.makedirs(directory)

    def get_file_name(self,file):
        return os.path.basename(file)

    def get_dir(self,file):
        return os.path.dirname(file)

    def get_file_info(self,file):
        directory,file_name = os.path.split(file)
        return directory,file_name


    def create_folder(self,directory,folder_name):
        folder = os.path.join(directory,folder_name)
        if not os.path.exists(folder):
            os.mkdir(folder)
        else:
            if os.path.isfile(folder):  # 如果是文件，不是文件夹，则抛出异常
                raise Exception(folder + " is not a folder but a flle")

    def create_folder_bypath(self,folder):
        if not os.path.exists(folder):
            os.mkdir(folder)
        else:
            if os.path.isfile(folder):  # 如果是文件，不是文件夹，则抛出异常
                raise Exception(folder + " is not a folder but a flle")


    def dumps_object_to_js_parameter_bypath(self,test_object,js_parameter,file,mode = "w"):
        with open(file, mode, encoding='UTF-8') as f:
            f.write(js_parameter)
            json.dump(test_object, f, indent=4)
            f.write(";\n")

    def dumps_object_to_js_parameter(self,test_object,js_parameter,directory,file_name,mode = 'w'):
        file = os.path.join(directory,file_name)
        with open(file, mode = mode, encoding='UTF-8') as f:
            f.write(js_parameter)
            json.dump(test_object, f, indent=4)
            f.write(";\n")

    def generate_script_bypath(self,scripts,file):
        with open(file, "w", encoding='UTF-8') as f:
            f.write(scripts)

    def generate_script(self,scripts=None,directory=None,file_name=None):
        file = os.path.join(directory,file_name)
        print(file)
        with open(file, "w", encoding='UTF-8') as f:
            f.write(scripts)

fileUtil = FileUtil()
if __name__ == "__main__":
    pass
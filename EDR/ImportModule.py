from Util.LogCFG import *
from Util.RegUtil import *
from Util.FileUtil import *
import pandas as pd
import sys
import os
from dataclasses import dataclass
from dataclasses import asdict,field
from typing import List,Any,Dict
import re
from string import Template
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# def

def padded_number(num,length):
    """
    function used to pading 0 to the number
    Args:
        num:numbner
        length:the string length
    Returns:
        eg padded_number(1,3) will return "001"
    """
    num_str = str(num)
    if len(num_str) < length:
        return num_str.zfill(length)
    else:
        return num_str.zfill(3+ len(num_str))

def validate_columns(actual_columns,expect_columns,sheet):
    """
    function used to check if expect columns exist in the sheet, if not, raise exception
    Args:
        actual_columns: the actual columns
        expect_columns: the columns expect in the the sheet
        sheet: sheet name
    Returns: NONE
    """
    not_exist = []
    for expect_col in expect_columns:
        if expect_col not in actual_columns:
            not_exist.append(expect_col)
    if len(not_exist) !=0:
        raise Exception(",".join(not_exist) + f" <- this colums not exist in sheet {sheet}")

def strip_upper_columns(columns):
    """
    function used to strip the column and upper the string
    Args:
        columns:
    Returns: eg ["1a\n"] will return ["1A"]
    """
    columns = [str(col).strip().upper() for col in columns]
    return columns


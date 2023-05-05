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


def DealQualiyOrQualifyTime(df) -> pd.DataFrame:
    """
    处理Excel中的qualify和disqualify 时间
    当前的规则是在单元格里面填写 1000, 2000 或者1000,
    然后将单元格弄从两个元素的列表
    Parameters:
        df - DataFrame 包含qualify和disqualify 的数据
    Returns:
        df - 处理了qualifytime和disqualifytime 以后的DataFrane
    Raises:
        NONE
    """
    for col in df:
        Debug_Logger.debug(col)
        if col.find("Qualify") >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df
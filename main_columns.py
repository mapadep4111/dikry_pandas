import pandas as pd
import numpy as np
from termcolor import colored
import time
import os
pd_read =  pd.Series([[1, 2],[ 3, 4 ], 5, np.nan])
print(pd_read)
dates = time.strftime('%Y-%m-%d')
print(dates)
pd_dates = pd.date_range(time.strftime('%Y%m%d'), periods=6)#"20130101"
print(pd_dates)
pd.options.display.max_rows = 4
pd.options.display.max_columns = 4
x = 0
while True:
    os.system('CLS')
    x = x + 1
    pd_dates = pd.date_range(time.strftime('%Y%m%d'), periods=x)
    df = pd.DataFrame(np.random.randn(x, 4), index=pd_dates, columns=list("ABCD"))
    time.sleep(0)
    print(colored(pd_dates,color='green'))
    print(colored(df,color='red'))

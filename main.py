import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'robot'] = int(1)
data.loc[data['whoAmI'] != 'robot', 'robot'] = int(0)
data.loc[data['whoAmI'] == 'human', 'human'] = int(1)
data.loc[data['whoAmI'] != 'human', 'human'] = int(0)
data.head(11)
""" не знаю почему выводит с десятком"""
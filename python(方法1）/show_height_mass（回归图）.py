# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#读取数据 name height mass gender homeworld
df = pd.read_csv('../csv/stat_character.csv')
fig, ax = plt.subplots(1,1)


sns.jointplot(x="height", y="mass", data=df, color="b", kind='reg')

plt.show()

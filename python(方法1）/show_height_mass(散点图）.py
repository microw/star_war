# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#读取数据
df = pd.read_csv('../csv/stat_character.csv')
fig, ax = plt.subplots(1,1)

#name height mass gender homeworld
#散点图
sns.jointplot(x="height", y="mass", data=df, color="b", s=50, kind='scatter',
              space = 0.1, size = 8, ratio = 5)
plt.show()

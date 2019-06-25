# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#读取数据
df = pd.read_csv('../csv/stat_character.csv')
fig, ax = plt.subplots(1,1)


#散点图+KDE 图
g = (sns.jointplot(x="height", y="mass", data=df, color="k")
      .plot_joint(sns.kdeplot, zorder=0, n_levels=6))
plt.show()

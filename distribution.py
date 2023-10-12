import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

root = 'D:/yolov5/datasets/VisDrone2019/VisDrone2019-DET-train/labels'
files = os.listdir(root)
x = []
for file in files:
    file_path = os.path.join(root, file)
    # print(file_path)
    with open(file_path, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            numbers = line.strip().split(' ')
            w = float(numbers[3])
            h = float(numbers[4])
            area = w * h
            x.append(area)

# sns.set()
# # 使用pandas来设置x 轴标签 和y 轴标签
# x = pd.Series(x, name="x variable")
# ax = sns.distplot(x)
# hist_fig = ax.get_figure()
# hist_fig.savefig("distribution.png")

# 将数据转换为DataFrame
df = pd.DataFrame(x, columns=['area'])
# 使用seaborn绘制直方图
plt.figure(dpi=100, figsize=(47, 40))

sns.set(font_scale=10)
palette = sns.color_palette("deep", n_colors=1)
# sns.histplot(data=df, x='area', kde=True, color='#1c4587', line_kws={"lw": 10})
sns.distplot(a=df, hist=True, bins=15,
             kde_kws={'linewidth': '10', 'color': '#1c4587'
                      })
plt.xlabel("Proportion of area")
plt.ylabel("Distribution density")
plt.savefig('histogram.png')
print(df.describe())

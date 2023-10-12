import os

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

filepath = "D:/yolov5/datasets/VisDrone2019/VisDrone2019-DET-train/labels"
filenames = os.listdir(filepath)
ratio = []

for filename in filenames:
    with open(filepath + "/" + filename, "r") as fileHandler:
        line = fileHandler.readline()
        # check line is not empty
        while line:
            txt = line.strip()
            w = txt.split(" ")[3]
            h = txt.split(" ")[4]
            try:
                r = float(w) / float(h)
                ratio.append(r)
                print(r)
            except Exception as e:
                print(e)
            # print(txt)
            # print(w)
            # print(h)
            # print("###############################")

            line = fileHandler.readline()

df = pd.DataFrame(ratio, columns=['Data'])
# 使用seaborn绘制直方图
sns.histplot(data=df, x='Data', kde=True)
plt.savefig('histogram.png')
print(df.describe())

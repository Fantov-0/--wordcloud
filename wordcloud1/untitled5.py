# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:23:57 2020

@author: Razer 14
"""

# -*- coding: utf-8 -*-
from os import path
from imageio import imread 
import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
 
# TXT文件读取
text = open('sdxl.txt',encoding='gbk').read()
 
# jieba分词 全模式 
wordlist = jieba.cut(text)     #cut_all = True
 
# 空格分割
wl_space_split = " ".join(wordlist)

 
# 读取mask蒙板图片
d = path.dirname(__file__)
nana_coloring = imread(path.join(d, "duo3.png"))
 
# 对分词后的文本生成词云，设置参数
my_wordcloud = WordCloud( background_color = 'white',      # 设置背景颜色
                            mask = nana_coloring,          # 设置背景图片
                            max_words = 1000,              # 设置最大现实的字数
                            stopwords = STOPWORDS,         # 设置停用词
                            max_font_size = 50,            # 设置字体最大值
                            random_state = 30,             # 设置有多少种随机生成状态，即有多少种配色方案
                            )
 
# 生成词云
my_wordcloud.generate(wl_space_split)
 
# 从图片获取颜色信息  
image_colors = ImageColorGenerator(nana_coloring)
 
# 重新着色  
my_wordcloud.recolor(color_func=image_colors)
 
plt.imshow(my_wordcloud)    # 显示词云图
plt.axis("off")             # 是否显示x轴、y轴下标
plt.show()
 
# save img  
my_wordcloud.to_file(path.join(d, "cloudimg.png"))
 
 
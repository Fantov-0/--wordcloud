# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:22:49 2020

@author: Razer 14
"""

from os import path
from imageio import imread 
import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
 
# TXT文件读取 神雕侠侣
text = open('sdxl.txt',encoding='gbk').read()


#加入武功词汇表
#导入武功txt文件
people_names_file = open("金庸小说全人物.txt",encoding='gbk')
people_names = list()
for line in people_names_file.readlines():
    line = line.strip()   # 去掉每行末尾的换行符
    jieba.add_word(line)  #加入词库
    people_names.append(line)

print(len(people_names))


#加入武功词汇表
#导入武功txt文件
kungfu_names_file = open("金庸小说全武功.txt",encoding='gbk')
kungfu_names = list()
for line in kungfu_names_file.readlines():
    line = line.strip()   # 去掉每行末尾的换行符
    jieba.add_word(line)  #加入词库
    kungfu_names.append(line)
print(len(kungfu_names))


#导入中文一般停用词集
stop_words_file = open("stop_words.txt",encoding='gbk')
stop_words = list()
for line in stop_words_file.readlines():
    line = line.strip()   # 去掉每行末尾的换行符
    stop_words.append(line)
stop_words_file.close()
 
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
                            max_words = 1000,              # 设置最大会显示的字数
                            stopwords = stop_words,         # 设置停用词，应用导入的中文停用词库
                            max_font_size = 50,            # 设置字体最大值
                            random_state = 30,             # 设置有多少种随机生成状态
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
 
# 保存图片 
my_wordcloud.to_file(path.join(d, "cloudimg2.png"))
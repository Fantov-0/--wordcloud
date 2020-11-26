# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:56:11 2020

@author: Razer 14
"""

import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud
 
#打开本体TXT文件
text = open('sdxl.txt',encoding='gbk').read()
print (type(text))
 
#结巴分词 cut_all=True 设置为全模式 
wordlist = jieba.cut(text, cut_all = True)
 
#使用空格连接 进行中文分词
wl_space_split = " ".join(wordlist)

 
#对分词后的文本生成词云
my_wordcloud = WordCloud().generate(wl_space_split)
 
#显示词云图
plt.imshow(my_wordcloud)
#是否显示x轴、y轴下标
plt.axis("off")

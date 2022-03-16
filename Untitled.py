#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
# 한글 폰트 오류 해결
from matplotlib import rc

rc('font', family='Malgun Gothic') #Mac은 'AppleGothic'
# '-'코드로 인식안함
plt.rcParams['axes.unicode_minus'] = False


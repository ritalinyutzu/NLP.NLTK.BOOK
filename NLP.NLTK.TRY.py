from nltk.book import *

#搜尋字詞功能
text3.concordance("lived")
text3.concordance("LIVED")

#近似字
text1.similar("monstrous")

#回頭檢視結構
text1.common_contexts(["monstrous","abundant"])

#相異字詞
set(text4)

#相異字詞排序
sorted(set(text4))

#定義詞彙多樣性的函數
def lexical_diversity(text):
    return len(set(text))/len(text)
lexical_diversity(text4)   #result = 0.06556530042314962

#檢視制定美國民主相關字詞出現在整篇的頻率

#構造文本的詞彙分布圖
text4.dispersion_plot(["citizens","democracy","freedom","duties","America","liberty","constitution"])

#圖存在桌面, citizens雖然全篇出現,但主要集中在前半段,America在後半段才大量出現

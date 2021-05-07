'''
원핫인코딩(one hot encoding)
'''
from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "부산일과학고등학교에 오신 것을 환영합니다."

nouns = komoran.nouns(text)
print(nouns)

#단어 사전
dic = {}
for word in nouns:
    if word not in dic.keys() :
        dic[word] = len(dic)

print(dic)

#원핫 인코딩
nb_classes = len(dic)
targets = list(dic.values())
one_hot_targets = np.eye(nb_classes)[targets]

print(one_hot_targets)
'''
KoNLPy("코엔엘파이") : 한국어 정보처리를 위한 파이썬 패키지
'''
from konlpy.tag import Kkma 

#꼬꼬마 형태소 분리
kkma = Kkma()

text = "부산일과학고등학교에 오신 것을 환영합니다."

#형태소 추출
morphs = kkma.morphs(text)
print(morphs)

#명사만 추출
nouns = kkma.nouns(text)
print(nouns)


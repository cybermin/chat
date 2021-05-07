'''
KoNLPy("코엔엘파이") : 한국어 정보처리를 위한 파이썬 패키지
'''
from konlpy.tag import Kkma 
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
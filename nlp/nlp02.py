from konlpy.tag import Komoran

komoran = Komoran()
text = "부산일과학고등학교에 오신 것을 환영합니다."

morphs = komoran.morphs(text)
print(morphs)

pos = komoran.pos(text)
print(pos)

nouns = komoran.nouns(text)
print(nouns)
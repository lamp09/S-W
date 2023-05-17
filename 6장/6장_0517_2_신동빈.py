'''
파일 저장 명 : 5장_0517_2_신동빈.py

작성일 : 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 6장 시퀀스 자료형
        03. 문자열
'''
# 1. 문자열 생성
name = '신동빈'
name2 = '''
신
동
빈'''
print('name :',name)
print('name2 : ', name2)

# 빈 문자열 생성
text1 = ''
print('text1 의 길이 : ', len(text1))
text2 = str()
print('text2 의 길이 : ', len(text2))

# 정수를 문자열로 생성
text3 = str(1234)
print('text3 : ', text3)
print('text3 의 자료형 : ', type(text3))

# 리스트를 문자열로 생성
text4 = str([1,2,3])
print('text4 의 자료형 : ', type(text4))
# 리스트 자체를 문자열로 인식하여 '[' 가 출력 됨.
print('text4 의 0번지 값 : ', text4[0])

# 2. 문자여 메소드
# 대소문자 변환
text1 = 'i like python'
print('text1 내용의 첫 문자를 대문자로 변환 : ', text1.capitalize())
print('text1 내용의 모든 단어의 첫 문자를 대문자로 변환', text1.title())
text2 = text1.upper() # 대문자 변환
print('text2 의 모든 단어를 대문자로 변환 : ', text2)
text3 = text2.lower() # 소문자 변환
print('text3 의 모든 단어를 소문자로 변환 : ', text3)

# 문자열 정렬
print(text3.center(30,'*'))

# 문자 찾기
print('text3 의 "a" 몇개 있나요?', text3.count('a'))
print('text3 의 "i" 몇개 있나요?', text3.count('i'))
print('text3 의 인덱스 5부터 10까지 중에서 "i" 몇개 있나요?', text3.count('i',5,10))
print('text3 의 인덱스 5이후에 "o"가 몇개 있나요?', text3.count('o',5))

#문자열 내의 위치 - index(), find(), startswitch(), endswitch()
print('text3에 "k"의 인덱스 위치는?', text3.index('k'))
print('text3에 "k"의 인덱스 위치는?', text3.find('k'))

print('text3에 "python"의 인덱스 위치는?', text3.index('python'))
print('text3에 "python"의 인덱스 위치는?', text3.index('python'))
# 없으면 오류 발생
# print('text3에 "python1"의 인덱스 위치는?', text3.index('python1'))
# 없으면 -1을 반환(출력)
print('text3에 "python1"의 인덱스 위치는?', text3.find('python1'))
print('text3가 "i like" 로 시작하는가? ', text3.startswith('i like'))
print('text3가 "abc"로 끝나는가?', text3.endswith('abc'))

# 문자열 결합
# 리스트 생성
list1 = ['1', '2', '3', '4', '5']
print('list1 내용에 "-"를 결합 : ', '-'.join(list1))
list2 = [1,2,3,4,5]
# 오류발생 정수와 문자는 연결이 안됨.
# join()의 대상은 반드시 문자열이어야 함
# print("list2 내용에 '-' 를 결합 : "), '-'.join(list2)

# 딕셔너리 생성 - 키 : 값(key:value)
dict1 = {'apple': '사과', 'grape' : '포도', 'peach' : '복숭아'}
# 키 (key)에 해당하는 문자열에 조인
print("dict1 내용에 '-' 를 결합 : "), '-'.join(dict1)

# 문자열 분리 - split()
text1 = 'I Like Python Language'
list1 = text1.split() # 문자열을 스페이스로 분리하여 리스트로 반환
print('text1 내용을 스페이스로 분리하여 리스트 생성 : ', list1)

text2 = 'I-Like-Python-Language'
print('text2 내용을 "-"로 분리하여 리스트로 반환 : ', text2.split('-'))

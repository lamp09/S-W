'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 8장 파일 입출력
'''
         
print("== 학생 정보 읽어오기1 ==")
with open('student.txt', 'r') as f :
    while True :
        student = f.readline()
        print(student, end='')
        
        
        if student == '' :
            break
        
print("== 학생 정보 읽어오기2 ==")
with open('student.txt', 'r') as f :
    while True :
        student = f.readline()
        studentlist = student.split()   # 빈칸을 기준으로 리스트 객체로 변환
        print(studentlist)
        
        if student == '' :
            break
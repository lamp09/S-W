'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 8장 파일 입출력
'''

# 3과목의 평균 점수를 계산하여 출력

print("== 학생 정보 읽어오기2 ==")
with open('student.txt', 'r') as f :
    while True :
        student = f.readline()
        if student == '' :
            break
        
        
        studentlist = student.split()   # 빈칸을 기준으로 리스트 객체로 변환
        name = studentlist[0] # 첫 번째 항목을 name에 저장
        
        sum = 0
        for i in range(1,4) :
           sum = sum + int(studentlist[1])
            
        print('{}의 평균 성정 : {}점 '.format(name, sum/3))
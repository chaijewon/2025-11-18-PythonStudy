'''
money=1000
age=25
if money>=500:
    item="사과"
    if age<=30:
        msg="new"
    else:
        msg="old"
    print(item,msg)
'''
'''
  반복문 
  while / for 
  while : 무한루프 = 지정된 횟수가 없는 경우 
  for : 횟수가 지정된 경우 
  
  while 형식 
  초기화 
  while 조건문:
    반복수행문장 
    증가식
'''
i=1
while i<=10:
    print("i=%d" %i)
    i+=1 #i=i+1
print("===============") # \n
i=1
while i<=10:
    if i%2==0:
        print("i=%d" %i)
    i+=1
print("===============")
i=1
while i<=10:
    if i%2!=0:
        print("i=%d" %i)
    i+=1
print("===============")
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(f"1~100까지 누적합:{sum}")

sum=even=odd=0
i=1
while i<=100:
    if i%2==0:
        even+=i
    else:
        odd+=i
    sum+=i
    i+=1
print(f"1~100 누적합:{sum}")
print(f"1~100 홀수합:{odd}")
print(f"1~100 짝수합:{even}")
print("======================")
#단을 입력받아서 구구단 출력
i = 1
dan=int(input("(2~9)단 입력:"))
while i<=9:
    print(f"{dan} * {i} = {dan*i}")
    i+=1


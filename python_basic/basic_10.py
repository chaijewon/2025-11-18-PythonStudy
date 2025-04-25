'''
  함수 : 한개의 기능을 모아서 재사용이 가능
        = 명령문을 모아서 처리
        = 변수 , 연산자  제어문
        = 기능 한개만 수행이 가능
        = 종류
          1) 라이브러리 : 제공 = 필요시마다 재사용
             print , range ... append
          2) 사용자 정의
          = 리턴형 : 여러개 전송이 가능
            return "a","b"
          = 매개변수 : 여러개 / 없는 경우
          = 함수명 : 변수의 식별자와 동일
          = 형식
            def 함수명(매개변수..):
                처리
                return ...
            => function 함수명(매개변수..)
            => fun 함수명(매개변수){} => 코틀린
               var(변수),val(상수)
            => dart

        1. 함수 형식
        --------------------------
             리턴형     매개변수
        --------------------------
               O          O
               def 함수명(매개변수):
                   처리문장
                   return 값
        --------------------------
               def 함수명():
                   처리문장
                   return 값
               O          X
        -------------------------- void
               def 함수명(매개변수):
                   처리문장
               X          O
        --------------------------
              def 함수명():
                   처리문장
               X          X
        --------------------------
        System.out.printlf("%d",1)
        System.out.printlf("%d%d%d%d%d",1,2,3,4,5)
        매개변수 => 가변 매개변수
                   def func(*args) => ...
                    func(1) func(2) func(1,2,3)
                   default 매개변수
                   => 매개변수는 뒤에서부터 처리
                   def 함수명(매개변수,매개변수=값,매개변수=값)
                   def func(a=10,b=20,c=30)
                   func() => a=10 ,b=20 ,c=30
                   func(100)  => a=100 b=20 c=30
'''
#print("Hello")
#print("Hello",end=" ")
# 1. 리턴형(X),매개변수(X)
'''
   30,40,10,50,20
   --
   10  
      -- -- -- --
      40 30 50 20 
      40
         -- -- --
      30 40 50 20
      20 40 50 30
      -- -- --
         40 50
         --    --
         30    40
            50 40
            -- --
            40 50 
               --
   
'''

def sort():
    #지역변수
    data=[30,40,10,50,20]
    #리스트형 => 중복 저장이 가능 , 수정이 가능
    #튜플형 (30,20,...) = 수정이 불가능 => 데이터베이스 SELECT
    #튜플=> 리스트형으로 변환
    #셀형 => {} : Set , 딕트 [키,값] => JSON Map
    print(f"정렬전:{data}")
    # for(int i=0;i<arr.length-1;i++)
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if data[i]>data[j]:
                 temp=data[i]
                 data[i]=data[j]
                 data[j]=temp
    print(f"정렬후:{data}")
sort()
#  리턴형이 있는 경우 , 매개변수는 없는 경우
def getInfoData():
    return "홍길동"

name=getInfoData()
print(name)

def getInfoData2():
    return "심청이",25,"여자"
name,age,sex=getInfoData2()
print(f"이름:{name}")
print(f"나이:{age}")
print(f"성별:{sex}")

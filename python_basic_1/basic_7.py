# 내장 데이터베이스가 존재 sqlite => 4만개
'''
   1. 함수 (사용자 정의)
      = 웹 연결 => URL을 읽어서 해당 함수를 호출
                  -----------
 urlpatterns=[
   path('',views.main_page),
   def main_page(request):
         recipe_data=models.mainRecipeData()
         """
           [
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
           ]
         """
         food_data=models.mainFoodData()
         rd=[]
         for r in recipe_data:
             rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
             rd.append(rdata)
         fd=[]
         for f in food_data:
             fdata={"fno":f[0],"name":f[1],"poster":f[2]}
             fd.append(fdata)
         #chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7 => Tuple ()
         cdata=models.chefMainData()
         cd={
              "chef":cdata[0],
              "poster":cdata[1],
              "mc1":cdata[2],
              "mc2": cdata[3],
              "mc3": cdata[4],
              "mc7": cdata[5]
         }
         #(poster,name,jjimcount,hit,theme)
         tdata=models.todayFoodData()
         td={
             "poster":tdata[0],
             "name":tdata[1],
             "jjimcount":tdata[2],
             "hit":tdata[3],
             "theme":tdata[4]
         }
         """
           1. list => []
           2. Tuple => (1,"aaa"...)
           3. Dict  => {키:값} => JSON , Map
         """
         news_data=models.newsData("맛집")
         #print(news_data.encode('utf-8'))
         main_data={
            "rd":rd,
            "fd":fd,
            "cd":cd,
            "td":td,
            "nd":news_data['items']
         }
         """
           list  =>  배열 [] = arraylist
           tuple => () = 데이터베이스 연결
           dict => {} = map
         """
    #return render(request,"main/home.html",main_data)
         return JsonResponse(main_data)
   path('food/list/',food_views.food_list),
   path('food/find/',food_views.food_find),
   path('recipe/list/',recipe_views.recipe_list_view),
   path('recipe/list_vue/',recipe_views.recipe_list),
   path('recipe/find/',recipe_views.recipe_find_view),
   path('recipe/find_vue/',recipe_views.recipe_find),
   path('recipe/chef/',recipe_views.recipe_chef_view),
   path('recipe/chef_vue/',recipe_views.recipe_chef),
   path('food/food_detail/',food_views.food_detail),
   path('recipe/detail/',recipe_views.recipeDetailView),
   path('recipe/detail_vue/',recipe_views.recipeDetail),
   path('goods/list/',goods_views.goods_list),
   path('recipe/chef_detail/',recipe_views.chef_detail)
   => VueJS axios('recipe/chef_detail/')

                         GateWay => MSA
         현재               |
                 ---------------------
                |           |        |
              NodeJS   Spring-Boot Django
                |          |          |
                -----------------------
]
'''
'''
   함수 형식
   --------
    def 함수명(매개변수...):
          기능 처리 
          return 값,값 => 없는 경우에는 사용하지 않는다 (void)
                 -----  return값이 여러개인 경우도 있다 
    *** 파이썬은 기본 => 데이터형 사용하지 않는다 
                       --------------------
                        => 가독성 (X)
    *** 수집 / 분석 / 통계 => 시각화 
    자바 => 웹 
    C => 하드웨어 
    C# => 웹 MS      
'''
import pymysql as pm
#연결
def getConnection():
    conn=pm.connect(host="127.0.0.1",user="root",
                password="happy",db="mydb",charset="utf8")
    return conn
# 해제
def disConnection(conn,cur):
    cur.close()
    conn.close()

# 전체 목록 읽기
def empListData():
    conn=getConnection()
    cur=conn.cursor()
    sql="""
         SELECT empno,ename,sal,job,
         date_format(hiredate,'%Y-%m-%d'),
         dname,loc
         FROM emp JOIN dept 
         ON emp.deptno=dept.deptno
        """
    cur.execute(sql)
    emp_list=cur.fetchall()
    disConnection(conn,cur)
    return emp_list
# 검색
# 상세보기

# 전체 기능 수행
def main():
    while(True):
        print("1.사원목록")
        print("2.사원검색")
        print("3.상세보기")
        print("4.종료")
        menu=int(input("메뉴 선택:"))
        if menu==4:
            print("프로그램 종료")
            break
        elif menu==1:
            emp_list=empListData()
            for emp in emp_list:
                e=list(emp)
                print(e)
        elif menu==2:

        elif menu==3:

main()






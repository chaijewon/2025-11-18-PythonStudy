import pymysql as pm
conn=pm.connect(host="127.0.0.1",
        user="root",password="happy",
        db="mydb",charset="utf8")
cur=conn.cursor()
cur.execute("select * from genie_music")
data=cur.fetchall();
#print(data)
#data1=list(data)
for row in data:
    music=list(row)
    for d in music:
        print(d,end=" ")
    print()

conn.close()

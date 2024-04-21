import pymysql
import os

# pip install pymysql <<설치!!

#pip install scikit-learn 
#pip install scipy
#pip install matplotlib
#pip install mglearn



# 한글 지원 환경
os.putenv('NLS_LANG', '.UTF8')
# Path 설정
#LOCATION = r"G:/instantcli"
#os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]
# DB 연결
connect = pymysql.connect(host='127.0.0.1',port = 3306, user='root', password='java', db='pymysql', charset='utf8')
cs = connect.cursor()#얘가 커서라는 애임
# 데이터 추가(insert)
#sql = "insert into pymysql values('kang', '1234', '강감찬', 45)"
#cs.execute(sql) # SQL문
cs.execute("select * from pymysql") # SQL문
#for i in cs: # data 보기
#    print(i)
while ( True ) :
    row = cs.fetchone()
    if row == None :
        break;
    print( row[0], ' | ', row[1], ' | ', row[2],' | ', row[3] )


# 나이가 40세 이상인 record
sql = "SELECT * FROM pymysql WHERE AGE >= 40"
cs.execute(sql)
# name이 '강감찬'인 데이터의 age를 40으로 수정
sql = "UPDATE pymysql SET AGE = 45 WHERE NAME = '강감찬'"
cs.execute(sql)
# 수정된 레코드 조회
sql = "SELECT * FROM pymysql WHERE NAME = '강감찬'"
cs.execute(sql)
#홍길동을 추가
#sql = "INSERT INTO pymysql VALUES('CHOI', '1144', '최길동', 32)"
#cs.execute(sql)
#for i in cs: # data 보기
#    print(i)
# name이 '홍길동'인 레코드 삭제
sql = "DELETE FROM pymysql WHERE NAME = '홍길동'"
cs.execute(sql)
# 전체 레코드 조회
sql = "SELECT * FROM pymysql"
cs.execute(sql)
for i in cs: # data 보기
    print(i)

# 사용 후 close
cs.close()
connect.commit()
connect.close()


from sklearn.datasets import load_iris
iris_dataset = load_iris()
#print(iris_dataset)

import matplotlib.pyplot as plt
# venv > Scripts > activate 실행해서 라이브러리가 설치된 가상환경 접속
# pip install matplotlib

# 산포도 데이터 생성
x = [1, 2, 3, 4, 5]  # x축 데이터
y = [2, 4, 6, 8, 10]  # y축 데이터

# 산포도 그리기
plt.scatter(x, y)

# 그래프에 제목과 축 레이블 추가
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")

# 그래프 표시
plt.show()
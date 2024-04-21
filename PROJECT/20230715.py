import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, confusion_matrix
import seaborn as sns


#겅로 설정 필수!
# 데이터 불러오기
titanic = sns.load_dataset("titanic")


#데이터 안 칼럼 명 반드시 확인(대소문자 유의, 얘 대소문자 다른거 인지 못함.)
#print(df.columns)#확인 완

# 필요한 열 선택(필요나 결과에 따라, 추가 혹은 삭제 요망)
selected_columns = ['age', 'sex', 'fare', 'pclass', 'survived']
titanic = titanic[selected_columns]

# 결측치 처리(널값, 싹 없애버리기)
titanic = titanic.dropna()

# 원-핫 인코딩(문자열을 숫자로 변환// 남.여를 0과 1로)
titanic_encoded = pd.get_dummies(titanic, columns=['sex'])

# 독립 변수와 종속 변수로 나누기
X = titanic_encoded.drop('survived', axis=1)
y = titanic_encoded['survived']

# 훈련 세트와 테스트 세트로 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# 로지스틱 회귀 모델 훈련하기(진짜 이걸로 끝나니, 너)
model = LogisticRegression()#이곳에 모듈 준비
model.fit(X_train, y_train)#모듈 셋팅

# 예측하기
y_pred = model.predict(X_test)

# 분류 성능 측정
accuracy = accuracy_score(y_test, y_pred)
#precision = precision_score(y_test, y_pred)
#recall = recall_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 결과 출력
print("정확도:", accuracy)
#print("정밀도:", precision)
#print("재현율:", recall)
print("정확성 :", roc)
print("F1 점수:", f1)

#이하 혼동 행렬 : 모델의 예측과 실제 결과 사이 오차를 행렬로 시각화.(평가 분석시 사용)
print("혼동 행렬:")#보기 편한걸 위해 cm은 프린트시 줄바꿈 적용
print(cm)





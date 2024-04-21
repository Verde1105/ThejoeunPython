from django.apps import AppConfig


class PyboConfig(AppConfig):
    name = 'pybo'#이 클래스가 셋팅.py 파일의 앱 항목에 추가 되어 있지 안다면, 장고는 이녀석을 인식못하는것 뿐만 아니라, 데이터베이스 관련 작업도 못하게된다! 주의!

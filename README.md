# BTC-PaperWallet-Generator
Wallet(HDKey) 아닌 개인키/공개키 쌍만 생성하고 싶을 경우를 위해 작성함.  
이 리포는 사실상 **bitcoinlib의 래퍼 클래스** 에 QR코드 생성을 혼합한 클래스 패키지임.


---

## Quick Start
1. 루트 디렉토리의 quickstart.py 파일을 열어 최상단에 비밀번호를 입력하시오.  
   Open quickstart.py and set your password
2. 그 후 실행하면 outputs 디렉토리 안에 비밀번호로 암호화된 개인키 QR, 공개 주소 QR이 저장됩니다.  
    Run it and you get two QR codes in the outputs folder.

---


Python Version : 3.10.19


* Environment Tool : pyenv


```shell
pip install -r requirements.txt
```
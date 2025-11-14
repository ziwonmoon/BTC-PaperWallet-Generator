# BTC-PaperWallet-Generator
**This tool is a non-custodial, offline key pair and QR code generator for creating static Bitcoin paper wallets.  
이 리포는 엄밀한 의미의 페이퍼월렛 생성기가 아니며, 단 하나의 키 쌍과 그 QR코드를 생성하도록 만들어졌습니다.**

Wallet(HDKey) 아닌 개인키/공개키 쌍만 생성하고 싶을 경우를 위해 작성함.  
이 리포는 사실상 **bitcoinlib의 래퍼 클래스** 에 QR코드 생성을 혼합한 클래스 패키지임.  
<br>
**안전한 사용을 위해서는, Git Clone -> Install Libraries -> Disconnect from Internet -> Generate Key Pair -> Delete All Files(including this repo) -> Connect Internet 의 단계를 따르십시오**

### If you just want to make a pair of the private key and the public address, see the "Quick Start" part below.

---

## Quick Start
1. 루트 디렉토리의 quickstart.py 파일을 열어 최상단에 비밀번호를 입력하시오.  
   Open quickstart.py and set your password
2. 그 후 실행하면 outputs 디렉토리 안에 비밀번호로 BIP-38 암호화된 개인키 QR, 공개 주소 QR이 저장됩니다.  
    Run it and you get two QR codes in the outputs folder. (BIP-38 Private Key and Public Address)

## If you want use Docker (not want to setup the environment)
(환결 설정 필요 없음)  
```Shell
docker build -t btc-paper-wallet .
docker run -v $(pwd)/outputs:/app/outputs btc-paper-wallet
```

---


Python Version : 3.10.19


* Environment Tool : pyenv


```shell
pip install -r requirements.txt
```

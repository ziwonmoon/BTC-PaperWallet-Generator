from bitcoinlib.keys import Key


class KeyManager:
    def __init__(self, new_key, import_key=None, passwd=None):
        if new_key == True:
            self.__key = Key()
            if passwd != None:
                self.__encrypted_key = self.__key.encrypt(passwd)
        else:
            self.__key = Key(import_key=import_key, password=passwd)


        self.__private_key = self.__key.wif()
        self.__public_address = self.__key.address()

    @property
    def private_key(self):
        print("[WARNING] 비밀키를 직접 다룰 때는 보안에 유의하십시오.")
        print("YOU MUST KNOW THAT IT IS DANGEROUS TO HANDLE THE PRV KEY")
        return self.__private_key
    
    @property
    def encrypted_private_key(self):
        return self.__encrypted_key

    @property
    def public_address(self):
        return self.__public_address
    
    
    
        
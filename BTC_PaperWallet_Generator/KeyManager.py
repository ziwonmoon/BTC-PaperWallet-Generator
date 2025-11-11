from bitcoinlib.keys import Key
import qrcode

class KeyManager:
    def __init__(self, new_key : bool, import_key=None, passwd=None):
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
    
    def get_private_key_QR(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=8
        )
        qr.add_data(self.private_key)
        qr.make()
        img = qr.make_image()
        img.save("outputs/UNENCRYPTED_Private_Key.png")

    def get_encrypted_private_key_QR(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=8
        )
        qr.add_data(str(self.encrypted_private_key))
        qr.make(fit=False)
        img = qr.make_image()
        img.save("outputs/encrypted_Private_Key.png")

    def get_public_address_QR(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=8
        )
        qr.add_data(self.public_address)
        qr.make()
        img = qr.make_image()
        img.save("outputs/public_address.png")
        

    
    
        
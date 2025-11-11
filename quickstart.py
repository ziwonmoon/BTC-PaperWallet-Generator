PASSWORD = 'YOUR_PASSWORD'




from BTC_PaperWallet_Generator.KeyManager import KeyManager

mykey = KeyManager(True, None, passwd='PASSWORD')

mykey.get_encrypted_private_key_QR()
mykey.get_public_address_QR()
class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        return cipher.iv + ciphertext

    def decrypt(self, data):
        iv, ciphertext = data[:AES.block_size], data[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return plaintext
import unittest
from encryption import encrypt, decrypt
from auth import hash_password, check_password
from user import User

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        # Test encryption and decryption
        plaintext = b'This is a test message'
        ciphertext = encrypt(plaintext)
        self.assertNotEqual(plaintext, ciphertext)
        decrypted_plaintext = decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_plaintext)

class TestAuthentication(unittest.TestCase):
    def test_hash_check_password(self):
        # Test password hashing and checking
        password = 'password123'
        hashed_password = hash_password(password)
        self.assertTrue(check_password(password, hashed_password))
        self.assertFalse(check_password('wrong_password', hashed_password))

    def test_user_authentication(self):
        # Test user authentication
        user = User('admin', 'password123')
        self.assertTrue(user.authenticate('password123'))
        self.assertFalse(user.authenticate('wrong_password'))

if __name__ == '__main__':
    unittest.main()

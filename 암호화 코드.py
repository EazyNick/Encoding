from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# 암호화에 사용할 키와 IV (Initialization Vector)를 생성합니다.
key = get_random_bytes(16)  # 128비트 키
iv = get_random_bytes(16)   # AES는 블록 암호이므로 IV가 필요합니다.

# 암호화할 메시지
message = "널 사랑해".encode('utf-8')

# AES 암호화 객체를 생성합니다.
cipher = AES.new(key, AES.MODE_CBC, iv)

# 메시지를 패딩하여 16바이트의 배수로 만듭니다.
padded_message = pad(message, AES.block_size)

# 메시지를 암호화합니다.
encrypted_message = cipher.encrypt(padded_message)

# 암호화된 메시지를 base64로 인코딩하여 출력합니다.
encrypted_message_base64 = base64.b64encode(iv + encrypted_message).decode('utf-8')
key_base64 = base64.b64encode(key).decode('utf-8')

print(f"암호화된 메시지: {encrypted_message_base64}")
print(f"암호화 키: {key_base64}")

# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# import base64

# # 암호화된 메시지와 키
# encrypted_message_base64 = "J7MkOZ7Rt+KZjkKlxXlnJ4nqR4Fj2N0Ke1H8pPm2sHss9CuV3WvUjA=="  # 위에서 출력된 값
# key_base64 = "xK3Jh8TQyYyrAbG1TkxAdg=="  # 위에서 출력된 값

# # base64로 인코딩된 데이터를 디코딩합니다.
# encrypted_message_with_iv = base64.b64decode(encrypted_message_base64)
# key = base64.b64decode(key_base64)

# # IV와 암호화된 메시지를 분리합니다.
# iv = encrypted_message_with_iv[:16]
# encrypted_message = encrypted_message_with_iv[16:]

# # AES 복호화 객체를 생성합니다.
# cipher = AES.new(key, AES.MODE_CBC, iv)

# # 메시지를 복호화하고 패딩을 제거합니다.
# decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

# # 복호화된 메시지를 UTF-8로 디코딩하여 출력합니다.
# print(f"복호화된 메시지: {decrypted_message.decode('utf-8')}")

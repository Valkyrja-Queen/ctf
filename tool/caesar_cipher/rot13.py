# シーザー暗号解析ツール

def caesar_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            # 大文字の場合
            if char.isupper():
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            # 小文字の場合
            else:
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

print("解析対象を入力てください:")
target = input()

decode = caesar_cipher(target)
print("解析結果：" + decode)

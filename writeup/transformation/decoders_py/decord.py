def encode_string(s):
    if len(s) % 2 != 0:
        s += '\0'  # 長さが奇数の場合、末尾にヌル文字を追加
    return ''.join([chr((ord(s[i]) << 8) + ord(s[i + 1])) for i in range(0, len(s), 2)])

def decode_string(encoded):
    decoded_chars = []
    for char in encoded:
        value = ord(char)
        decoded_chars.append(chr(value >> 8))  # 上位バイト
        decoded_chars.append(chr(value & 0xFF))  # 下位バイト
    decoded_string = ''.join(decoded_chars)
    return decoded_string.rstrip('\0')  # デコードした文字列の末尾のヌル文字を削除

def main():
    choice = input("文字列を直接入力する場合は1を、ファイルから読み込む場合は2を入力してください: ")

    if choice == '1':
        # ユーザーにエンコードされた文字列の入力を求める
        encoded_string = input("エンコードされた文字列を入力してください: ")
    elif choice == '2':
        # ファイル名の入力を求める
        file_path = input("ファイルのパスを入力してください: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                encoded_string = file.read().strip()  # ファイルの内容を読み込む
        except FileNotFoundError:
            print("ファイルが見つかりませんでした。")
            return
    else:
        print("無効な選択肢です。")
        return

    # デコード処理を実行
    decoded_string = decode_string(encoded_string)

    # デコード結果を表示
    print("デコードされた文字列:", decoded_string)

if __name__ == "__main__":
    main()


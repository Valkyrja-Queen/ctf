# 10進数のASCIIコードを文字に変換するツール

def convert_ascii(text):
    char = chr(int(text))

    return char

def select_mode():
    mode = input("""ASCIIコードを入力して変換する：１\nASCIIコードのファイルを読み込んで実行する：２\nモードを選択してください(1or2)：""")
    if mode == "1":
        target = input("変換したいASCIIコードを入力してください：")
        print(convert_ascii(target))
    elif mode == "2":
        target_f = input("ファイルのパスを入力してください：")
        with open(target_f, "r") as file:
            # ファイルの各行を順番に処理する
            for line in file:
                # strip()で改行文字を取り除く
                line = line.strip()

                print(convert_ascii(line), end="")
    else:
        print("1か2を入力してください\n")
        select_mode()

select_mode()

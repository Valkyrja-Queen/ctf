#!/bin/bash

# 配列の定義
array=("Kotlin" "Cobol" "Scala" "Perl" "Ruby" "Python" "Go" "Rust" "C" "C++" "C#" "PHP" "Java" "JavaScript")

# 配列の長さを取得
length=${#array[@]}

# 0から配列の長さ-1までのランダムなインデックスを生成
random_index=$((RANDOM % length))

# ランダムに選ばれた要素を取得
random_element=${array[$random_index]}

# 選ばれた要素を表示
echo "使用する言語: $random_element"


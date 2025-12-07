#!/bin/bash

# 使用方法: ./script.sh <チャレンジプログラムのパス>
# 例: ./script.sh ./challenge

if [ $# -eq 0 ]; then
  echo "使用方法: $0 <チャレンジプログラムのパス>"
  echo "例: $0 ./challenge"
  exit 1
fi

CHALLENGE="$1"
LENGTH=13

if [ ! -x "$CHALLENGE" ]; then
  echo "エラー: $CHALLENGE が実行可能ではありません"
  exit 1
fi

echo "チャレンジプログラム: $CHALLENGE"
echo "フラグ長: $LENGTH 文字"
echo "================================"
echo ""

# 印字可能なASCII文字の範囲で総当たり
# 実際にはフラグフォーマット（例: FLAG{...}）がわかっている場合は
# その範囲に絞ると効率的

# まず、各位置でどの文字が正しいかを特定する戦略
# "Wrong at index X" のメッセージから1文字ずつ特定

flag=""

for pos in $(seq 0 $((LENGTH - 1))); do
  echo "位置 $pos を探索中..." >&2
  found=0

  # 印字可能ASCII文字（32-126）を試す
  for ascii in $(seq 32 126); do
    char=$(printf "\\$(printf '%03o' $ascii)")

    # 現在までのフラグ + 試行文字 + 残りをダミー文字で埋める
    test_input="${flag}${char}"
    for ((i = ${#test_input}; i < LENGTH; i++)); do
      test_input="${test_input}A"
    done

    # チャレンジプログラムに入力
    result=$(echo "$test_input" | "$CHALLENGE" 2>&1)

    # "Wrong at index X" を確認
    if echo "$result" | grep -q "Wrong at index"; then
      wrong_index=$(echo "$result" | grep -oP 'Wrong at index \K\d+')
      if [ "$wrong_index" -gt "$pos" ]; then
        # この位置は正解
        flag="${flag}${char}"
        echo "位置 $pos: '$char' (ASCII $ascii) ✓" >&2
        found=1
        break
      fi
    elif echo "$result" | grep -q "Correct"; then
      # 完全一致
      flag="${flag}${char}"
      echo "位置 $pos: '$char' (ASCII $ascii) ✓" >&2
      found=1
      break
    elif echo "$result" | grep -q "Wrong length"; then
      continue
    fi
  done

  if [ $found -eq 0 ]; then
    echo "位置 $pos で文字が見つかりませんでした" >&2
    exit 1
  fi
done

echo ""
echo "================================"
echo "発見したフラグ: $flag"
echo ""

# 最終確認
echo "最終確認中..." >&2
result=$(echo "$flag" | "$CHALLENGE" 2>&1)
echo "$result"

#!/bin/bash

# 使用方法: ./script.sh <テスト対象のコマンド>
# 例: ./script.sh "wc -c"

if [ $# -eq 0 ]; then
  echo "使用方法: $0 <テスト対象のコマンド>"
  echo "例: $0 'wc -c'"
  exit 1
fi

TARGET_CMD="$1"

echo "テスト対象: $TARGET_CMD"
echo "================================"
echo ""

# 1から100まで繰り返す
for length in {1..100}; do
  # 指定された長さの0埋め文字列を生成
  input=$(printf '%0*d' "$length" 0)

  # プログラムに渡して結果を取得
  result=$(echo -n "$input" | eval "$TARGET_CMD" 2>&1)

  # 結果を表示
  printf "長さ %3d: %s\n" "$length" "$result"
done

echo ""
echo "================================"
echo "テスト完了"

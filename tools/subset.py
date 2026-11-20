# -*- coding: utf-8 -*-
"""
字體精簡工具：只保留策展頁用得到的字，2MB 的字體可縮到約 20KB
用法：
  1. pip install fonttools brotli
  2. 把頁面新增的文字加進 chars.txt（同一個字出現一次即可）
  3. python3 subset.py 原始字體.ttf 輸出檔名.woff2
注意：沒有收進 chars.txt 的字，在頁面上會退回成黑體
"""
import subprocess, sys, os

src, out = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
subprocess.run(['pyftsubset', src,
                f'--text-file={os.path.join(here, "chars.txt")}',  # 要保留的字
                '--flavor=woff2',                                  # 網頁用壓縮格式
                f'--output-file={out}'], check=True)
print('完成：', out, os.path.getsize(out) // 1024, 'KB')

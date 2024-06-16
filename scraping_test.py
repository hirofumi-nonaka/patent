import requests
from bs4 import BeautifulSoup
# スクレイピング対象のURL
address = 'https://www.takayamaweb.co.jp/'
# ページのHTMLを取得
response = requests.get(address)
html = response.text
# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html, 'html.parser')
# tableタグを抽出
tables = soup.find_all('table')
# 最初のテーブルの内容を表示
if tables:
     first_table = tables[0]
     print("最初のテーブル:")
     print(first_table)
else:
     print("テーブルは見つかりませんでした。")

import pandas as pd
# # スクレイピング対象のURL
address = 'https://www.takayamaweb.co.jp/'
# # HTMLからtable要素を読み込む
tables = pd.read_html(address)
# # 各テーブルの内容を表示
if tables:
 for idx, table in enumerate(tables):
    print(f"テーブル {idx+1}:")
    print(table)
    print("\n")
else:
    print("テーブルがありませんでした")

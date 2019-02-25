# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
import os
import requests

# url先の画像を保存する関数
def download(url,name):
    img = request.urlopen(url)
    path = "./"+name+"/"+os.path.basename(url)
    localfile = open(path, 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()

def main():
	dir_name = input('plz dir_name:')
	os.makedirs(dir_name,exist_ok=True)

	# アクセス先
	access_url = input('URL:')
	
	# urlアクセス
	try:
		res = requests.get(access_url)
		res.raise_for_status()
	except OSError:
		print("ERROR PLZ URL")
		return
	# beautifulsoupでパース
	soup = BeautifulSoup(res.text,"lxml")
	# 画像URLを取得
	image_selecter = input('plz img selecter:')
	# ページに存在するimgタグを検索
	tag = soup.select(image_selecter)

	if tag == []:
		print("NOT FOUND")
		return

	# 画像URLを取得
	for i in range(len(tag)):
		img_url = tag[i].get('src')
		print(img_url)
		# ローカルに画像をダウンロード
		download(img_url,dir_name)


if __name__ == '__main__':
	main()


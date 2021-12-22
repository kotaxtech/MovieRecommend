# MovieRecommend
概要：あなたのおすすめする映画を３つまで他のユーザーと共有できるWEBアプリケーション

今後の展望：以下の点を実装したいと考えています。
- APIを用いて映画タイトルの入力欄に検索機能を追加する。
- APIの情報から該当する映画ジャケットを取得しTOPページに表示する。

# デモ
![movie](https://user-images.githubusercontent.com/66913031/111263412-2d062e80-8669-11eb-8255-f3acef9ee604.gif)

※事前にいくつかユーザーを作っているので、TOPページの概観は少々異なります。


# 使い方
### Githubからclone
Github上からソースコードをローカルPC上にcloneします。
```
$ git clone git@github.com:K-out-A/MovieRecommend.git
```
cloneしたディレクトリ上に移動します。
```
$ cd MovieRecommend
```

### 動作環境の構築
仮想環境を作成します。（そのまま実行すると既存のパッケージに干渉してエラーが起きる可能性があるためです。）
```
$ python3 -m venv myvenv
```
仮想環境を実行します。
```
$ source myvenv/bin/activate
```
必要なライブラリを仮想環境上にinstallします。（requirements.txtの中に必要なライブラリのリストが入っています。）
```
$ pip3 install -r requirements.txt
```

### ソースコードの実行
以下のコードを順に実行します。
```
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver
```

http://127.0.0.1:8000/ にアクセスして、デモ動画の冒頭ページが表示されたら成功です。

# 動作環境の詳細
- Ubuntu 18.04.5 LTS
- Python 3.7.3
- Django 3.1.2
- Pillow 2.2.1

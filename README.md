# SELENIUM-PRACTICE
## 目次
- [任意地の最高気温を取得](#任意地の最高気温を取得)
    - [目次](#目次)
    - [事前準備](#事前準備)
    - [.envファイルの設定事項](#envファイルの設定事項)
    - [実行方法](#実行方法)

## 事前準備
- カレントディレクトリ直下に`.env`ファイルを作成

## .envファイルの設定事項
以下のチェックリストに該当するものがあった場合`.env`ファイルを書き換えること
- 実行環境関連パラメータ
    - 開発環境の場合`ENVIRONMENT=True`、本番環境の場合`ENVIRONMENT=False`
- スクリーンショットパラメータ
    - スクリーンショットを取得する場合`SCREENSHOT=True`、取得しない場合`SCREENSHOT=False`
    - スクリーンショットは`./data`ディレクトリに保存される
    - スクリーンショットのファイル名は`{実行日時}_screenshot.png`となる
- 任意地パラメータ
    - `X_POSITION`, `Y_POSITION`に任意地を設定する
    - 任意地は[こちら](https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/index_mxtem.html)の検証から確認できる(例: `X_POSITION=-270`, `Y_POSITION=-1500` => `福岡`)
    - 指定方法はこれから改善していく予定

## 実行方法
1. pipenvのインストール
    ```bash
    $ pip install pipenv
    ```
2. 依存パッケージのインストール
    ```bash
    $ pipenv install
    ```
3. `.env`ファイルを作成
4. `.env`ファイル内で各種設定を行う
    ⇒ [`.env`ファイルの設定事項](#envファイルの設定事項)
5. 実行
    ```bash
    $ pipenv run start
    ```

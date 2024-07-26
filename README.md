# GPT Command Executor

このプロジェクトは、OpenAIのGPT-4を使用してユーザーのクエリに基づいたシェルコマンドを提案し、選択・実行するためのPythonスクリプトです。

## 概要
このスクリプトは、ユーザーからのクエリを受け取り、OpenAIのAPIを使用して適切なシェルコマンドを生成します。生成されたコマンドは`fzf`を使って選択され、ユーザーの確認のもと実行されます。

## 必要な前提条件
- Python 3.x
- OpenAI APIキー
- `fzf` (コマンドラインツール)

## インストール手順
1. このリポジトリをクローンします。
    ```sh
    git clone <リポジトリのURL>
    cd <リポジトリ名>
    ```

2. 必要なPythonライブラリをインストールします。
    ```sh
    pip install openai python-dotenv
    ```

3. `.env`ファイルを作成し、OpenAI APIキーを設定します。
    ```sh
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    ```

4. `fzf`をインストールします。
    ```sh
    sudo apt-get install fzf
    ```

## 使用方法
1. `gpt`コマンドを実行します。
    ```sh
    python gpt.py "<クエリ>"
    ```
    例:
    ```sh
    python gpt.py "システムのアップデート方法"
    ```

2. 提案されたコマンドが`fzf`に表示されます。適切なコマンドを選択します。

3. 選択したコマンドを実行するかどうか確認されます。`YES`と入力して実行します。

## ファイル構成の説明
- `gpt.py`:
    - メインのスクリプト。クエリを受け取り、OpenAIのAPIを使用して応答を取得し、fzfでコマンドを選択・実行します。
- `prompt.py`:
    - プロンプト生成のための関数を含みます。クエリと現在の状況に基づいてOpenAIに送信するプロンプトを生成します。
- `.env`:
    - 環境変数を設定するファイル。OpenAI APIキーを含めます。

## エラーハンドリングについて
- `gpt.py`内の`get_gpt_response`関数および`execute_command`関数では、例外処理を行いエラーメッセージを返します。
- `fzf`でのコマンド選択がキャンセルされた場合、適切なメッセージを表示します。

## 環境変数の設定
`.env`ファイルにOpenAI APIキーを設定します。以下の形式でキーを入力してください。
```plaintext
OPENAI_API_KEY=your_api_key_here

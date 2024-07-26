import openai
import sys
import os
import subprocess
from dotenv import load_dotenv
from prompt import get_prompt

# 環境変数をロード
load_dotenv()

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            timeout=30
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: gpt <query>")
        sys.exit(1)

    task = " ".join(sys.argv[1:])
    current_status = "現在の環境情報を読み込む"  # 環境情報をここで追加

    # 環境情報を取得して読み込む
    with open("environment_info.txt", "r") as f:
        current_status = f.read()

    prompt = get_prompt(task, current_status)
    response = get_gpt_response(prompt)
    
    print(f"{response}")

    if "解決のステップ" not in response:
        sys.exit(1)

    # 提案されたコマンドを選択肢としてfzfで表示
    commands = [line for line in response.split('\n') if line.strip() and not line.startswith('#')]
    if not commands:
        print("使用するべきコマンドが見つかりませんでした。")
        sys.exit(1)

    selected_command = subprocess.run('fzf', input="\n".join(commands), text=True, shell=True, capture_output=True).stdout.strip()

    if selected_command:
        confirm = input(f"実行しますか?(YES / no)(Enterにより、Yes): ")
        if confirm.lower() in ["yes", "y", ""]:
            print(f"実行中: {selected_command}")
            result = execute_command(selected_command)
            print(result)
        else:
            print("コマンドの実行がキャンセルされました。")
    else:
        print("コマンドが選択されませんでした。")

if __name__ == "__main__":
    main()

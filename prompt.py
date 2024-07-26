# prompt.py

def get_prompt(task, current_status):
    prompt = f"""
    # [現在の状況] : {current_status}
    # [最終ゴール] : {task}
    ## 条件 :
    - "```", "`"は絶対に出力しないで。
    - markdown形式の出力ではなく、txt形式の出力として。
    - Debian based Linuxを使用している。
    - '-y'を適宜使用して。

    # [出力] :
    - 使用コマンドのみを教えて。その他はなにも出力しないで。
    """
    return prompt
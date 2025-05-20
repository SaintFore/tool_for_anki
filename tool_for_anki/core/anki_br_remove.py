"""
移除掉使用AI制作卡片时的分隔符
以及将四个下划线替换为三个下划线，防止Markdown识别错误
"""

from pathlib import Path


def br_remove(file_path):
    """
    移除 Anki ID，返回新文件路径

    Args:
        file_path: 文件路径

    Returns:
        文件路径或None(处理失败时)
    """
    try:
        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        handled_lines = []

        for line in lines:
            if line.strip() == "---":
                handled_lines.append("\n")
            elif line.strip() == "":
                continue
            else:
                if "____" in line:
                    line = line.replace("____", "___")
                handled_lines.append(line.strip())

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(handled_lines))
        return path
    except Exception as e:
        print(f"处理文件{file_path}时出错: {e}")
        return None

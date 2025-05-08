from anki_tools import remove_anki_id_and_normalize
from pathlib import Path


def add_tag(file_path, tag):
    """
    添加标签到文件中

    Args:
        file_path: 文件路径
        tag: 要添加的标签

    Returns:
        新文件路径或None(处理失败时)
    """

    path = remove_anki_id_and_normalize(file_path)
    print(path)
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    sign = 0
    handle = []

    for line in lines:
        if line.strip() == "":
            sign += 1
            handle.append(line)
        elif sign == 2 and line.strip() != "":
            line = line.strip() + f" #{tag}\n"
            sign = 0
            handle.append(line)
        else:
            sign = 0
            handle.append(line)

    # new_path = path.with_stem(f"{path.stem}_tagged")
    # with open(new_path, "w", encoding="utf-8") as file:
    #     file.writelines(handle)
    # return new_path

    # 直接覆盖原文件
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(handle)
    return path

"""
Anki笔记处理工具

用于管理和处理Anki笔记文件的工具集。
"""

__version__ = "0.3.0"

# 导出核心函数，便于直接从包导入
from tool_for_anki.core.anki_tools import remove_anki_id_and_normalize
from tool_for_anki.core.add_tag import add_tag

__all__ = ["remove_anki_id_and_normalize", "add_tag"]
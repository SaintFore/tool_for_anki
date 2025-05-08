"""
应用入口点
"""

from tool_for_anki import __version__
from tool_for_anki.gui import run

print(f"Anki笔记处理工具 v{__version__}")

if __name__ == "__main__":
    run()
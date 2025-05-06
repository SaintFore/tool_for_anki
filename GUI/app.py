import customtkinter
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path
from anki_tools import remove_anki_id_and_normalize

class App(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)  # 初始化DnD功能
        
        self.title("Anki 笔记处理工具")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # 创建标签提示用户
        self.label = customtkinter.CTkLabel(self, text="将文件拖放到下方区域")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        
        # 创建文本框作为拖放区域
        self.drop_area = customtkinter.CTkTextbox(self, height=200)
        self.drop_area.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.drop_area.insert("1.0", "拖放文件到这里...")
        
        # 配置拖放功能
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.drop_callback)
        
        # 显示已选文件的路径
        self.path_label = customtkinter.CTkLabel(self, text="文件路径将显示在这里")
        self.path_label.grid(row=2, column=0, padx=20, pady=10)
        
        # 处理按钮
        self.process_button = customtkinter.CTkButton(self, text="处理文件", command=self.process_files)
        self.process_button.grid(row=3, column=0, padx=20, pady=20)
        
        # 用于存储拖放的文件路径
        self.file_paths = []
        
    def drop_callback(self, event):
        """处理文件拖放事件"""
        # 清空之前的内容
        self.drop_area.delete("1.0", "end")
        
        # 获取文件路径（处理tkinterdnd2返回的字符串格式）
        file_paths = event.data
        # print(f"拖放的文件路径: {file_paths}")
        
        # 处理可能的多个文件
        self.file_paths = file_paths.split(" ") if " " in file_paths else [file_paths]
        
        # 显示拖放的文件
        for path in self.file_paths:
            self.drop_area.insert("end", f"{Path(path).stem}\n")
        
        # 更新路径标签
        if len(self.file_paths) == 1:
            self.path_label.configure(text=f"文件路径: {self.file_paths[0]}")
        else:
            self.path_label.configure(text=f"已选择 {len(self.file_paths)} 个文件")
    
    def process_files(self):
        """处理选中的文件"""
        if not self.file_paths:
            self.path_label.configure(text="请先拖放文件!")
            return
        
        # 这里可以添加你的文件处理逻辑
        print("处理以下文件:")
        for path in self.file_paths:
            # print(path)
            remove_anki_id_and_normalize(path)  # 调用处理函数
        
        # 更新UI
        self.path_label.configure(text=f"已处理 {len(self.file_paths)} 个文件")

def run():
    """运行应用程序"""
    app = App()
    app.mainloop()
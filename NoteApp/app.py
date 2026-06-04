import customtkinter as ctk
import json
import os

import sys

# 基础配置
def get_data_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(os.path.dirname(sys.executable), "data.json")
    else:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

DATA_FILE = get_data_path()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class MemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("现代备忘录")
        # 强制设置初始几何尺寸，增大窗口
        self.geometry("500x600")
        self.update_idletasks() # 强制刷新窗口属性

        # 窗口居中计算逻辑
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 500
        height = 600
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
        # 工业风：设置 80% 透明度
        self.attributes('-alpha', 0.85)

        # 全局字体定义
        self.main_font = ("Segoe UI", 13)

        # 顶部布局 - 使用 CTkTextbox 支持多行输入
        self.entry = ctk.CTkTextbox(self, height=200, font=("Segoe UI", 16), corner_radius=10)
        self.entry.pack(pady=20, padx=20, fill="x")

        self.add_button = ctk.CTkButton(self, text="添加", command=self.add_item, font=self.main_font, height=35, corner_radius=10)
        self.add_button.pack(pady=5, padx=20, fill="x")

        # 任务列表容器 - 设置圆角增加工业感
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="待办事项", corner_radius=15, fg_color="#202020")
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.items = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.items = json.load(f)
                for item in self.items:
                    self.create_item_ui(item)

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False)

    def add_item(self):
        text = self.entry.get("1.0", "end-1c").strip()
        if text:
            self.items.insert(0, text)
            # 重新渲染列表以确保顺序
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            for item in self.items:
                self.create_item_ui(item)
            self.save_data()
            self.entry.delete("1.0", "end")

    def create_item_ui(self, text, prepend=False):
        # 创建条目容器 - 工业风配色
        frame = ctk.CTkFrame(self.scrollable_frame, fg_color="#303030", corner_radius=8)
        if prepend:
            frame.pack(fill="x", pady=5, padx=5, side="top")
        else:
            frame.pack(fill="x", pady=5, padx=5)

        label = ctk.CTkLabel(frame, text=text, anchor="w", font=self.main_font)
        label.pack(side="left", padx=10, fill="x", expand=True)

        btn = ctk.CTkButton(frame, text="删除", width=60, fg_color="#8B0000", hover_color="#A52A2A",
                            bg_color="transparent", command=lambda: self.delete_item(frame, text))
        btn.pack(side="right", padx=5, pady=5)

    def delete_item(self, frame, text):
        frame.destroy()
        self.items.remove(text)
        self.save_data()

if __name__ == "__main__":
    app = MemoApp()
    app.mainloop()
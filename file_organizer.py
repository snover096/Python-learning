import os
import shutil
import sys

# 定义文件类型与文件夹的对应关系
# 你可以根据实际需求在这里添加或修改后缀名
FILE_TYPES = {
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
    '视频': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    '音频': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    '文档': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md'],
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '安装包': ['.exe', '.msi'],
}

def organize_files():
    """
    根据文件后缀名整理当前目录下的文件
    """
    # 获取程序当前运行的目录
    # 注意：如果是打包成EXE，os.getcwd() 返回的是EXE所在的文件夹
    current_dir = os.getcwd()
    
    # 获取当前执行文件的名称（包括脚本名或打包后的EXE名）
    # 这样做是为了防止程序把“自己”也移动到安装包文件夹里
    current_exe_or_script = os.path.basename(sys.argv[0])

    print(f"--- 开始整理目录: {current_dir} ---")

    # 计数器，用于统计整理了多少文件
    count = 0

    # 遍历当前目录下的所有内容
    for filename in os.listdir(current_dir):
        # 构造文件的完整路径
        file_path = os.path.join(current_dir, filename)

        # 过滤条件：
        # 1. 跳过文件夹（我们只整理文件）
        # 2. 跳过程序本身（防止移动正在运行的程序）
        if os.path.isdir(file_path) or filename == current_exe_or_script:
            continue

        # 获取文件的后缀名，并统一转为小写
        file_ext = os.path.splitext(filename)[1].lower()

        # 确定目标文件夹名称
        target_folder = '其他'  # 默认分类
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                target_folder = folder_name
                break
        
        # 构造目标目录的完整路径
        target_dir = os.path.join(current_dir, target_folder)
        
        # 如果对应的分类文件夹不存在，则自动创建
        if not os.path.exists(target_dir):
            try:
                os.makedirs(target_dir)
                print(f"创建文件夹: {target_folder}")
            except Exception as e:
                print(f"创建文件夹失败: {e}")
                continue

        # 执行移动操作
        try:
            target_path = os.path.join(target_dir, filename)
            
            # 检查目标文件夹内是否已存在同名文件
            if os.path.exists(target_path):
                print(f"[跳过] {filename} 已存在于 {target_folder} 文件夹中")
            else:
                shutil.move(file_path, target_path)
                print(f"[成功] 移动 {filename} -> {target_folder}/")
                count += 1
        except Exception as e:
            print(f"[错误] 移动文件 {filename} 时发生异常: {e}")

    print(f"\n整理任务结束！共处理了 {count} 个文件。")

if __name__ == "__main__":
    # 执行主函数
    organize_files()
    # 保持窗口开启，方便查看结果（打包为EXE后非常有用）
    input("\n按下回车键退出程序...")

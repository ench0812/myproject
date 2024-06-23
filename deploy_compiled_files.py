import os
import shutil

# 確定 dist 目錄存在
dist_dir = "dist"
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
os.makedirs(dist_dir)

# copy 需要的原始檔案
original_files = ["main.py", "requirements.txt"]

for file in original_files:
    shutil.copy(file, os.path.join(dist_dir))

# 遍歷指定目錄下的所有子目錄和檔案
project_paths = ["src"]

for directory in project_paths:
    for root, dirs, files in os.walk(directory):
        # 對於每個檔案，如果是 .pyd 檔案，則複製到 dist/ 目錄中
        for file in files:
            if file.endswith(".pyd") or file.endswith(".so"):
                # 獲取相對於 src/ 目錄的路徑
                relative_path = os.path.relpath(root, directory)
                # 目標複製路徑
                target_dir = os.path.join(dist_dir, directory, relative_path)
                # 如果目標目錄不存在，則創建
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                # 複製檔案
                shutil.move(os.path.join(root, file), target_dir)

            if file.endswith(".c"):
                os.remove(os.path.join(root, file))

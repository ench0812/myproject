import os

from Cython.Build import cythonize
from setuptools import setup, Extension

# 設定專案路徑
project_paths = ['src']

# 收集所有需要編譯的 Python 文件
py_files = []
for directory in project_paths:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

# 編譯設定
extensions = [
    Extension(
        os.path.splitext(file.replace(os.sep, '.'))[0],
        [file],
        # extra_compile_args=[
        #     "-march=armv8-a",  # 指定 ARM 架構
        #     "-mtune=cortex-a57",  # 針對 Jetson Nano 的 CPU 核心
        #     "-O3",  # 啟用最高級別優化
        #     "-ftree-vectorize",  # 啟用向量化
        #     "-ffast-math",  # 快速數學運算優化
        #     "-funsafe-math-optimizations",  # 不安全的數學運算優化
        #     "-fopenmp"  # 啟用 OpenMP 支持
        # ],
        extra_compile_args=[
            "-march=native",  # 指定 x86 架構
            "-O3",  # 啟用最高級別優化
            "-ftree-vectorize",  # 啟用向量化
            "-ffast-math",  # 快速數學運算優化
            "-funsafe-math-optimizations",  # 不安全的數學運算優化
            "-fopenmp"  # 啟用 OpenMP 支持
        ],
        extra_link_args=[
            "-fopenmp"  # 連接時啟用 OpenMP 支持
        ]
    ) for file in py_files
]

setup(
    name='meter-collect',
    ext_modules=cythonize(extensions, compiler_directives={
        'language_level': "3",
        'embedsignature': True,
        'cdivision': True,
    }),
    zip_safe=False,
)

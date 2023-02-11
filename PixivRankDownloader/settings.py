import os

COOKIE_FILE = os.environ['COOKIE']

# 下载线程数
DOWNLOAD_THREADS = 4

# 每秒最大下载文件数。大于0时启用该设置。
DOWNLOAD_SPEED = 0.5

# 代理信息
PROXY_HOST = ""
PROXY_PORT = ""
USE_PROXY = False

# 下载计数。最大不超过150
QUANTITY = 150

# 下载路径
IMAGE_PATH = "./114514"

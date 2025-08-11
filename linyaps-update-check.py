#!/bin/env python3
import os
import sys
import argparse
import requests
import json

# 脚本返回说明:
# 0:是最新版本,1:不是最新版本,2:网络炸了,4:我也不知道什么问题


# 创建参数解析器
parser = argparse.ArgumentParser(description="读取linyaps版本号参数")
# 添加--linyaps参数（支持--linyaps=xxx格式）
parser.add_argument(
    '--linyaps',  # 参数名
    type=str,      # 参数类型（字符串）
    required=True, # 是否必填（若不填则运行时报错）
    help='指定linyaps的版本号，格式如--linyaps=1.9.9-1'
)
# 解析命令行参数
args = parser.parse_args()

# 提取并使用版本号
linyaps_cur_version = args.linyaps

def err_fatal ():sys.exit(4)      # 其他未知异常返回4
def err_network (): sys.exit(2)    # 网络问题则返回2
def is_old (): sys.exit(1)    # 老版本返回1
def is_newest (): sys.exit(0)      # 不需要更新返回0

# 从Gitee仓库获取最新的稳定版本
def get_latest_tag ():
    # Gitee API地址：获取最新release信息
    url = "https://gitee.com/api/v5/repos/LFRon/Linyaps-generic-linux-SIG/releases/latest"
    try:
        response = requests.get(url)
        release_info = json.loads(response.text)
        # 提取tag_name字段
        tag_name = release_info.get("tag_name")
        return tag_name
    # 对于异常处理
    except requests.exceptions.RequestException as e: err_network()
    except Exception as e: err_fatal()




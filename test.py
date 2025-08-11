#!/bin/env python3
import os
import subprocess
import sys

# 说明:脚本错误返回情况
# 异常情况:4,安装失败:3,网络异常:2,不支持当前发行版:1

# 建议将此脚本直接用root权限跑

# 进行意外的异常处理
def fatal_error ():
    sys.exit(4)

# 进行意外的安装失败异常处理
def fatal_error_installation ():
    sys.exit(3)

# 下载网络异常处理
def err_network ():
    sys.exit(2)

# 不支持当前发行版处理
def err_distro_not_supported ():
    sys.exit(1)

# 初始化变量设置
distro_output = subprocess.getstatusoutput('cat /etc/os-release')   # 通过os-release获取发行版详情信息
distro_name = ""       # 用于存储发行版名称
distro_version = ""       # 用于存储发行版代号
# 获取当前操作系统架构
distro_arch = subprocess.getstatusoutput('uname -m')[1]   # 直接通过uname -m的输出获取当前系统架构

# 初始化下载链接变量
download_url = ""

# 获取操作系统发行版名称
for line in distro_output[1].splitlines():
    # 捕获发行版名称
    if line.startswith('ID='): distro_name = line.split('=',1)[1].strip('"')
    # 捕获发行版版本号
    if line.startswith('VERSION_ID='): distro_version = line.split('=', 1)[1].strip('"')

print('- 你的发行版是:'+distro_name)
print('- 你的发行版版本号是:'+distro_version)

#!/bin/env python3
import os
import subprocess
import sys

# 进行意外的异常处理
def fatal_error ():
    sys.exit(3)

# 下载网络异常处理
def err_network ():
    sys.exit(2)

# 不支持当前发行版处理
def err_distro_not_supported ():
    sys.exit(1)

# 初始化变量设置
distro_output = subprocess.getstatusoutput('cat /etc/os-release')   # 通过os-release获取发行版详情信息
distro_name = ""     # 用于存储发行版名称
distro_codename = ""     # 用于存储发行版代号
# 获取当前操作系统架构    
distro_arch = subprocess.getstatusoutput('uname -m')[1]   # 直接通过uname -m的输出获取当前系统架构
# 初始化下载链接变量
download_url = ""

# 获取操作系统发行版名称
for line in distro_output[1]:
    # 捕获发行版名称
    if line.startwith('ID='): distro_name = line.split('=',1)[1]
    else if line.startswith('VERSION_CODENAME='): distro_codename = line.split('=', 1)[1]

# 遇到ArchLinux这类玲珑已经在软件源里的直接跳过
if (distro_name=='arch') sys.exit(0)    

# 进行下载链接处理
download_url = f'https://gitee.com/LFRon/Linyaps-generic-linux-SIG/releases/download/latest/{distro_name}-{distro_codename}-{distro_arch}.tar.gz'

if (os.system(f'wget {download_url}') == 1024): err_network()     # 没网返回2
else if (os.system(f'wget {download_url}') == 2048): err_distro_not_supported()     # 发行版不支持返回1

if (os.system('mkdir -p /tmp/linyaps-installer')!=0): fatal_error()


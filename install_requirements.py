#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动查找子文件夹中的requirements.txt文件并执行安装
"""

import os
import subprocess
import sys
from pathlib import Path

def find_and_install_requirements():
    """
    查找当前目录下一层子文件夹中的requirements.txt文件并执行pip install
    """
    current_dir = Path.cwd()
    print(f"📁 正在扫描目录: {current_dir}")
    print()
    
    # 查找所有子文件夹
    subdirs = [d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    if not subdirs:
        print("❌ 未找到任何子文件夹")
        return
    
    print(f"🔍 发现 {len(subdirs)} 个子文件夹，正在查找requirements.txt...")
    found_requirements = []
    
    # 在每个子文件夹中查找requirements.txt
    for subdir in subdirs:
        requirements_file = subdir / 'requirements.txt'
        if requirements_file.exists():
            found_requirements.append(requirements_file)
            print(f"  ✅ {subdir.name}/requirements.txt")
        else:
            print(f"  ⚪ {subdir.name}/ (无requirements.txt)")
    
    print()
    
    if not found_requirements:
        print("❌ 未找到任何requirements.txt文件")
        return
    
    print(f"📦 找到 {len(found_requirements)} 个requirements.txt文件，开始安装依赖...")
    print("=" * 60)
    
    # 为每个找到的requirements.txt执行安装
    success_count = 0
    for i, req_file in enumerate(found_requirements, 1):
        folder_name = req_file.parent.name
        print(f"\n[{i}/{len(found_requirements)}] 📋 处理 {folder_name}/requirements.txt")
        print("-" * 40)
        
        try:
            # 使用pip install -r安装依赖
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '-r', str(req_file)],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ 成功安装 {folder_name} 项目的依赖")
            success_count += 1
            
            # 只显示重要的输出信息
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                installed_packages = [line for line in lines if 'Successfully installed' in line]
                if installed_packages:
                    print(f"📦 {installed_packages[0]}")
                    
        except subprocess.CalledProcessError as e:
            print(f"❌ 安装 {folder_name} 项目依赖失败")
            if e.stderr:
                # 只显示关键错误信息
                error_lines = e.stderr.strip().split('\n')
                key_errors = [line for line in error_lines if any(keyword in line.lower() for keyword in ['error', 'failed', 'could not'])]
                if key_errors:
                    print(f"💥 错误: {key_errors[-1]}")
                else:
                    print(f"💥 错误: {e.stderr.strip()}")
        except Exception as e:
            print(f"❌ 安装 {folder_name} 项目时发生未知错误")
            print(f"💥 错误: {str(e)}")
    
    print("\n" + "=" * 60)
    print(f"📊 安装完成: {success_count}/{len(found_requirements)} 个项目成功安装依赖")

def main():
    """
    主函数
    """
    print("\n" + "=" * 60)
    print("🚀 自动安装requirements.txt依赖工具")
    print("=" * 60)
    print()
    
    try:
        find_and_install_requirements()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断操作")
        print("👋 程序已退出")
        return
    except Exception as e:
        print(f"\n💥 程序执行出错: {e}")
        return
    
    print("\n🎉 程序执行完成！")

if __name__ == '__main__':
    main()
# Miscellaneous Projects

这是一个存放各种杂项项目的仓库，包含了一些独立的小工具和实验性项目。

## 🛠️ 工具

### install_requirements.py

一个自动化工具，用于批量安装子项目的Python依赖。

**功能特性：**
- 🔍 自动扫描所有子文件夹
- 📦 查找并识别 `requirements.txt` 文件
- ⚡ 批量执行 `pip install -r requirements.txt`
- 📊 提供详细的安装进度和结果统计
- 🎨 美观的命令行界面输出
- ❌ 智能错误处理和友好的错误提示

**使用方法：**
```bash
python install_requirements.py
```

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 🚀 快速开始

1. 克隆仓库到本地
2. 运行 `python install_requirements.py` 安装所有子项目的依赖
3. 探索各个子项目文件夹中的内容

## 📁 项目结构

```
miscellaneous-projects/
├── install_requirements.py    # 依赖安装工具
├── LICENSE                    # MIT许可证
├── README.md                  # 项目说明文档
└── [各种子项目文件夹]/         # 独立的项目目录
```

---

> 💡 **提示**: 每个子项目都是独立的，可以单独运行和使用。使用 `install_requirements.py` 可以快速为所有项目安装依赖。
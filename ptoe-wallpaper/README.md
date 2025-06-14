# PTOEWallpaper - 元素周期表壁纸生成器

一个用于生成美观的元素周期表壁纸的Python项目。该项目可以创建高分辨率的元素周期表图像，包含中英文元素名称、原子序数、化学符号和原子质量等信息。

## 功能特性

- 🎨 生成高分辨率（7680x4320）元素周期表壁纸
- 🌈 根据元素类型使用不同颜色标识（碱金属、碱土金属、过渡金属等）
- 🔤 支持中英文双语显示
- 📊 包含完整的元素信息：原子序数、化学符号、中英文名称、原子质量
- 🎯 精确的元素位置布局
- 📱 适用于各种屏幕尺寸的壁纸

## 项目结构

```
PTOEWallpaper/
├── data/                   # 元素数据文件
│   ├── atomic-mass.json   # 原子质量数据
│   ├── attribute.json     # 元素属性分类
│   ├── color.json         # 颜色配置
│   ├── name.json          # 元素名称
│   ├── position.json      # 元素位置坐标
│   └── symbol.json        # 化学符号
├── fonts/                 # 字体文件
│   └── arialbd.ttf       # Arial Bold字体
├── main.py               # Manim动画版本
├── ptoe.py               # PIL静态图像生成
├── requirements.txt      # 项目依赖
└── README.md            # 项目说明文档
```

## 安装和使用

### 环境要求

- Python 3.6+
- PIL (Pillow)

### 安装依赖

```bash
pip install -r requirements.txt
```

### 生成壁纸

运行以下命令生成元素周期表壁纸：

```bash
python ptoe.py
```

生成的图像将保存为 `image.png`。

### 动画版本

项目还包含一个使用Manim制作的动画版本：

```bash
# 需要先安装manim
pip install manimgl

# 运行动画
manimgl main.py ptoe -c #101318
```

## 元素分类和颜色

项目使用不同颜色来区分元素类型：

- 🟡 **碱金属** (Alkali Metal) - #ecbe59
- 🟢 **碱土金属** (Alkaline Earth Metal) - #dee955  
- 🔴 **过渡金属** (Transition Metal) - #fd8572
- 🔵 **后过渡金属** (Post-transition Metal) - #4cddf3
- 🟣 **镧系元素** (Lanthanoid) - #ec77a3
- 🟪 **锕系元素** (Actinoid) - #c686cc
- 🟢 **类金属** (Metalloid) - #3aefb6
- 🟢 **其他非金属** (Other Nonmetal) - #52ee61
- 🔵 **稀有气体** (Noble Gas) - #759fff
- ⚪ **未知元素** (Unknown) - #cccccc

## 许可证

本项目采用 **MIT 许可证** 进行授权。

### MIT 许可证说明

MIT 许可证是一个宽松的开源许可证，允许您：

✅ **商业使用** - 可以在商业项目中使用此代码  
✅ **修改** - 可以修改源代码  
✅ **分发** - 可以分发原始代码或修改后的代码  
✅ **私人使用** - 可以私人使用此代码  
✅ **专利使用** - 获得专利使用权  

### 许可证要求

在使用本项目时，您需要：

📋 **包含许可证** - 在所有副本中包含原始许可证和版权声明  
📋 **包含版权声明** - 保留原作者的版权信息  

### 免责声明

⚠️ 本软件按"原样"提供，不提供任何明示或暗示的保证  
⚠️ 作者不承担任何使用本软件造成的损害责任  

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 作者

**Jack Peng** - 项目创建者和维护者

---

如果这个项目对您有帮助，请给它一个 ⭐ Star！
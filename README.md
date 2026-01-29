# 🚀 Space Shooter - 太空射击游戏

一个功能完整的 Python 太空射击游戏，使用 Pygame 开发。

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 游戏特色

### 核心功能
- ✅ **流畅的游戏体验** - 60 FPS 流畅运行
- ✅ **多种敌机类型** - 基础型、快速型、坦克型
- ✅ **武器升级系统** - 三级武器火力
- ✅ **道具系统** - 生命恢复、武器升级、额外分数
- ✅ **关卡进度** - 难度递增，无限关卡
- ✅ **视觉效果** - 爆炸特效、星空背景
- ✅ **高分记录** - 本地最高分保存

### 游戏玩法

#### 🎯 游戏目标
控制你的飞船，击败来袭的敌机，获得最高分！

#### 🕹️ 操作说明
- **← →** 或 **A D** - 左右移动飞船
- **SPACE** - 发射子弹 / 开始游戏
- **P** - 暂停/继续游戏
- **ESC** - 返回菜单
- **Q** - 退出游戏（菜单界面）

#### 💪 道具系统
- **🟢 + (绿色)** - 恢复 20 点生命值
- **🟣 P (紫色)** - 武器升级（最高3级）
- **🟡 $ (黄色)** - 获得 50 分

#### 👾 敌机类型
- **🔴 红色战机** - 普通敌机，速度中等，10分
- **🟣 紫色战机** - 快速敌机，移动迅速，15分
- **🟠 橙色战机** - 坦克敌机，血量厚，25分

## 📦 安装说明

### 环境要求
- Python 3.7 或更高版本
- Pygame 2.0 或更高版本

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/yourusername/space-shooter.git
cd space-shooter
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

或者手动安装 Pygame：
```bash
pip install pygame
```

3. **运行游戏**
```bash
python main.py
```

## 🎯 游戏技巧

1. **优先攻击坦克型敌机** - 它们分数高但移动慢
2. **收集武器道具** - 三级火力可以快速清屏
3. **保持移动** - 不要停在一个位置
4. **关注血量** - 及时收集生命道具
5. **提升等级** - 分数越高，敌机越强，但得分也越高

## 📊 游戏机制

### 难度系统
- 每 500 分升一级
- 等级越高，敌机越快
- 敌机生成频率随等级提升

### 武器系统
- **1级** - 单发子弹
- **2级** - 双发子弹（左右两侧）
- **3级** - 三发子弹（中间+两侧）

### 生命系统
- 初始生命值：100
- 被敌机撞击：-20 生命
- 受伤后短暂无敌（2秒）

## 🛠️ 开发说明

### 项目结构
```
space_shooter/
├── main.py           # 主游戏文件
├── README.md         # 项目说明
├── requirements.txt  # 依赖列表
└── highscore.txt     # 高分记录（自动生成）
```

### 代码特点
- **面向对象设计** - 清晰的类结构
- **模块化架构** - 易于扩展和修改
- **注释完整** - 中文注释便于理解
- **性能优化** - 精灵渲染，60 FPS

## 🎨 自定义修改

### 修改游戏难度
在 `main.py` 中找到：
```python
self.speed = 6  # 玩家速度
self.enemy_spawn_delay = 60  # 敌机生成延迟
```

### 修改颜色
在 `main.py` 顶部的颜色定义：
```python
BLUE = (50, 150, 255)  # 玩家颜色
RED = (255, 50, 50)    # 敌机颜色
```

### 添加新敌机类型
在 `Enemy` 类中添加新的 `self.type` 类型。

## 🐛 已知问题
- 无

## 📝 更新日志

### v1.0.0 (2026-01-29)
- ✨ 初始版本发布
- 🎮 核心游戏功能
- 🎨 完整的视觉效果
- 📊 高分记录系统

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 👨‍💻 作者

**开发：** Clawdbot AI Assistant  
**技术栈：** Python + Pygame

## 🙏 致谢

- Pygame 开发团队
- 所有开源贡献者

---

**享受游戏！🎮✨**

如果喜欢这个项目，请给个 ⭐️ Star！

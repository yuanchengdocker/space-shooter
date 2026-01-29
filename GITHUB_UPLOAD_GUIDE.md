# 🚀 Space Shooter - GitHub 上传指南

## 📋 快速开始

### 方法一：使用 GitHub CLI（推荐 - 如果已安装）

```bash
# 1. 创建 GitHub 仓库
gh repo create space-shooter --public --source=. --remote=origin --push

# 完成！🎉
```

### 方法二：手动创建（通用方法）

#### Step 1: 在 GitHub 创建仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **仓库名称：** `space-shooter`
   - **描述：** `🚀 A complete space shooter game built with Python and Pygame`
   - **可见性：** ☑️ Public（公开）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**勾选 "Choose a license"

3. 点击 **"Create repository"** 按钮

#### Step 2: 推送代码到 GitHub

复制并运行以下命令（替换 `YOUR_USERNAME`）：

```bash
cd /Users/miniwan/clawd/space_shooter

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/space-shooter.git

# 推送代码到 GitHub
git branch -M main
git push -u origin main
```

## ✅ 验证上传成功

访问你的仓库链接：
```
https://github.com/YOUR_USERNAME/space-shooter
```

你应该看到：
- ✅ README.md 文件内容
- ✅ main.py 游戏代码
- ✅ requirements.txt 依赖文件

## 🎮 运行游戏

```bash
# 安装依赖
pip install -r requirements.txt

# 运行游戏
python main.py
```

## 📝 仓库信息

- **仓库名称：** space-shooter
- **描述：** A complete space shooter game built with Python and Pygame
- **标签：** python, pygame, game, space-shooter, arcade

## 🎨 添加 GitHub Topics（可选）

在仓库页面添加以下 Topics：
- `python`
- `pygame`
- `game`
- `space-shooter`
- `arcade`
- `shooter-game`

## 🚀 让游戏更出色

### 添加截图
在 `README.md` 中添加游戏截图：

```markdown
## 🎮 游戏截图

### 主菜单
![主菜单](screenshots/menu.png)

### 游戏画面
![游戏画面](screenshots/gameplay.png)

### 游戏结束
![游戏结束](screenshots/gameover.png)
```

### 添加 LICENSE
```bash
# 创建 MIT License
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
```

## 🎯 下一步

1. **测试游戏** - 确保游戏正常运行
2. **添加截图** - 展示游戏画面
3. **分享链接** - 告诉朋友们你的新游戏！
4. **继续改进** - 添加新功能、音效、更多关卡...

## 💡 提示

- 如果遇到推送问题，确保你已经 SSH 密钥添加到 GitHub
- 或者使用 HTTPS 方式推送（会要求输入 GitHub 用户名和密码）
- 记得替换 `YOUR_USERNAME` 为你的实际 GitHub 用户名

## 🐛 常见问题

### 问题 1: 推送时提示认证失败
**解决方案：**
```bash
# 使用 HTTPS 方式
git remote set-url origin https://github.com/YOUR_USERNAME/space-shooter.git
git push -u origin main
```

### 问题 2: 提示仓库不存在
**解决方案：**
- 确保先在 GitHub 网站上创建了仓库
- 检查仓库名称是否正确

### 问题 3: 推送后看不到 README
**解决方案：**
- 刷新 GitHub 页面
- 检查文件是否正确提交

---

**需要帮助？** 请查看 GitHub 官方文档：https://docs.github.com

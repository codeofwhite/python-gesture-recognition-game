# 手势飞机大战游戏 - gesture_recognition_game

基于计算机视觉手势识别的交互式飞机大战游戏，支持手势操控、账号登录、双模式闯关、飞船升级与背景音乐系统。

## 项目简介
这是一款使用摄像头手势控制的 Python 飞机大战游戏。玩家通过手势控制飞机移动、攻击、变身、躲避，包含休闲漫游模式与 BOSS 挑战模式，支持用户登录、分数存档、属性成长等完整功能。

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/66acbe12-eb7c-4ccf-a054-3464acc860a8" />

## 功能介绍
1. 手势控制
- 剪刀：飞机缩小，提高躲避
- 拳头 / 点赞：发射子弹 / 镭射攻击

2. 游戏模式
- 漫游模式：击碎陨石，获取道具（闪电、护盾、双倍分数等）
- 挑战模式：对战多主题 BOSS，支持 Hero / Queen 形态切换

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/d223b990-0859-48aa-a750-463cc43bd164" />

3. 用户系统
- 注册 / 登录
- 分数、战绩、游戏场次自动保存
- 个人信息主页

4. 成长系统
- 升级移动速度
- 升级生命值
- 升级生命数量
- 提升道具掉落概率

## 启动教程
1. 安装依赖
打开终端运行：

```bash
pip install -r requirements.txt
```

2. 项目里有 user_info.sql，需要手动创建数据库

3. 启动游戏
```bash
python game_main_system.py
```

## 项目结构
```plaintext
├── game_main_system.py    # 游戏主程序（启动入口）
├── chapter_2_sample.py    # 游戏示例/测试文件
├── user_info.sql          # MySQL 表结构
├── gesture/               # 手势识别模块
├── game/                  # 游戏逻辑
├── plane_sprite/          # 飞机精灵、动画
├── sounds/                # 音效、背景音乐
├── imgs/                  # 图片资源
├── Fonts/                 # 字体
├── config/                # 配置文件
├── tk_ui/                 # UI界面
```


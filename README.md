# Room Life Design · 房间生活感设计

把自己的卧室照片交给 AI，生成温馨、明亮暖光、有生活气息的房间改造效果图。

这是一个可安装的 Agent Skill，不是独立生图软件。它把空间布局、生活感、四层灯光和参考图选择方法交给你自己的 AI 执行。当前发布版本：**v1.12.0**。

## 两步开始

### 1. 安装 Skill

如果你使用 Codex，把下面整段话发给它：

```text
请使用 $skill-installer，从下面的 GitHub 目录安装 room-life-design：
https://github.com/mu-xiaoyuan/room-life-design/tree/main/skills/room-life-design
请安装完整目录，包括 references、assets、agents 和 scripts，不要只下载 SKILL.md。
安装完成后告诉我是否成功。
```

安装参数供 AI 定位内置安装脚本后使用：

```text
--repo mu-xiaoyuan/room-life-design --path skills/room-life-design
```

安装后在新的对话或下一轮中使用；如果技能列表没有刷新，重启客户端。上述安装方式参考 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。不同版本的安装位置由工具自行管理，不要复制作者电脑的路径。

其他支持 Agent Skills 的工具：使用该工具的导入方式，安装仓库中的整个 `skills/room-life-design` 文件夹。不同工具的安装方法不完全相同，本仓库不承诺所有 AI 聊天窗口都能通过链接直接安装。

也可以[下载仓库 ZIP](https://github.com/mu-xiaoyuan/room-life-design/archive/refs/heads/main.zip)，解压后导入 `skills/room-life-design` 文件夹，而不是把整个仓库当作一个 Skill。

### 2. 上传房间照片

在启用这个 Skill 的改造对话中上传照片即可；如果 AI 没有自动调用，补充：

```text
使用 room-life-design 改造这间卧室，直接生成效果图，功能分区由你决定。
```

默认由 AI 分析房间、决定合适的分区和风格、选择参考图、生成并检查结果，不要求你测量房间。你也可以随照片写「需要办公区和休闲区」「保留这张床」「不要植物」等偏好。只有关键画面信息缺失或要求相互冲突时才需要补问。

想自己选分区，可以说「先让我选择功能区」；只想听分析，可以说「先分析，不要生成」。

## AI 内部怎么工作

1. 读取入口和本次任务需要的规则，分析用户照片中的房间结构、现有家具和大致容量。
2. 保留固定建筑结构，比较床的位置与朝向，安排真正能使用的功能区。
3. 先看文字索引，通常只打开 **1～2 张**匹配的参考图；参考库增大不代表每次要重看整个图库。
4. 用户照片是唯一改造对象，参考图只提供生活感、灯光、材质和层次，不移植参考房间的建筑结构。
5. 调用用户 AI 的图片编辑工具，检查效果并交付图片。没有生图工具时必须说明限制，不能声称已经生成。

默认审美：有物品积累和使用痕迹的个人空间，明亮而柔和的暖光，松弛且有层次，避免过度整洁的样板间。空间估计不是测量结果，效果图不是施工图。

## 文件内容

- `skills/room-life-design/SKILL.md`：入口与关键约束。
- `references/`：布局、灯光、生活感、交互、案例结论和参考图索引。
- `assets/`：14 张风格参考图和 1 张案例原始图。
- `agents/openai.yaml`：Codex 显示名称和默认提示。
- `scripts/build_case_contact_sheets.py`：维护者分析新增案例时可用的联系表工具；日常改造不需要运行。

普通图片生成不依赖 Python。可选案例工具需要 Python 3.10+ 和 Pillow，处理 HEIF/HEIC 时另需 pillow-heif。

## 更新与反馈

`main` 提供最新版本；需要固定版本时，安装参数增加 `--ref v1.12.0`。已安装副本不会因为本仓库更新就必然自动更新，应使用 AI 工具自己的更新方式；不要直接覆盖个人修改。

欢迎通过 [Issues](https://github.com/mu-xiaoyuan/room-life-design/issues)反馈安装问题、布局不合理或效果不符合预期的情况。分享房间图片前请自行去除不想公开的个人信息。

## 素材说明

参考图片来自维护者提供的博主案例，不宣称由本项目原创，也不因本仓库公开而授予这些图片的再分发或商用权。请查看 [素材说明](NOTICE.md)。目前没有为全部内容统一指定开源许可证。

本项目不是 OpenAI 官方插件；安装 Skill 不包含模型、账号、生图额度或 API 密钥。同一 Skill 在不同模型上的效果可能不同。

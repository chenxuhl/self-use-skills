# Claude Code 开发技能集合

> 精选的 Claude Code 常用开发技能集合。

[**English**](./README.md)

---

## 快速开始

### Windows

```powershell
# 以管理员权限运行 PowerShell
.\scripts\install.ps1
```

### macOS/Linux

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

## 安装方式

### 方式一：使用安装脚本（推荐）

项目提供了自动安装脚本，会自动检测并创建符号链接、junction 或目录复制。

### 方式二：符号链接

在 Claude Code 配置目录中创建符号链接，指向本项目的 `skills` 目录：

```powershell
# Windows (PowerShell - 需要管理员权限)
# 将下面的路径替换为实际的项目路径
$projectPath = "C:\path\to\self-use-skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills" -Target "$projectPath\skills"
```

```bash
# macOS/Linux
# 将下面的路径替换为实际的项目路径
PROJECT_PATH="/path/to/self-use-skills"
ln -s "$PROJECT_PATH/skills" ~/.claude/skills
```

### 方式三：配置文件设置

在 `~/.claude/settings.json` (Windows 为 `%USERPROFILE%\.claude\settings.json`) 中添加：

```json
{
  "skillsPath": "C:\\path\\to\\self-use-skills\\skills"
}
```

> **注意**：Windows 路径需要使用双反斜杠 `\\`

## 卸载

### Windows

```powershell
.\scripts\uninstall.ps1
```

### macOS/Linux

```bash
./scripts/uninstall.sh
```

## 项目结构

```
self-use-skills/
├── skills/                    # 技能目录
│   └── skill-name/            # 单个技能
│       └── skill.md           # 技能配置文件
├── scripts/                   # 项目管理脚本
│   ├── install.ps1            # Windows 安装脚本
│   ├── install.sh             # macOS/Linux 安装脚本
│   ├── uninstall.ps1          # Windows 卸载脚本
│   ├── uninstall.sh           # macOS/Linux 卸载脚本
│   ├── setup-skills.py        # 技能配置生成脚本
│   └── download-skill.py      # 从官方仓库下载完整技能
├── .gitignore
├── package.json
└── README.md
```

## 下载完整技能内容

默认情况下，每个技能只包含基础配置（`skill.md`）。要获取完整的技能内容（包括参考文档和脚本），使用以下命令：

```bash
# 下载单个技能
python scripts/download-skill.py skill-creator

# 下载所有技能
python scripts/download-skill.py all

# 列出所有可下载的技能
python scripts/download-skill.py --list

# 强制覆盖已存在的技能内容
python scripts/download-skill.py skill-creator --force
```

## 包含的技能

| 技能名称 | 作用 | 地址 |
|---------|------|------|
| artifacts-builder | 利用现代前端 Web 技术构建复杂多组件 HTML 资产 | [链接](https://github.com/anthropics/skills) |
| aws-skills | AWS CDK 最佳实践，MCP 服务器和无服务器架构 | [链接](https://github.com/zxkane/aws-skills) |
| changelog-generator | 自动将 Git 提交转换为用户友好的变更日志 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |
| claude-code-terminal-title | 动态设置终端标题，清晰展示当前任务 | [链接](https://github.com/bluzername/claude-code-terminal-title) |
| d3js-visualization | 生成 D3 图表和交互式数据可视化 | [链接](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| ffuf-web-fuzzing | 集成 ffuf 网络模糊测试工具 | [链接](https://github.com/jthack/ffuf_claude_skill) |
| finishing-a-development-branch | 引导开发任务的收尾工作流程 | [链接](https://github.com/obra/superpowers) |
| ios-simulator | 与 iOS 模拟器交互进行测试和调试 | [链接](https://github.com/conorluddy/ios-simulator-skill) |
| jules | 使用 Google Jules AI 代理处理编码任务 | [链接](https://github.com/sanjay3290/ai-skills) |
| langsmith-fetch | 从 LangSmith Studio 获取执行轨迹 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |
| mcp-builder | 创建高质量的 MCP 服务器 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |
| move-code-quality-skill | Move 语言代码质量检查 | [链接](https://github.com/1NickPappas/move-code-quality-skill) |
| playwright-browser-automation | Playwright 自动化测试工具 | [链接](https://github.com/lackeyjb/playwright-skill) |
| prompt-engineering | 提示工程技巧和最佳实践 | [链接](https://github.com/NeoLabHQ/context-engineering-kit) |
| pypict-claude-skill | PICT 成对测试用例生成 | [链接](https://github.com/omkamal/pypict-claude-skill) |
| reddit-fetch | 从 Reddit 获取内容（替代 WebFetch） | [链接](https://github.com/ykdojo/claude-code-tips) |
| skill-creator | 创建高效 Claude 技能的指南 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |
| skill-seekers | 将文档网站转换为 Claude AI 技能 | [链接](https://github.com/yusufkaraaslan/Skill_Seekers) |
| software-architecture | Clean Architecture、SOLID 等设计模式 | [链接](https://github.com/NeoLabHQ/context-engineering-kit) |
| subagent-driven-development | 子代理驱动的开发模式 | [链接](https://github.com/NeoLabHQ/context-engineering-kit) |
| test-driven-development | TDD 测试驱动开发实践 | [链接](https://github.com/obra/superpowers) |
| using-git-worktrees | 创建隔离的 Git 工作树 | [链接](https://github.com/obra/superpowers) |
| connect | 接入 Gmail、Slack、GitHub 等 1000+ 服务 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |
| webapp-testing | Playwright 测试本地 Web 应用 | [链接](https://github.com/ComposioHQ/awesome-claude-skills) |

## 添加新技能

1. 在 `scripts/setup-skills.py` 中的 `SKILLS` 列表添加新技能配置
2. 运行 `python scripts/setup-skills.py` 生成技能配置

```python
{
    "name": "your-skill-name",           # 技能目录名
    "title": "Your Skill Title",         # 技能显示标题
    "description": "技能描述",           # 技能描述
    "repo_url": "https://github.com/user/repo",  # 仓库地址
    "repo_path": "path/to/skill",        # 仓库内技能路径（可选）
    "category": "category-name",         # 分类
},
```

## 常见问题

**Q: 为什么默认只包含 skill.md 文件？**

A: 为了保持项目轻量，默认只创建技能的元数据配置。完整技能内容（参考文档、脚本等）可以通过 `download-skill.py` 按需下载。

**Q: 如何验证技能是否正确安装？**

A: 在 Claude Code 中运行 `/skills` 命令，查看已安装的技能列表。

**Q: 符号链接创建失败怎么办？**

A: Windows 下创建符号链接需要管理员权限。如果没有管理员权限，安装脚本会自动降级使用目录复制。

## 许可证

MIT License

## 贡献

欢迎提交 PR 添加更多有用的技能！

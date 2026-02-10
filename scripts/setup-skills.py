#!/usr/bin/env python3
"""Skills Setup Script - Creates skill configuration files for all commonly used development skills"""

import os
import subprocess
from pathlib import Path

# Base paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"

# Ensure skills directory exists
SKILLS_DIR.mkdir(exist_ok=True)

# Define all skills with their configurations
SKILLS = [
    {
        "name": "artifacts-builder",
        "title": "Artifacts Builder",
        "description": "一套利用现代前端 Web 技术（如 React、Tailwind CSS、shadcn/ui）构建复杂多组件 Claude.ai HTML 资产的工具集。",
        "repo_url": "https://github.com/anthropics/skills",
        "repo_path": "skills/web-artifacts-builder",
        "category": "frontend",
    },
    {
        "name": "aws-skills",
        "title": "AWS Skills",
        "description": "结合 CDK 最佳实践的 AWS 开发，包含成本优化的 MCP 服务器和无服务器/事件驱动架构模式。",
        "repo_url": "https://github.com/zxkane/aws-skills",
        "repo_path": "skills",
        "category": "cloud",
    },
    {
        "name": "changelog-generator",
        "title": "Changelog Generator",
        "description": "通过分析 Git 提交历史，自动将技术性提交转换为用户友好的发布说明，生成面向用户的变更日志。",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/changelog-generator",
        "category": "documentation",
    },
    {
        "name": "claude-code-terminal-title",
        "title": "Claude Code Terminal Title",
        "description": "给每个 Claude-Code 终端窗口动态设置标题，清晰展示当前正在执行的任务，再也不用担心搞混哪个窗口在干啥了。",
        "repo_url": "https://github.com/bluzername/claude-code-terminal-title",
        "repo_path": "",
        "category": "productivity",
    },
    {
        "name": "d3js-visualization",
        "title": "D3.js Visualization",
        "description": "教会 Claude 生成 D3 图表和交互式数据可视化。",
        "repo_url": "https://github.com/chrisvoncsefalvay/claude-d3js-skill",
        "repo_path": "",
        "category": "visualization",
    },
    {
        "name": "ffuf-web-fuzzing",
        "title": "FFUF Web Fuzzing",
        "description": "集成 ffuf 网络模糊测试工具，让 Claude 能执行模糊测试并分析漏洞结果。",
        "repo_url": "https://github.com/jthack/ffuf_claude_skill",
        "repo_path": "",
        "category": "security",
    },
    {
        "name": "finishing-a-development-branch",
        "title": "Finishing a Development Branch",
        "description": "通过清晰的选项引导开发任务的收尾，并处理选定的工作流程。",
        "repo_url": "https://github.com/obra/superpowers",
        "repo_path": "tree/main/skills/finishing-a-development-branch",
        "category": "git",
    },
    {
        "name": "ios-simulator",
        "title": "iOS Simulator",
        "description": "让 Claude 能够与 iOS 模拟器交互，方便测试和调试 iOS 应用。",
        "repo_url": "https://github.com/conorluddy/ios-simulator-skill",
        "repo_path": "",
        "category": "mobile",
    },
    {
        "name": "jules",
        "title": "Jules AI Agent",
        "description": "把编码任务交给 Google Jules AI 代理，异步处理 GitHub 仓库中的 bug 修复、文档编写、测试和功能实现。",
        "repo_url": "https://github.com/sanjay3290/ai-skills",
        "repo_path": "tree/main/skills/jules",
        "category": "ai",
    },
    {
        "name": "langsmith-fetch",
        "title": "LangSmith Fetch",
        "description": "通过自动从 LangSmith Studio 获取并分析执行轨迹，轻松调试 LangChain 和 LangGraph 代理。这是 Claude Code 首个 AI 可观测性技能。",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/langsmith-fetch",
        "category": "ai",
    },
    {
        "name": "mcp-builder",
        "title": "MCP Builder",
        "description": "指导你用 Python 或 TypeScript 创建高质量的 MCP（模型上下文协议）服务器，轻松将外部 API 和服务集成到 LLM 中",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/mcp-builder",
        "category": "integration",
    },
    {
        "name": "move-code-quality-skill",
        "title": "Move Code Quality",
        "description": "根据官方《Move Book》2024 版代码质量检查清单，分析 Move 语言包是否符合规范和最佳实践",
        "repo_url": "https://github.com/1NickPappas/move-code-quality-skill",
        "repo_path": "",
        "category": "quality",
    },
    {
        "name": "playwright-browser-automation",
        "title": "Playwright Browser Automation",
        "description": "由模型调用的 Playwright 自动化工具，用于测试和验证 Web 应用程序。",
        "repo_url": "https://github.com/lackeyjb/playwright-skill",
        "repo_path": "",
        "category": "testing",
    },
    {
        "name": "prompt-engineering",
        "title": "Prompt Engineering",
        "description": "教你那些经典的提示工程技巧和模式，包括 Anthropic 的最佳实践和智能体说服原则，让你的提示效果直接拉满！",
        "repo_url": "https://github.com/NeoLabHQ/context-engineering-kit",
        "repo_path": "tree/master/plugins/customaize-agent/skills/prompt-engineering",
        "category": "productivity",
    },
    {
        "name": "pypict-claude-skill",
        "title": "PyPICT Claude Skill",
        "description": "用 PICT（成对独立组合测试）为需求或代码设计全面的测试用例，自动生成覆盖成对组合的优化测试套件。",
        "repo_url": "https://github.com/omkamal/pypict-claude-skill",
        "repo_path": "",
        "category": "testing",
    },
    {
        "name": "reddit-fetch",
        "title": "Reddit Fetch",
        "description": "当 WebFetch 被封或返回 403 错误时，用 Gemini CLI 从 Reddit 获取内容。",
        "repo_url": "https://github.com/ykdojo/claude-code-tips",
        "repo_path": "tree/main/skills/reddit-fetch",
        "category": "utility",
    },
    {
        "name": "skill-creator",
        "title": "Skill Creator",
        "description": "手把手教你打造高效的 Claude 技能，通过专业领域知识、工作流和工具集成。",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/skill-creator",
        "category": "productivity",
    },
    {
        "name": "skill-seekers",
        "title": "Skill Seekers",
        "description": "几分钟内就能把任何文档网站自动变成 Claude AI 技能。",
        "repo_url": "https://github.com/yusufkaraaslan/Skill_Seekers",
        "repo_path": "",
        "category": "productivity",
    },
    {
        "name": "software-architecture",
        "title": "Software Architecture",
        "description": "实现了包括 Clean Architecture、SOLID 原则以及全面的软件设计最佳实践在内的设计模式。",
        "repo_url": "https://github.com/NeoLabHQ/context-engineering-kit",
        "repo_path": "tree/master/plugins/ddd/skills/software-architecture",
        "category": "architecture",
    },
    {
        "name": "subagent-driven-development",
        "title": "Subagent Driven Development",
        "description": "为每个任务分派独立的子代理，并在迭代之间设置代码审查检查点，实现快速且可控的开发。",
        "repo_url": "https://github.com/NeoLabHQ/context-engineering-kit",
        "repo_path": "tree/master/plugins/sadd/skills/subagent-driven-development",
        "category": "productivity",
    },
    {
        "name": "test-driven-development",
        "title": "Test Driven Development",
        "description": "在编写实现代码之前，用来实现任何功能或修复 bug 时使用。",
        "repo_url": "https://github.com/obra/superpowers",
        "repo_path": "tree/main/skills/test-driven-development",
        "category": "testing",
    },
    {
        "name": "using-git-worktrees",
        "title": "Using Git Worktrees",
        "description": "通过智能目录选择和安全验证，创建隔离的 Git 工作树。",
        "repo_url": "https://github.com/obra/superpowers",
        "repo_path": "blob/main/skills/using-git-worktrees",
        "category": "git",
    },
    {
        "name": "connect",
        "title": "Connect",
        "description": "把 Claude 接入任何应用。发邮件、创建问题、发消息、更新数据库……跨 Gmail、Slack、GitHub、Notion 以及 1000 多种服务。",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/connect",
        "category": "integration",
    },
    {
        "name": "webapp-testing",
        "title": "Webapp Testing",
        "description": "用 Playwright 测试本地 Web 应用，验证前端功能、调试 UI 行为、抓取截图。",
        "repo_url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "repo_path": "blob/master/webapp-testing",
        "category": "testing",
    },
]


def create_skill_structure(skill_path: Path) -> None:
    """Create the standard skill directory structure."""
    # Create subdirectories
    (skill_path / "references").mkdir(exist_ok=True)
    (skill_path / "scripts").mkdir(exist_ok=True)

    # Create a .gitkeep in empty directories
    (skill_path / "references" / ".gitkeep").touch()
    (skill_path / "scripts" / ".gitkeep").touch()


def create_skill(skill_data: dict) -> Path:
    """Create a skill directory with its configuration files."""
    skill_path = SKILLS_DIR / skill_data["name"]
    skill_path.mkdir(exist_ok=True)

    # Create directory structure
    create_skill_structure(skill_path)

    # Build GitHub URL
    base_url = skill_data["repo_url"]
    path_part = skill_data.get("repo_path", "")
    full_url = f"{base_url}/{path_part}" if path_part else base_url

    skill_content = f"""---
name: {skill_data["name"]}
title: {skill_data["title"]}
description: {skill_data["description"]}
category: {skill_data["category"]}
repoUrl: {full_url}
---

# {skill_data["title"]}

> {skill_data["description"]}

## 来源

- 仓库: {full_url}

## 类别

`{skill_data["category"]}`

## 说明

此技能的完整内容需要从官方仓库获取。运行以下命令下载完整技能：

```bash
python scripts/download-skill.py {skill_data["name"]}
```
"""

    skill_md_path = skill_path / "skill.md"
    skill_md_path.write_text(skill_content, encoding="utf-8")

    return skill_path


def main():
    """Main setup function."""
    print(f"Creating skills directory: {SKILLS_DIR}")

    created_count = 0
    for skill in SKILLS:
        skill_path = create_skill(skill)
        created_count += 1
        print(f"  [OK] {skill['name']} -> {skill_path}")

    print("\n" + "=" * 50)
    print(f"Skills setup complete! Created {created_count} skills")
    print(f"Location: {SKILLS_DIR}")
    print("=" * 50)
    print("\nNote: Each skill now has references/ and scripts/ directories.")
    print("Use 'python scripts/download-skill.py <skill-name>' to download full content.")


if __name__ == "__main__":
    main()

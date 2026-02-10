# Skills Setup Script for Windows PowerShell
# This script creates skill configuration files for all commonly used development skills

$skillsRoot = Split-Path -Parent $PSScriptRoot
$skillsDir = Join-Path $skillsRoot "skills"

# Ensure skills directory exists
if (!(Test-Path $skillsDir)) {
    New-Item -ItemType Directory -Path $skillsDir | Out-Null
}

# Define all skills with their configurations
$skills = @(
    @{
        name = "artifacts-builder"
        title = "Artifacts Builder"
        description = "一套利用现代前端 Web 技术（如 React、Tailwind CSS、shadcn/ui）构建复杂多组件 Claude.ai HTML 资产的工具集。"
        repoUrl = "https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder"
        category = "frontend"
    },
    @{
        name = "aws-skills"
        title = "AWS Skills"
        description = "结合 CDK 最佳实践的 AWS 开发，包含成本优化的 MCP 服务器和无服务器/事件驱动架构模式。"
        repoUrl = "https://github.com/zxkane/aws-skills"
        category = "cloud"
    },
    @{
        name = "changelog-generator"
        title = "Changelog Generator"
        description = "通过分析 Git 提交历史，自动将技术性提交转换为用户友好的发布说明，生成面向用户的变更日志。"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/changelog-generator"
        category = "documentation"
    },
    @{
        name = "claude-code-terminal-title"
        title = "Claude Code Terminal Title"
        description = "给每个 Claude-Code 终端窗口动态设置标题，清晰展示当前正在执行的任务，再也不用担心搞混哪个窗口在干啥了。"
        repoUrl = "https://github.com/bluzername/claude-code-terminal-title"
        category = "productivity"
    },
    @{
        name = "d3js-visualization"
        title = "D3.js Visualization"
        description = "教会 Claude 生成 D3 图表和交互式数据可视化。"
        repoUrl = "https://github.com/chrisvoncsefalvay/claude-d3js-skill"
        category = "visualization"
    },
    @{
        name = "ffuf-web-fuzzing"
        title = "FFUF Web Fuzzing"
        description = "集成 ffuf 网络模糊测试工具，让 Claude 能执行模糊测试并分析漏洞结果。"
        repoUrl = "https://github.com/jthack/ffuf_claude_skill"
        category = "security"
    },
    @{
        name = "finishing-a-development-branch"
        title = "Finishing a Development Branch"
        description = "通过清晰的选项引导开发任务的收尾，并处理选定的工作流程。"
        repoUrl = "https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch"
        category = "git"
    },
    @{
        name = "ios-simulator"
        title = "iOS Simulator"
        description = "让 Claude 能够与 iOS 模拟器交互，方便测试和调试 iOS 应用。"
        repoUrl = "https://github.com/conorluddy/ios-simulator-skill"
        category = "mobile"
    },
    @{
        name = "jules"
        title = "Jules AI Agent"
        description = "把编码任务交给 Google Jules AI 代理，异步处理 GitHub 仓库中的 bug 修复、文档编写、测试和功能实现。"
        repoUrl = "https://github.com/sanjay3290/ai-skills/tree/main/skills/jules"
        category = "ai"
    },
    @{
        name = "langsmith-fetch"
        title = "LangSmith Fetch"
        description = "通过自动从 LangSmith Studio 获取并分析执行轨迹，轻松调试 LangChain 和 LangGraph 代理。这是 Claude Code 首个 AI 可观测性技能。"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/langsmith-fetch"
        category = "ai"
    },
    @{
        name = "mcp-builder"
        title = "MCP Builder"
        description = "指导你用 Python 或 TypeScript 创建高质量的 MCP（模型上下文协议）服务器，轻松将外部 API 和服务集成到 LLM 中"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mcp-builder"
        category = "integration"
    },
    @{
        name = "move-code-quality-skill"
        title = "Move Code Quality"
        description = "根据官方《Move Book》2024 版代码质量检查清单，分析 Move 语言包是否符合规范和最佳实践"
        repoUrl = "https://github.com/1NickPappas/move-code-quality-skill"
        category = "quality"
    },
    @{
        name = "playwright-browser-automation"
        title = "Playwright Browser Automation"
        description = "由模型调用的 Playwright 自动化工具，用于测试和验证 Web 应用程序。"
        repoUrl = "https://github.com/lackeyjb/playwright-skill"
        category = "testing"
    },
    @{
        name = "prompt-engineering"
        title = "Prompt Engineering"
        description = "教你那些经典的提示工程技巧和模式，包括 Anthropic 的最佳实践和智能体说服原则，让你的提示效果直接拉满！"
        repoUrl = "https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering"
        category = "productivity"
    },
    @{
        name = "pypict-claude-skill"
        title = "PyPICT Claude Skill"
        description = "用 PICT（成对独立组合测试）为需求或代码设计全面的测试用例，自动生成覆盖成对组合的优化测试套件。"
        repoUrl = "https://github.com/omkamal/pypict-claude-skill"
        category = "testing"
    },
    @{
        name = "reddit-fetch"
        title = "Reddit Fetch"
        description = "当 WebFetch 被封或返回 403 错误时，用 Gemini CLI 从 Reddit 获取内容。"
        repoUrl = "https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch"
        category = "utility"
    },
    @{
        name = "skill-creator"
        title = "Skill Creator"
        description = "手把手教你打造高效的 Claude 技能，通过专业领域知识、工作流和工具集成。"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/skill-creator"
        category = "productivity"
    },
    @{
        name = "skill-seekers"
        title = "Skill Seekers"
        description = "几分钟内就能把任何文档网站自动变成 Claude AI 技能。"
        repoUrl = "https://github.com/yusufkaraaslan/Skill_Seekers"
        category = "productivity"
    },
    @{
        name = "software-architecture"
        title = "Software Architecture"
        description = "实现了包括 Clean Architecture、SOLID 原则以及全面的软件设计最佳实践在内的设计模式。"
        repoUrl = "https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture"
        category = "architecture"
    },
    @{
        name = "subagent-driven-development"
        title = "Subagent Driven Development"
        description = "为每个任务分派独立的子代理，并在迭代之间设置代码审查检查点，实现快速且可控的开发。"
        repoUrl = "https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development"
        category = "productivity"
    },
    @{
        name = "test-driven-development"
        title = "Test Driven Development"
        description = "在编写实现代码之前，用来实现任何功能或修复 bug 时使用。"
        repoUrl = "https://github.com/obra/superpowers/tree/main/skills/test-driven-development"
        category = "testing"
    },
    @{
        name = "using-git-worktrees"
        title = "Using Git Worktrees"
        description = "通过智能目录选择和安全验证，创建隔离的 Git 工作树。"
        repoUrl = "https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/"
        category = "git"
    },
    @{
        name = "connect"
        title = "Connect"
        description = "把 Claude 接入任何应用。发邮件、创建问题、发消息、更新数据库……跨 Gmail、Slack、GitHub、Notion 以及 1000 多种服务。"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/connect"
        category = "integration"
    },
    @{
        name = "webapp-testing"
        title = "Webapp Testing"
        description = "用 Playwright 测试本地 Web 应用，验证前端功能、调试 UI 行为、抓取截图。"
        repoUrl = "https://github.com/ComposioHQ/awesome-claude-skills/blob/master/webapp-testing"
        category = "testing"
    }
)

# Create each skill directory and configuration
foreach ($skill in $skills) {
    $skillPath = Join-Path $skillsDir $skill.name

    # Create skill directory
    if (!(Test-Path $skillPath)) {
        New-Item -ItemType Directory -Path $skillPath | Out-Null
    }

    # Create skill.md file
    $skillContent = @"
---
name: $($skill.name)
title: $($skill.title)
description: $($skill.description)
category: $($skill.category)
repoUrl: $($skill.repoUrl)
---

# $($skill.title)

> $($skill.description)

## 来源

- 仓库: $($skill.repoUrl)

## 类别

`$($skill.category)`
"@

    $skillMdPath = Join-Path $skillPath "skill.md"
    Set-Content -Path $skillMdPath -Value $skillContent -Encoding UTF8

    Write-Host "✓ Created $($skill.name)" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Skills setup complete!" -ForegroundColor Cyan
Write-Host "Created $($skills.Count) skills in: $skillsDir" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

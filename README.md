# Claude Code Dev Skills Collection

> A curated collection of commonly used development skills for Claude Code.

[**中文**](./README_zh.md)

---

## Quick Start

### Windows

```powershell
# Run PowerShell as Administrator
.\scripts\install.ps1
```

### macOS/Linux

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

## Installation Methods

### Method 1: Installation Script (Recommended)

The project provides automated installation scripts that handle symbolic links, junctions, or directory copying.

### Method 2: Symbolic Link

Create a symbolic link in your Claude Code configuration directory pointing to the `skills` folder:

```powershell
# Windows (PowerShell - requires Administrator privileges)
# Replace with your actual project path
$projectPath = "C:\path\to\self-use-skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills" -Target "$projectPath\skills"
```

```bash
# macOS/Linux
# Replace with your actual project path
PROJECT_PATH="/path/to/self-use-skills"
ln -s "$PROJECT_PATH/skills" ~/.claude/skills
```

### Method 3: Configuration File

Add to `~/.claude/settings.json` (Windows: `%USERPROFILE%\.claude\settings.json`):

```json
{
  "skillsPath": "C:\\path\\to\\self-use-skills\\skills"
}
```

> **Note**: Windows paths require double backslashes `\\`

## Uninstall

### Windows

```powershell
.\scripts\uninstall.ps1
```

### macOS/Linux

```bash
./scripts/uninstall.sh
```

## Project Structure

```
self-use-skills/
├── skills/                    # Skills directory
│   └── skill-name/            # Single skill
│       └── skill.md           # Skill configuration
├── scripts/                   # Management scripts
│   ├── install.ps1            # Windows installation script
│   ├── install.sh             # macOS/Linux installation script
│   ├── uninstall.ps1          # Windows uninstallation script
│   ├── uninstall.sh           # macOS/Linux uninstallation script
│   ├── setup-skills.py        # Skill configuration generator
│   └── download-skill.py      # Download full skill from official repo
├── .gitignore
├── package.json
└── README.md
```

## Downloading Full Skill Content

By default, each skill only contains basic configuration (`skill.md`). To get the complete skill content (including reference documents and scripts), use:

```bash
# Download a single skill
python scripts/download-skill.py skill-creator

# Download all skills
python scripts/download-skill.py all

# List all available skills
python scripts/download-skill.py --list

# Force overwrite existing content
python scripts/download-skill.py skill-creator --force
```

## Included Skills

| Skill Name | Description | Source |
|------------|-------------|--------|
| artifacts-builder | Build complex multi-component HTML artifacts with modern frontend technologies | [Link](https://github.com/anthropics/skills) |
| aws-skills | AWS CDK best practices, MCP servers, and serverless architectures | [Link](https://github.com/zxkane/aws-skills) |
| changelog-generator | Convert Git commits to user-friendly changelogs | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |
| claude-code-terminal-title | Dynamic terminal titles to show current tasks | [Link](https://github.com/bluzername/claude-code-terminal-title) |
| d3js-visualization | Generate D3 charts and interactive visualizations | [Link](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| ffuf-web-fuzzing | Integrate ffuf web fuzzing tool | [Link](https://github.com/jthack/ffuf_claude_skill) |
| finishing-a-development-branch | Guide for finishing development tasks | [Link](https://github.com/obra/superpowers) |
| ios-simulator | Interact with iOS simulator for testing | [Link](https://github.com/conorluddy/ios-simulator-skill) |
| jules | Use Google Jules AI agent for coding tasks | [Link](https://github.com/sanjay3290/ai-skills) |
| langsmith-fetch | Fetch execution traces from LangSmith Studio | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |
| mcp-builder | Create high-quality MCP servers | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |
| move-code-quality-skill | Move language code quality checks | [Link](https://github.com/1NickPappas/move-code-quality-skill) |
| playwright-browser-automation | Playwright automation testing | [Link](https://github.com/lackeyjb/playwright-skill) |
| prompt-engineering | Prompt engineering techniques and best practices | [Link](https://github.com/NeoLabHQ/context-engineering-kit) |
| pypict-claude-skill | PICT pairwise test case generation | [Link](https://github.com/omkamal/pypict-claude-skill) |
| reddit-fetch | Fetch content from Reddit (WebFetch alternative) | [Link](https://github.com/ykdojo/claude-code-tips) |
| skill-creator | Guide for creating effective Claude skills | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |
| skill-seekers | Convert documentation sites to Claude AI skills | [Link](https://github.com/yusufkaraaslan/Skill_Seekers) |
| software-architecture | Clean Architecture, SOLID, design patterns | [Link](https://github.com/NeoLabHQ/context-engineering-kit) |
| subagent-driven-development | Subagent-driven development workflow | [Link](https://github.com/NeoLabHQ/context-engineering-kit) |
| test-driven-development | TDD test-driven development practices | [Link](https://github.com/obra/superpowers) |
| using-git-worktrees | Create isolated Git worktrees | [Link](https://github.com/obra/superpowers) |
| connect | Integrate with Gmail, Slack, GitHub, 1000+ services | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |
| webapp-testing | Test local web apps with Playwright | [Link](https://github.com/ComposioHQ/awesome-claude-skills) |

## Adding New Skills

1. Add new skill configuration to the `SKILLS` list in `scripts/setup-skills.py`
2. Run `python scripts/setup-skills.py` to generate skill configuration

```python
{
    "name": "your-skill-name",           # Skill directory name
    "title": "Your Skill Title",         # Skill display title
    "description": "Skill description",  # Skill description
    "repo_url": "https://github.com/user/repo",  # Repository URL
    "repo_path": "path/to/skill",        # Path within repo (optional)
    "category": "category-name",         # Category
},
```

## FAQ

**Q: Why does each skill only contain skill.md by default?**

A: To keep the project lightweight. Only metadata configuration is created by default. Full skill content (references, scripts) can be downloaded on-demand using `download-skill.py`.

**Q: How to verify skills are installed correctly?**

A: Run `/skills` command in Claude Code to see the list of installed skills.

**Q: What if symbolic link creation fails?**

A: On Windows, creating symbolic links requires Administrator privileges. Without admin rights, the installation script will automatically fall back to directory copying.

## License

MIT License

## Contributing

PRs welcome to add more useful skills!

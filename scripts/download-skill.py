#!/usr/bin/env python3
"""
Download full skill content from official repositories.
Usage: python scripts/download-skill.py <skill-name>
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Skill repository mappings
SKILL_REPOS = {
    "artifacts-builder": {
        "repo": "https://github.com/anthropics/skills.git",
        "path": "skills/web-artifacts-builder",
    },
    "aws-skills": {
        "repo": "https://github.com/zxkane/aws-skills.git",
        "path": "skills",
    },
    "changelog-generator": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "changelog-generator",
    },
    "claude-code-terminal-title": {
        "repo": "https://github.com/bluzername/claude-code-terminal-title.git",
        "path": "",
    },
    "d3js-visualization": {
        "repo": "https://github.com/chrisvoncsefalvay/claude-d3js-skill.git",
        "path": "",
    },
    "ffuf-web-fuzzing": {
        "repo": "https://github.com/jthack/ffuf_claude_skill.git",
        "path": "",
    },
    "finishing-a-development-branch": {
        "repo": "https://github.com/obra/superpowers.git",
        "path": "skills/finishing-a-development-branch",
    },
    "ios-simulator": {
        "repo": "https://github.com/conorluddy/ios-simulator-skill.git",
        "path": "",
    },
    "jules": {
        "repo": "https://github.com/sanjay3290/ai-skills.git",
        "path": "skills/jules",
    },
    "langsmith-fetch": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "langsmith-fetch",
    },
    "mcp-builder": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "mcp-builder",
    },
    "move-code-quality-skill": {
        "repo": "https://github.com/1NickPappas/move-code-quality-skill.git",
        "path": "",
    },
    "playwright-browser-automation": {
        "repo": "https://github.com/lackeyjb/playwright-skill.git",
        "path": "",
    },
    "prompt-engineering": {
        "repo": "https://github.com/NeoLabHQ/context-engineering-kit.git",
        "path": "plugins/customaize-agent/skills/prompt-engineering",
    },
    "pypict-claude-skill": {
        "repo": "https://github.com/omkamal/pypict-claude-skill.git",
        "path": "",
    },
    "reddit-fetch": {
        "repo": "https://github.com/ykdojo/claude-code-tips.git",
        "path": "skills/reddit-fetch",
    },
    "skill-creator": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "skill-creator",
    },
    "skill-seekers": {
        "repo": "https://github.com/yusufkaraaslan/Skill_Seekers.git",
        "path": "",
    },
    "software-architecture": {
        "repo": "https://github.com/NeoLabHQ/context-engineering-kit.git",
        "path": "plugins/ddd/skills/software-architecture",
    },
    "subagent-driven-development": {
        "repo": "https://github.com/NeoLabHQ/context-engineering-kit.git",
        "path": "plugins/sadd/skills/subagent-driven-development",
    },
    "test-driven-development": {
        "repo": "https://github.com/obra/superpowers.git",
        "path": "skills/test-driven-development",
    },
    "using-git-worktrees": {
        "repo": "https://github.com/obra/superpowers.git",
        "path": "skills/using-git-worktrees",
    },
    "connect": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "connect",
    },
    "webapp-testing": {
        "repo": "https://github.com/ComposioHQ/awesome-claude-skills.git",
        "path": "webapp-testing",
    },
}


def run_command(cmd, cwd=None):
    """Run a command and return its output."""
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def download_skill(skill_name: str, force: bool = False):
    """Download a skill from its official repository."""
    if skill_name not in SKILL_REPOS:
        print(f"Error: Skill '{skill_name}' not found in registry.")
        print("Available skills:")
        for name in sorted(SKILL_REPOS.keys()):
            print(f"  - {name}")
        return False

    repo_info = SKILL_REPOS[skill_name]
    repo_url = repo_info["repo"]
    repo_path = repo_info["path"]

    # Paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    skills_dir = project_root / "skills"
    skill_dir = skills_dir / skill_name
    temp_dir = project_root / ".temp" / skill_name

    print(f"Downloading skill: {skill_name}")
    print(f"Source: {repo_url}")
    print(f"Target: {skill_dir}")
    print()

    # Check if skill already has content
    if skill_dir.exists():
        refs_dir = skill_dir / "references"
        scripts_dir = skill_dir / "scripts"
        has_content = (
            (refs_dir.exists() and any(refs_dir.iterdir()))
            or (scripts_dir.exists() and any(scripts_dir.iterdir()))
        )

        if has_content and not force:
            response = input(f"Skill '{skill_name}' already has content. Overwrite? (y/N): ")
            if response.lower() != "y":
                print("Download cancelled.")
                return False

    # Clean temp directory
    if temp_dir.exists():
        import shutil
        shutil.rmtree(temp_dir)

    # Clone repository
    print("Cloning repository...")
    returncode, stdout, stderr = run_command(f"git clone --depth 1 {repo_url} \"{temp_dir}\"")
    if returncode != 0:
        print(f"Error cloning repository: {stderr}")
        return False

    # Determine source directory
    source_dir = temp_dir
    if repo_path:
        source_dir = temp_dir / repo_path
        if not source_dir.exists():
            print(f"Warning: Expected path '{repo_path}' not found in repository.")
            print("Using repository root instead.")
            source_dir = temp_dir

    # Copy files to skill directory
    print("Copying files...")
    import shutil

    # Copy references
    refs_source = source_dir / "references"
    if refs_source.exists():
        refs_target = skill_dir / "references"
        if refs_target.exists():
            shutil.rmtree(refs_target)
        shutil.copytree(refs_source, refs_target)
        print(f"  Copied references/")

    # Copy scripts
    scripts_source = source_dir / "scripts"
    if scripts_source.exists():
        scripts_target = skill_dir / "scripts"
        if scripts_target.exists():
            shutil.rmtree(scripts_target)
        shutil.copytree(scripts_source, scripts_target)
        print(f"  Copied scripts/")

    # Copy skill.md if it exists and is different
    skill_md_source = source_dir / "skill.md"
    if skill_md_source.exists():
        # Read both files and compare
        existing_content = (skill_dir / "skill.md").read_text(encoding="utf-8") if (skill_dir / "skill.md").exists() else ""
        new_content = skill_md_source.read_text(encoding="utf-8")

        # Only copy if content is significantly different (not just our template)
        if "此技能的完整内容需要从官方仓库获取" not in new_content:
            (skill_dir / "skill.md").write_text(new_content, encoding="utf-8")
            print(f"  Updated skill.md")

    # Clean up
    print("Cleaning up...")
    shutil.rmtree(temp_dir)

    print()
    print(f"Successfully downloaded skill: {skill_name}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Download full skill content from official repositories"
    )
    parser.add_argument(
        "skill",
        nargs="?",
        help="Skill name to download (or 'all' to download all skills)"
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force overwrite existing content"
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all available skills"
    )

    args = parser.parse_args()

    if args.list:
        print("Available skills:")
        for name in sorted(SKILL_REPOS.keys()):
            info = SKILL_REPOS[name]
            print(f"  {name:30} {info['repo']}")
        return 0

    if not args.skill:
        parser.print_help()
        return 1

    if args.skill == "all":
        print("Downloading all skills...")
        print()
        success_count = 0
        for skill_name in sorted(SKILL_REPOS.keys()):
            if download_skill(skill_name, args.force):
                success_count += 1
            print()

        print(f"Downloaded {success_count}/{len(SKILL_REPOS)} skills successfully.")
        return 0

    return 0 if download_skill(args.skill, args.force) else 1


if __name__ == "__main__":
    sys.exit(main())

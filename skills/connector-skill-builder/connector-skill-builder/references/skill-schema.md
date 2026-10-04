# SKILL.md 结构模板

> Reference for: connector-skill-builder
> Load when: 生成步骤

## frontmatter

仅 `name` + `description`；description 写全触发条件（场景 / 文件类型 / 任务类型），正文不重复。

```yaml
---
name: 软件名-connector
description: 接入说明与触发条件。当需要 [场景] 时使用。
---
```

## 正文章节（按序）

1. `# 名称` — 一句话功能定义
2. `## 角色定位` — 2–3 句，定义专家身份与专长
3. `## 触发场景` — 具体场景 / 关键词列表
4. `## 核心流程` — 编号步骤，含执行通道说明（MCP 工具 / API / CLI 命令）
5. `## 约束` — MUST / MUST NOT 两个列表
6. `## 参考指引` — 表格：主题 / 文件 / 何时读

## 渐进披露

- 正文 ≤500 行；细节进 `references/`
- `references/` 一级平铺，从 SKILL.md 直接链接
- 超 100 行的参考文件顶部加目录

## 结构示例

```
软件-connector/
├── SKILL.md
├── scripts/          # 确定性操作脚本
└── references/       # 协议 / 参数表 / 模板
```

## 触发词建议

description 中列出触发关键词：软件名、领域术语、接入动作（"接入""连接""操作手册""通道"）。

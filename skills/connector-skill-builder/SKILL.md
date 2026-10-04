---
name: connector-skill-builder
description: 为任意具备 API / MCP / CLI 可编程面的工程软件生成接入 Skill（软件操作手册）并执行最小通路验证。当需要接入新软件、为软件编写 Agent 接入手册、扩展工具通道、或核查现有软件接入时使用。
---

# Connector Skill Builder

软件接入 Skill 生成器。输入一个软件，输出：探测报告 → 能力映射 → 接入 Skill（SKILL.md + scripts/ + references/）→ 验证记录 → 路由登记。

## 前置门槛

检查软件可编程面，任一命中即通过：

| 面 | 检查 |
|---|---|
| MCP server | `.mcp.json` / 官方 MCP 文档 / 社区 server |
| CLI | 可执行文件 `--help` / 子命令 |
| 本地服务 | 端口监听 / JSON 或等价协议 |
| SDK / 脚本 API | 官方文档 / 语言绑定 |

未命中任一 → 不生成，记录缺口。

## 生成流程

### 1 探测

1. 定位可编程面（端口 / 命令 / 配置 / 文档）
2. 用 `scripts/probe_template.py` 起步，跑最小探针：
   - 心跳：ping / 存活检查
   - 读状态：场景 / 文档 / 项目信息
   - 执行一次：最小操作
   - 回传：截图 / 输出 / 结果文件
3. 全部成功 → 进入映射；失败 → 记录失败点并停止

### 2 映射

能力 → 能力接口表：

| 能力接口 | 覆盖操作 |
|---|---|
| 3D 建模 | 对象创建 / 修改 / 拓扑 / UV |
| 绑定 | 骨骼 / 权重 / 约束 |
| 导出 | FBX / GLB / VRM / USD / 图集 |
| 拆层 | 图层拆分 / 命名 / 分组 |
| 绑参 | 参数读写 / 映射表 |
| 像素帧 | 画布 / 图层 / 帧动画 |
| 渲染回传 | 视口 / 预览截图 |

清单外能力登记为扩展接口，不强行归类。

### 3 生成

按 `references/skill-schema.md` 生成 SKILL.md：

- frontmatter：`name` + `description`（触发条件写入 description）
- 正文：角色定位 / 触发场景 / 核心流程 / 约束（MUST / MUST NOT）/ 参考指引
- 渐进披露：正文 ≤500 行，细节进 `references/`
- 附 `scripts/`（确定性操作脚本）、`references/`（协议 / 清单 / 模板）
- 手册无人称、描述功能

### 4 验证与登记

1. 按 `references/verification.md` 执行最小通路验证（心跳 + 读状态 + 执行 + 回传）
2. 验证通过 → 登记路由表：能力接口 × 软件 × 通道类型 × 验证记录
3. 未通过不登记

## 约束

### MUST
- 先探测后生成（探针通过才写手册）
- description 写全触发条件
- 验证未通过不登记
- 输出无人称、只描述功能

### MUST NOT
- 有可编程面时不写 UI 操作步骤
- 为不满足门槛的软件生成手册
- 在 SKILL.md 堆细节（进 references/）

## 参考

| 主题 | 文件 | 何时读 |
|---|---|---|
| SKILL.md 结构 | `references/skill-schema.md` | 生成步骤 |
| 验证协议 | `references/verification.md` | 验证步骤 |
| 探针模板 | `scripts/probe_template.py` | 探测步骤 |
| 工具推荐清单 | `references/tool-recipes.md` | 推荐 / 检索候选工具时 |

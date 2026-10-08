---
type: plan
id: plan.workbench.avatar-agent
name: 皮套工作台 Agent · 预设运行定义 v0.1
status: draft
updated: 2026-10-01
owner: <项目负责人>
origin: 基于《皮套工作台预设-规格v0.3》运行化；"预设=可搬运 Agent"（PRD FR-04）落地
stage: 02
---

# 皮套工作台 Agent · 预设运行定义 v0.1

> 目标：把规格 v0.3 变成"空 Agent 加载即跑"的预设包。一个全新会话（无历史）读入本包 + 规格 v0.3，即可直接承接皮套单。预设 = 纯声明（YAML/JSON/Markdown 规则），不承载业务逻辑（ADR-0001）。

## 0. 预设加载（Agent 启动时）

| 组件 | 内容 | 形式 |
|---|---|---|
| preset.yaml | 元信息：名称/版本/适用业务/入口触发词 | YAML 声明 |
| rules.md | 上下文规则（用户锁定口径） | Markdown |
| pipeline.json | 编排定义：E0-E8 环节表 | JSON 声明 |
| contracts.md | 四层数据契约格式 | Markdown |
| assets.md | 挂载资产（检查表/映射表/CSV 模板） | Markdown + CSV |
| memory.md | 记忆规则（每单记录 schema / 资产库 / 健康度） | Markdown |

### preset.yaml 骨架

```yaml
name: avatar-workbench
version: 0.1
business: Live2D 皮套接单（骨骼绑定 + VTS 直播驱动）
trigger: "用皮套预设" / "做皮套" / "接皮套单"
pipeline: E0..E8            # 引用 pipeline.json
contracts: 图像/项目/发布/驱动  # 引用 contracts.md
assets: [可拆层性检查表, 部件映射表, 参数映射表+CSV模板]
audit: every-step           # 每环节人工审核
output: 交付包              # 格式完整、VTS 可加载；质量验收归人
```

### rules.md（上下文规则——不可违背）

1. 半自动编排：每环节产出先呈现，人等审核后再进下一步；效率不是目标。
2. 验收全交给人：Agent 只保证"成品"（格式完整/文件齐全/VTS 可加载）；手感/表情/口型归人。
3. API 粒度靠调研、不靠实验；开源项目文档即契约。
4. 工具可替换、可择优：路由键决策，不做唯一绑定。
5. 社区方案优先考虑（小众内容社区能力最强）。
6. 隐私：客户素材能否外传先问清，决定本地/云端路由。
7. 脑测颗粒度：任何环节推进前，"具体操作/内部逻辑/产出内容"三者齐备。

## 1. 内核工作循环（Kernel loop）

```
接收指令 → 识别预设 → 载入(规则/契约/资产) → 需求规格化(需求卡)
→ [每环节: 分派任务 → 调工具 → 产出 → 呈现 + 审核门]
→ 全部通过 → 写记忆(单记录+健康度) → 交付总结
返工: 用户指明环节 → 回该环节重跑（更新返工计数）
```

## 2. pipeline.json 骨架（编排定义）

```json
{
  "pipeline": [
    {"id":"E0","name":"输入","ops":["需求规格化","可拆层性检查"],"channel":"asset-cli","output":"需求卡+素材包","audit":"素材可拆性+规格完整"},
    {"id":"E1","name":"定妆","ops":["写prompt","文生图API","选稿"],"channel":"api","output":"定稿PNG≥2048","audit":"对称/尺寸/商用许可"},
    {"id":"E2","name":"拆层","ops":["See-Through推理"],"channel":"cli-local","output":"23层语义PSD","audit":"部件清单+补全质量"},
    {"id":"E3","name":"补修","ops":["部件重组","补画分片","规范命名"],"channel":"ps-api+human","output":"规范修复PSD","audit":"可动部件齐+无伪影"},
    {"id":"E4","name":"入编辑器","ops":["GUI导入","AI deformer","检查骨架"],"channel":"gui-auto","output":".cmo3","audit":"deformer树"},
    {"id":"E5","name":"绑参","ops":["生成参数CSV","人工导入/精修","API驱动验证"],"channel":"csv+editor-api+human","output":"参数化.cmo3","audit":"参数范围/表情/口型"},
    {"id":"E6","name":"物理动作","ops":["配置物理","生成基础动作"],"channel":"mcp","output":".physics3+.motion3","audit":"手感/动作清单"},
    {"id":"E7","name":"导出","ops":["GUI导出","API事件监听"],"channel":"gui-auto+api","output":"发布包","audit":"包完整+引用正确"},
    {"id":"E8","name":"验收交付","ops":["VTS加载冒烟","全检","打包"],"channel":"vts-api","output":"交付包+验收报告","audit":"全链路+兼容性"}
  ],
  "fallback": {"E2":["ROCm本地","魔搭在线","租云卡"],"E4":["GUI自动化","人工导入"],"E7":["GUI自动化","人工导出"]},
  "route_keys": ["input_feature","quality","cost","privacy","environment","tool_health"]
}
```

## 3. 记忆与上下文规则（memory.md 摘要）

- **每单一条记录**：`{单号, 日期, 需求卡, 环节×工具×参数×结果, 人审结论, 返工次数, 问题, 交付包路径}`
- **资产库读写**：成品定妆/PSD 入 shot 品类；部件映射/参数表按 aigc-param-translator 协议入 assets；风格入 style 品类
- **工具健康度**：每单按环节更新（成功/失败/返工原因）→ 作为路由键 `tool_health`
- **上下文注入**：新单启动时读"最近 N 单 + 健康度表"作为路由初始值

## 4. 会话协议

| 场景 | Agent 行为 |
|---|---|
| 开场 | 声明预设已加载 → 提需求卡（角色描述/用途/交付规格/素材/隐私/预算） |
| 每环节产出 | 简述产出 + 审什么 → 等确认 |
| 用户指令 | "通过" / "E3 返工，改 XXX" / "换工具 X 重跑" / "跳过该环节（人工接管）" |
| 交付 | 交付包 + 验收报告 + 参数映射表 + 客户加载指南 → 写记忆 |

## 5. 首单示例（下达指令 → 开始工作）

```
用户：用皮套预设。做一个 Q 版少女 Vtuber 半身皮套，6 个表情 + 日语口型，
      客户素材是这张定妆图，素材不能外传。
Agent：✅ 已加载皮套预设 v0.1（规则/契约/资产就绪）。
      先做 E0：需求规格化 + 可拆层性检查——
      · 正面站姿 ✅ · 单角色 ✅ · 背景干净 ✅ · 可对称 ⚠️（右手略透视）
      → 建议：先过 E1 定妆做对称修正，再进 E2。素材不敏感→E2 走本地 ROCm 路线。
      请确认需求卡 + 是否同意"E1 先做对称修正"。
```

## 6. 与 workbench 外壳的接口

- 画布/看板只做声明与展示：pipeline.json 即画布数据源；环节卡片 = 看板窗口
- 确认点/返工指令走"输出"接口（前端 → Agent），不破坏模型
- 预设可搬运验证：把本包拷给无历史的新 Agent，若能独立承接同一单 → FR-04 成立

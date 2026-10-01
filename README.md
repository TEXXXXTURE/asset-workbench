# 资产工作台（asset-workbench）

<p align="center"><img src="assets/icon.png" width="128" alt="asset-workbench icon"></p>

角色资产生产工作台。共享上游，分叉出口：皮套（Live2D）、像素游戏素材、萌化动画化三条业务线共用同一套上游资产，在定妆图之后分叉。

## 项目结构

```
asset-workbench/
├── README.md
├── assets/
│   └── icon.png             # 项目概念图标
├── docs/
│   └── model-map.md         # 模型能力地图与 E1 选型调优
└── presets/
    ├── 皮套工作台预设-规格v0.3.md
    ├── 像素素材工作台预设-走查v0.1.md
    └── 皮套工作台Agent-预设运行定义v0.1.md
```

## 共享上游

概念图 → 定妆图 → 部件语义拆分 → 动作语义字典。

分界点在定妆图之后，业务线选择不同出口。

## 三条业务线

| 线 | 出口 | 落档 |
|---|---|---|
| E · 皮套 | Live2D 模型包（.model3/.moc3/.physics3/.motion3） | 规格 v0.3 |
| P · 像素 | 像素游戏素材（sprite / 图集） | 走查 v0.1 |
| M · 萌化动画化 | 萌化图 / 循环动画（GIF / sprite sheet / JSON） | 工具调研完成 |

## 皮套线（E 线）

环节链：E0 输入 → E1 定妆 → E2 拆层 → E3 补修 → E4 入编辑器 → E5 绑参 → E6 物理动作 → E7 导出 → E8 验收。

每个环节包含：具体操作、内部逻辑、产出内容、通道、人工审核门。

四层数据契约：

- 图像契约：PNG-alpha / PSD 层结构
- 项目契约：.cmo3 + 参数 CSV
- 发布契约：.model3 + .moc3 + .physics3 + .motion3
- 驱动契约：PARAM 映射表

Agent 通道：软件 API / MCP / CLI·本地推理 / GUI 自动化。

E5 通道：Cubism 外部集成 API（读写参数值、事件感知；参数 0.5 秒临时缓冲不落盘）+ 参数 CSV 批量导入导出（半自动主通道）。

路由：路由键（输入特征 / 质量要求 / 成本 / 隐私 / 环境 / 工具健康度）→ 策略（规则 → 评分 → 实测）→ 回退链。

## 像素线（P 线）

P 环节对称走查（人类像素画师 × AI 工作台双轨）。

六风险：帧一致性 / 调色板锁定 / 尺寸网格 / 循环闭合 / 图集格式 / 商用许可。

## 萌化动画化（M 线）

三层工具地图：在线一键层 / 本地可控层 / 动态动画层。

- 手绘路线：Animated Drawings → Dreamina Sketch-to-Video → ToonCrafter
- 像素路线：Sprite-AI → Ludo Forge Pixel / Anijam

## 模型能力地图（E1 选型调优）

主流生图模型按内容类型划分（二次元 / 写实 / 像素 / 国风 / 特定画风），配 E1 定妆的选型路由与抽卡调优闭环。详见 [docs/model-map.md](docs/model-map.md)。

## 文档导航

| 文档 | 内容 |
|---|---|
| [presets/皮套工作台预设-规格v0.3.md](presets/皮套工作台预设-规格v0.3.md) | 皮套线 E0-E8 规格、四层契约、E5 API 清单、路由、输出契约、单点测试计划 |
| [presets/像素素材工作台预设-走查v0.1.md](presets/像素素材工作台预设-走查v0.1.md) | 像素线 P 环节走查、六风险、与皮套线对称/差异 |
| [presets/皮套工作台Agent-预设运行定义v0.1.md](presets/皮套工作台Agent-预设运行定义v0.1.md) | 六组件预设包、内核循环、会话协议、首单示例 |
| [docs/model-map.md](docs/model-map.md) | 模型能力地图与 E1 选型调优 |

## 状态

- 皮套规格 v0.3、像素走查 v0.1、Agent 运行定义 v0.1 落档（2026-10-01）
- 单点测试计划：台阶 0 魔搭在线拆层试跑 → 台阶 1 本地部署 → E5 CSV 验证 → E4/E7 GUI 校准
- 工作台外壳未动工

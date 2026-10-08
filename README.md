# 资产工作台（asset-workbench）

<p align="center"><img src="assets/icon.png" width="128" alt="asset-workbench icon"></p>

角色资产生产工作台。共享上游，定妆图后分叉业务线；每条业务线为预设选项，模拟正常工作步骤（概念 → 定妆 → 部件拆分 → 动作字典 → 分叉产出），业务线持续推出。任何具备 API / MCP / CLI 可编程面的工程软件，可按规范接入并随时替换。

## 架构

```
               ┌───────────────── 共享上游 ─────────────────┐
               │   概念图 → 定妆图 → 部件语义拆分 → 动作语义字典  │
               └────────────────────┬────────────────────────┘
                                    │ 分界点：定妆图之后分叉
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
      Skin 预设                Pixel 预设               Chibi 预设
   Live2D 模型包              sprite / 图集             GIF / sprite sheet / JSON
          └────────────── 业务线为预设选项，持续推出 ─────────────┘
```

每条业务线 = 环节流水线 + Agent 通道 + 人工审核门；各线以预设形式落档，新增业务线时按同一结构登记入口与出口。

## 项目结构

```
asset-workbench/
├── README.md
├── assets/
│   └── icon.png                       # 项目概念图标
├── docs/
│   ├── model-map.md                   # 模型能力地图与定妆环节选型调优
│   └── 软件接入Skill生成规范-v0.1.md  # 半开放软件接入规范
├── presets/
│   ├── Skin预设-规格v0.3.md
│   ├── Pixel预设-走查v0.1.md
│   └── Skin-Agent-预设运行定义v0.1.md
└── skills/
    └── connector-skill-builder/       # 软件接入 Skill 生成器
```

## 业务线（预设选项 · 持续扩展）

当前内置 Skin / Pixel / Chibi 三套预设风格；它们是众多美术资源风格类型中的三种，后续可扩展其他类型。各预设模拟正常工作步骤（概念 → 定妆 → 部件拆分 → 动作字典 → 分叉产出）。

| 线 | 资产品类 | 出口 | 落档 |
|---|---|---|---|
| Skin 预设（虚拟形象风格） | Live2D 角色模型 | .model3/.moc3/.physics3/.motion3 | 规格 v0.3 |
| Pixel 预设（像素美术风格） | 像素游戏素材 | sprite / 图集 | 走查 v0.1 |
| Chibi 预设（Q 版萌系风格） | Q 版形象 / 循环动画 | GIF / sprite sheet / JSON | 工具调研完成 |

各线环节规格见 [presets/](presets/) 文档。

## 半开放软件接入

```
软件可编程面（API / MCP / CLI / SDK）
        ↓
   探测 → 映射 → 生成 → 验证 → 登记
        ↓
  路由主动选择 · 同能力接口软件可随时替换
```

- 门槛：MCP server / CLI / 本地服务 / SDK 脚本 API，任一命中
- 生成器：connector-skill-builder（探测 → 映射 → 生成 → 验证 → 登记）
- 能力接口：3D 建模 / 绑定 / 导出 / 拆层 / 绑参 / 像素帧 / 渲染回传
- 实例：Blender（3D 建模 / 绑定 / 导出 / 渲染回传，socket 直连 127.0.0.1:9876，2026-10-02 已验证）

规范：[docs/软件接入Skill生成规范-v0.1.md](docs/软件接入Skill生成规范-v0.1.md)

## 模型能力地图（E1 选型调优）

主流生图模型按内容类型划分（二次元 / 写实 / 像素 / 国风 / 特定画风），配定妆环节的选型路由与调优流程。详见 [docs/model-map.md](docs/model-map.md)。

## 文档导航

| 文档 | 内容 |
|---|---|
| [presets/Skin预设-规格v0.3.md](presets/Skin预设-规格v0.3.md) | Skin 预设各环节规格（概念→定妆→拆层→字典→分叉产出）、四层契约、拆层环节 API 清单、路由、输出契约、单点测试计划 |
| [presets/Pixel预设-走查v0.1.md](presets/Pixel预设-走查v0.1.md) | Pixel 预设环节走查、六风险、与 Skin 预设对称/差异 |
| [presets/Skin-Agent-预设运行定义v0.1.md](presets/Skin-Agent-预设运行定义v0.1.md) | 六组件预设包、内核循环、会话协议、首单示例 |
| [docs/model-map.md](docs/model-map.md) | 模型能力地图与 E1 选型调优 |
| [docs/软件接入Skill生成规范-v0.1.md](docs/软件接入Skill生成规范-v0.1.md) | 半开放软件接入：门槛、四步生成流程、登记与可插拔、实例记录 |

## 状态

- 预设风格：Skin（规格 v0.3）、Pixel（走查 v0.1）已落档；Chibi（Q 版萌系，工具调研完成）持续扩展中
- 单点测试计划：台阶 0 魔搭在线拆层试跑 → 台阶 1 本地部署 → 拆层环节 CSV 验证 → GUI 校准
- 半开放软件接入：Blender 实例已验证（socket 直连 9876），connector-skill-builder 生成器就绪（2026-10-02）
- 工作台外壳未动工

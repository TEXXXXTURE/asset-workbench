# 工具推荐清单（Tool Recipes）

> Reference for: connector-skill-builder
> Load when: 需要为业务线推荐现成工具、或在生成接入 Skill 前检索候选工具。

候选工具按固定格式登记。Agent 扩展工具集时先查本清单；清单外工具按同一格式追加，URL 必须指向官方仓库 / 官方文档。

## 条目格式

| 字段 | 内容 |
|---|---|
| 名称 | 工具名 |
| 来源 | 官方仓库 / 文档 URL |
| 用途 | 一句话功能与产出 |
| 可编程面 | 通道类型（MCP / CLI / 本地服务 / SDK / 脚本层） |
| 接入要点 | 密钥、环境依赖、专属机制说明 |
| 与工作台关系 | 对应业务线 / 能力接口 / 上下游衔接 |
| 状态 | 已验证 / 待验证 / 参考 |

## 条目

### image-blaster

| 字段 | 内容 |
|---|---|
| 名称 | image-blaster |
| 来源 | https://github.com/neilsonnn/image-blaster |
| 用途 | 单张图 → 3D 世界管线：动态物体网格（.glb/.obj，Hunyuan 3D / Meshy）+ 静态环境高斯泼溅（.spz，World Labs Marble）+ 环境/物体音效（.mp3，ElevenLabs SFX），约 5 分钟 |
| 可编程面 | Claude Code skill 包 + mjs 脚本执行层（FAL / World Labs 云 API） |
| 接入要点 | 密钥 `WORLD_LABS_API_KEY` + `FAL_KEY`（音效经 FAL，无需单独 ElevenLabs key）；bun / node 运行；依赖 Claude Code 专属 agent(fork)/allowed-tools 机制，迁移至其他 Agent 环境需改造 |
| 与工作台关系 | 「图像 → 3D 世界化」业务线候选；产出 Blender-ready（.glb/.obj），可接已验证的 Blender 通道作下游精修 |
| 状态 | 待验证（需密钥与环境改造） |

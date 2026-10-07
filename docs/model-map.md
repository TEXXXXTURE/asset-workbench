# 模型能力地图与定妆环节选型调优

模型选型是 E1 定妆环节的风格路由调优。初始形象满意后，后续制作是固定工作；生图质感需要反复抽卡，E1 是全线的质感闸门。

## 模型能力地图

| 内容类型 | 首选底模 | 擅长依据 | 部署 |
|---|---|---|---|
| 二次元动漫（皮套主路线） | Z-Image 系 / Illustrious XL / NoobAI-XL | Z-Image 原生二次元强（动漫、漫画、像素多能，魔搭生态活跃）；Illustrious 角色特征精准、LoRA 训练首选；NoobAI 角色知识最深、与 Illustrious 共享生态 | 魔搭 / 创空间 / 本地 SDXL 8-12GB |
| 写实 / 照片级 | FLUX 2 Pro / RealVisXL / Juggernaut XL | FLUX 材质物理最接近摄影；RealVisXL 自然肤色、真实光影；Juggernaut 全能写实 | 云端 API / 本地 |
| 风格化 / 半写实全能 | Pony V6 XL / DreamShaper XL | Pony LoRA 库最大、风格化与混合风格强；DreamShaper 半写实全能 | 本地 |
| 国风 / 带文字 | Qwen-Image 系 | 风格信号保留强，国风优先，带文字海报 | 魔搭 |
| 像素 | Z-Image 像素能力 / 像素 LoRA | Z-Image 原生像素 art；SeaArt Chibi Pixel 等 LoRA | 魔搭 / 本地 |
| 特定画风（水彩/漫画/霓虹） | Krea-2 等风格 LoRA 集 | kidsdrawing、softwatercolor、retroanime 等一键风格 | 魔搭 |

## 核心规律

- 底模决定"能画什么"，LoRA 决定"是什么画风"
- Pony 与 Illustrious/NoobAI 是两个不互通的 LoRA 生态，选底模前先定生态

## 定妆环节调优机制

四件套：

1. 模型资产登记：model 品类记录模型名、底模、触发词、LoRA 权重、风格、部署与健康度
2. 选型路由：内容特征 → 底模族 → 具体模型 → LoRA 挂载
3. 抽卡协议：固定 prompt × N 个 seed 批量出图，人筛选，记录选中的模型＋参数＋seed
4. 反馈闭环：选中记录 → 偏好分/健康度 → 更新路由权重 → 下次自动优先命中

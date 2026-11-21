# Awesome AI（中文版）

> 把 GitHub 上 8000+ Star 的 AI 开源项目整理成中文：**它是什么、能干什么、上手难不难**。
> 
> 收录 **781** 个项目，其中 **130** 个已写中文解析。数据抓取自 GitHub Search API，更新于 2026-11-21。
> 
> 在线浏览（带搜索和筛选）：https://zhishi.us.ci/ai-list/

难度标记：🟢 易 = 装上就能用 · 🟡 中 = 要会点命令行或配置 · 🔴 难 = 要懂原理或自己部署运维

## 目录

1. [智能体 Agent](#智能体-Agent)（40）
2. [对话助手](#对话助手)（18）
3. [编程开发](#编程开发)（23）
4. [模型与推理](#模型与推理)（14）
5. [RAG 知识库](#RAG-知识库)（6）
6. [图像生成](#图像生成)（5）
7. [视频生成](#视频生成)（1）
8. [语音音频](#语音音频)（5）
9. [自动化工作流](#自动化工作流)（5）
11. [学习教程](#学习教程)（9）
13. [其他](#其他)（4）

---

## 智能体 Agent

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [morluto/rea](https://github.com/morluto/rea) | 用智能体逆向分析任意软件，从应用行为一路拆到二进制，安全研究与竞品分析用。 | 471,718 | 🔴难 |
| [obra/superpowers](https://github.com/obra/superpowers) | 把软件开发方法论固化成技能框架，让 AI 编程助手按流程干活而不是乱改。 | 322,956 | 🟡中 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | AI 代理运行时优化系统，统管技能、记忆、权限和资源，重度 agent 用户才需要。 | 307,939 | 🔴难 |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | DeepSeek 官方智能体框架，一切皆插件，用来搭自己的 agent 运行时。 | 284,774 | 🔴难 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 最早爆火的全自动智能体，给个目标自己拆任务执行，学 agent 架构必读。 | 188,120 | 🟡中 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 一整套“AI 员工”角色库：前端、运营、社区，拉进 agent 就组成虚拟团队。 | 169,579 | 🟢易 |
| [langgenius/dify](https://github.com/langgenius/dify) | 开源 LLM 应用开发平台，可视化编排 agent/RAG/工作流，可私有化部署。 | 161,593 | 🟢易 |
| [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 国内最全的 Java 后端与面试体系指南，含 AI 应用开发章节。 | 159,631 | 🟢易 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 100+ 可直接跑的 agent / RAG 应用代码合集，抄架构最快的地方。 | 145,233 | 🟢易 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 多智能体量化交易框架：研究员/交易员/风控角色协作出交易决策。 | 123,315 | 🔴难 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 让 AI 直接操作浏览器：填表、抓数据、走流程，Python 几行接入。 | 121,633 | 🟢易 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 给 agent 加跨会话持久记忆，自动记录并召回它干过的事。 | 118,693 | 🟢易 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 开源多 agent 工作台，公司在统一入口里管理一堆 agent。 | 115,529 | 🟡中 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 让 agent“看见整个互联网”：读推特、Reddit、YouTube、GitHub 并能搜索。 | 113,608 | 🟡中 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 谷歌官方终端 AI agent，Gemini 能力直接进命令行。 | 108,956 | 🟢易 |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 让 AI agent 自己在单卡上跑训练实验、自动找更优配置。 | 100,341 | 🔴难 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP 服务器大全，给 Claude/Cursor 接各种工具，找现成能力先看这里。 | 98,334 | 🟢易 |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 实时全球情报看板：新闻聚合 + 地缘监测，开源可自建。 | 91,002 | 🟢易 |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 中文《从零开始构建智能体》教程，原理+代码，国内学 agent 最顺。 | 87,526 | 🟢易 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 字节开源的长任务 SuperAgent 框架，会研究、写代码、出报告。 | 85,561 | 🔴难 |
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 开源 AI 求职 agent：扫招聘站、按匹配度打分、自动投递。 | 83,973 | 🟢易 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | agent 编排框架，多智能体集群协同干活。 | 82,173 | 🔴难 |
| [netdata/netdata](https://github.com/netdata/netdata) | 全栈实时监控：指标、日志、链路、拓扑，一台机器就能跑。 | 81,561 | 🟢易 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 用一个 bash 文件从 0 复刻 Claude Code 式 agent harness，理解 agent 最快。 | 80,687 | 🟡中 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 微软 18 课 AI Agent 入门，带示例代码。 | 80,647 | 🟢易 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude 技能合集，装一批现成能力。 | 79,964 | 🟢易 |
| [usestrix/strix](https://github.com/usestrix/strix) | 开源 AI 渗透测试工具，自动找漏洞并给修复建议。 | 76,841 | 🔴难 |
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | 开源金融数据平台，量化研究和 AI 分析的数据底座。 | 75,608 | 🟡中 |
| [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | 现代前端开发检查清单，人和 AI 都能照着过一遍。 | 74,787 | 🟢易 |
| [blader/humanizer](https://github.com/blader/humanizer) | 去掉文字里的 AI 味，让输出像人写的。 | 71,717 | 🟢易 |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 让 agent 跨 Reddit/X/YouTube/HN 调研任意话题近 30 天动态。 | 71,544 | 🟢易 |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 多智能体软件公司：产品经理/架构/开发角色协作出代码。 | 71,370 | 🟡中 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 给 agent 加记忆层，即插即用，跨会话记住用户偏好。 | 69,291 | 🟢易 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Claude Code 从 vibe coding 到工程化的最佳实践合集。 | 69,273 | 🟢易 |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 私有化 AI 工作台：文档问答 + agent，桌面可装，数据本地。 | 68,473 | 🟢易 |
| [upstash/context7](https://github.com/upstash/context7) | 给 agent 提供最新版本文档，解决模型知识过时和 API 记错。 | 65,201 | 🟢易 |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 多平台热点聚合 + 舆情监测，RSS 加智能提醒，自媒体选题用。 | 63,761 | 🟢易 |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 提供《深入理解 AI Agent》全书正文、PDF 与代码，帮助开发者快速掌握 AI 代理设计与实践，适合想系统学习的技术人员 | 58,943 | 🟢易 |
| [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) | 本地模型 API 层，支持 RAG、技能、工具、MCP、文本转 SQL 等功能，兼容任意 OpenAI 兼容推理服务器 | 57,644 | 🟡中 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | 让人类与 AI 代理协同工作，支持自托管与插件化，适合构建可扩展的多代理系统 | 56,968 | 🟡中 |

## 对话助手

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 号称“什么都能干”的跨平台 AI 助手，能直接操作电脑和系统。 | 394,934 | 🟡中 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Nous 出品的自进化智能体（就是我），自带工具、技能库和长期记忆。 | 265,027 | 🟡中 |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 社区最大的提示词库（原 Awesome ChatGPT Prompts），提示词可以直接抄。 | 178,074 | 🟢易 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 自建 ChatGPT 式界面，接 Ollama 或 OpenAI 兼容 API，带多人账号和知识库。 | 159,184 | 🟢易 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 拖拽式搭建 AI 工作流和 agent，低代码，适合快速做原型。 | 156,814 | 🟢易 |
| [github/spec-kit](https://github.com/github/spec-kit) | 规格驱动开发（SDD）工具包：先写规格再让 AI 编码，减少跑偏返工。 | 150,852 | 🟡中 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 最主流的 LLM 应用开发框架，链式编排、工具调用、RAG 全家桶。 | 149,986 | 🟡中 |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 微软 21 课生成式 AI 入门课，带代码，零基础系统学。 | 123,927 | 🟢易 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 开源的 AI 软件工程师，自己写代码、跑测试、提 PR。 | 93,932 | 🟡中 |
| [ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat) | 零配置 AI 聊天客户端，填 key 就能用，可一键部署。 | 88,980 | 🟢易 |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 本地跑 LLM 的桌面客户端，可商用，低配机器也能跑。 | 77,330 | 🟢易 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 规格驱动开发工具，让 AI 编码前先对齐需求文档。 | 75,364 | 🟡中 |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | ChatGPT/Claude/Gemini 系统提示词泄露合集，学大厂怎么调教。 | 72,255 | 🟢易 |
| [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 学术党神器：论文翻译润色、PDF 解析、插件化，国内高校常用。 | 71,708 | 🟢易 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 图工程 agent：一句话触发多 agent 编排。 | 71,034 | 🟡中 |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 用手机或任意电脑远程控制 Claude Code、Codex 的客户端。 | 68,153 | 🟢易 |
| [xtekky/gpt4free](https://github.com/xtekky/gpt4free) | 白嫖各家模型的逆向接口集合，稳定性看运气，商用别碰。 | 67,090 | 🟡中 |
| [tw93/Pake](https://github.com/tw93/Pake) | 一条命令把网页打包成轻量桌面应用（Rust + Tauri）。 | 63,883 | 🟢易 |

## 编程开发

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 一个 CLAUDE.md 文件把 Karpathy 的编程习惯喂给 Claude Code，改代码风格最省事的办法。 | 234,783 | 🟢易 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 给 AI 代理装上“懒资深工程师”的大脑：能不写的代码就不写，专治过度设计。 | 195,739 | 🟢易 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 给 AI 编程助手补 UI/UX 设计能力的技能包，出的界面不再一眼 AI 味。 | 152,219 | 🟢易 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Cursor、Devin、Claude Code 等 AI 工具的完整系统提示词泄露合集，学提示词工程看这个。 | 144,796 | 🟢易 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 复制即用的 React 组件库，AI 生成界面的默认底座。 | 128,656 | 🟢易 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | 统一 LLM API + agent 循环 + 终端编码助手，一条工具链全包。 | 123,096 | 🟡中 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 让编码 agent 少说废话少烧 token 的本地代理+技能，答案短但够用。 | 121,815 | 🟢易 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Google 工程师出品的生产级编码技能集，给 agent 补工程规范。 | 119,426 | 🟢易 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 给编码 agent 审美：美术方向、参考图、浏览器截图对比。 | 119,412 | 🟢易 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 给编码 agent 的设计词汇表，用 polish/bolder 这类指令精确调界面。 | 114,142 | 🟢易 |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 本地优先的 AI 设计协作工作台，出动态图和原型。 | 108,722 | 🟡中 |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 把一个想法或代码库画成交互式架构图，写方案配图神器。 | 98,392 | 🟢易 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 把代码变成可交互知识图谱，用来快速读懂陌生项目。 | 93,464 | 🟡中 |
| [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 免费 MIT 的 AI 网关：一个端点接 375 家供应商、1400+ 模型。 | 89,229 | 🟢易 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Rust 写的命令行代理，把 LLM token 消耗压掉 60-90%，省钱利器。 | 87,318 | 🟢易 |
| [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | 计算机科学公开课视频清单，按科目索引。 | 84,900 | 🟢易 |
| [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | 开源 agent 视频生产系统，12 条流水线覆盖剪辑、配音、成片。 | 81,980 | 🟡中 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 把工具输出、日志、RAG 片段先压缩再喂模型，省 20% token。 | 80,223 | 🟢易 |
| [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 在本地跑的 AI 求职框架，基于 Claude Code 自动改简历、投岗位。 | 72,856 | 🟡中 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | 安全弹性地运行 AI 生成的代码，沙箱基础设施。 | 71,306 | 🔴难 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 基于 CSS 的 Anti‑AI‑slop 设计工具，提升 Claude Code、Cursor、Codex 等 AI 代码助手的输出质量与可读性 | 58,691 | 🟢易 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 精选 Claude Code 资源与最佳实践，帮助开发者高效使用 Anthropic 的 AI 编程助手，适合想提升代码生成质量的团队 | 58,476 | 🟢易 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 将 AI 代理转化为科学家，提供 177+ 已验证技能和 100+ 科学数据库，适合科研人员快速构建实验助手 | 57,956 | 🟡中 |

## 模型与推理

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | 一条命令在本机跑 Qwen/DeepSeek/Llama 等开源模型，本地部署的默认入口。 | 187,782 | 🟢易 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | AI 模型定义的事实标准库，几乎所有开源模型都从这里加载。 | 169,334 | 🟡中 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 节点式扩散模型工作流，出图/视频/换脸全能，比 WebUI 灵活但学习曲线陡。 | 147,863 | 🟡中 |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 手写 GPT：用 PyTorch 从零实现大模型，理解原理最好的一本书。 | 108,725 | 🔴难 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | 深度学习第一框架，研究和训练默认选它。 | 105,758 | 🔴难 |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 高吞吐 LLM 推理引擎，PagedAttention 省显存翻倍吞吐，生产部署标配。 | 97,290 | 🔴难 |
| [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | 插件形式免 key 用前沿模型（DeepSeek/Kimi），只适合折腾党。 | 82,291 | 🟡中 |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 100+ LLM/VLM 统一微调框架，LoRA、全参、DPO 都支持，带 WebUI。 | 76,166 | 🟡中 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 国产 LLM 多市场股票分析系统：行情+新闻+看板+推送，可零成本定时跑。 | 73,580 | 🟢易 |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 两小时从零训出 64M 小模型，最低成本理解 LLM 训练全流程。 | 67,780 | 🟡中 |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 60+ 深度学习论文逐行实现加注释，学论文最快。 | 67,779 | 🔴难 |
| [keras-team/keras](https://github.com/keras-team/keras) | 高层深度学习 API，上手最快，教学和原型首选。 | 64,445 | 🟡中 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 一个接口调 100+ 家 LLM，统一 OpenAI 格式，多模型路由标准件。 | 63,633 | 🟢易 |
| [ultralytics/yolov5](https://github.com/ultralytics/yolov5) | PyTorch 实现的 YOLOv5，支持目标检测、实例分割、分类训练与模型导出，适合需要视觉模型快速部署的工程师 | 58,290 | 🟢易 |

## RAG 知识库

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 把代码库+文档+SQL+PDF 变成可查询知识图谱，做代码库问答很省事。 | 151,258 | 🟡中 |
| [supabase/supabase](https://github.com/supabase/supabase) | 开源 Firebase 替代：Postgres+认证+存储+实时，做 AI 应用后端最省事。 | 115,208 | 🟡中 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 深度文档理解的 RAG 引擎，PDF/表格切分质量高，适合企业知识库。 | 94,491 | 🟡中 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 百度开源 OCR 之王，PDF/图片转结构化数据，中文识别最稳。 | 92,958 | 🟢易 |
| [docling-project/docling](https://github.com/docling-project/docling) | 文档解析成结构化数据喂给 GenAI，PDF/Word/PPT 都能拆。 | 70,831 | 🟢易 |
| [pathwaycom/serviette](https://github.com/pathwaycom/serviette) | 无代码 RAG 服务器，支持 8 种向量数据库，便于快速构建文档检索与问答系统，适合业务快速落地 | 58,696 | 🟡中 |

## 图像生成

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 最经典的 SD 绘图 WebUI，插件生态最大，出图和训 LoRA 都靠它。 | 165,367 | 🟢易 |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | 一张图实时换脸 + 视频 deepfake，你本机已装 DirectML 版。 | 98,505 | 🟡中 |
| [opencv/opencv](https://github.com/opencv/opencv) | 计算机视觉基础库，图像和视频处理绕不开。 | 91,663 | 🟡中 |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 本地微调 LLM 和扩散模型的最快方案，显存省一半，带 UI。 | 79,862 | 🟡中 |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 浏览器里的间谍卫星模拟器，接真实开源卫星数据。 | 66,147 | 🟢易 |

## 视频生成

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 开源 AI 视频编辑器，用文字描述改视频，剪辑可回溯。 | 87,539 | 🟡中 |

## 语音音频

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 完全本地的 ElevenLabs 替代：声音克隆、配音、语音设计，数据不出机器。 | 115,528 | 🟡中 |
| [fighting41love/funNLP](https://github.com/fighting41love/funNLP) | 中文 NLP 资源大全：敏感词、实体抽取、词库，中文文本处理必备。 | 84,703 | 🟢易 |
| [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 开源 Notion 替代（本地优先），团队 wiki + 项目管理。 | 79,282 | 🟢易 |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | AI 把文档或主题变成原生 PPT，形状和动画都可编辑。 | 78,912 | 🟢易 |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 开源语音 AI，提供高保真语音合成与识别，适合需要自研语音交互的产品 | 57,403 | 🟡中 |

## 自动化工作流

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 可视化工作流自动化平台，内置 AI 节点、能连 400+ 应用，国内自建自动化首选。 | 211,561 | 🟢易 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 把任意网页抓成干净的 Markdown/结构化数据喂给 AI，爬虫+搜索一体。 | 205,460 | 🟢易 |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 国产一键短视频生成：给主题就出文案+配音+素材+字幕成片。 | 144,856 | 🟢易 |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 现代爬虫框架，从单请求到大规模抓取自适应，反爬友好。 | 104,693 | 🟡中 |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 专为 AI 设计的爬虫，直接输出干净 Markdown，自带提取和搜索 API。 | 87,615 | 🟢易 |

## 学习教程

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 谷歌深度学习框架，工业部署生态成熟，新项目大多已转 PyTorch。 | 201,667 | 🔴难 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | LLM 学习路线图 + Colab 笔记本，从基础到微调一条龙。 | 85,170 | 🟡中 |
| [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) | 《动手学深度学习》中文版，代码可运行，国内外 500+ 高校在用。 | 82,622 | 🟡中 |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 提示词工程权威指南，含论文、笔记和 notebook。 | 80,247 | 🟢易 |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | AI 工程从零到上线的学习路径。 | 79,704 | 🟢易 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI 官方 API 示例与最佳实践，接 API 先看这个。 | 77,254 | 🟢易 |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 微软 12 周 24 课 AI 入门，非技术也能跟。 | 71,056 | 🟢易 |
| [byoungd/up](https://github.com/byoungd/up) | 《人生进阶指南》中英双语，AI 时代的学习、创业、财富笔记。 | 70,764 | 🟢易 |
| [deepfakes/faceswap](https://github.com/deepfakes/faceswap) | 面部替换软件，支持多种模型与高质量合成，适合研究与创意项目的视觉实验 | 57,625 | 🔴难 |

## 其他

| 项目 | 说明 | Stars | 难度 |
|---|---|---|---|
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek 开源的 MoE 大模型权重与推理代码，671B 级别。 | 104,882 | 🔴难 |
| [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus) | 自托管的 AI 工作台，聊天/工具/知识库一体，替代云端订阅。 | 95,873 | 🟡中 |
| [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | DeepSeek 推理模型 R1 的开源权重，长链思考，数学和代码强。 | 92,053 | 🔴难 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | AI 对冲基金团队：多个投资风格 agent 分工做投研。 | 64,780 | 🔴难 |

---

## 关于收录标准

- 只收 Star ≥ 8000 的仓库，靠 Star 和近半年活跃度一起看
- 「说明」是编辑写的一句话，不是官方描述的翻译
- 难度是**上手成本**，不代表项目好坏

## 声明

每个项目的版权归其作者所有，本项目只做索引和中文说明，不包含任何项目的源码分发。
说明文字为原创整理，欢迎转载注明出处。

## 更新

```bash
python scripts/fetch.py   # 重新抓取，覆盖 data/repos.json
```

## License

MIT（索引与说明文字部分）

# 第二课作业

基础作业 - 完成下面两个作业

1. 在茴香豆 Web 版中创建自己领域的知识问答助手

参考视频零编程玩转大模型，学习茴香豆部署群聊助手

完成不少于 400 字的笔记 + 线上茴香豆助手对话截图(不少于5轮)

（可选）参考 代码 在自己的服务器部署茴香豆 Web 版

2. 在 InternLM Studio 上部署茴香豆技术助手

根据教程文档搭建 茴香豆技术助手，针对问题"茴香豆怎么部署到微信群？"进行提问

完成不少于 400 字的笔记 + 截图

进阶作业 - 二选一

A.【应用方向】 结合自己擅长的领域知识（游戏、法律、电子等）、专业背景，搭建个人工作助手或者垂直领域问答助手，参考茴香豆官方文档，部署到下列任一平台。
飞书、微信

可以使用 茴香豆 Web 版 或 InternLM Studio 云端服务器部署

涵盖部署全过程的作业报告和个人助手问答截图

B.【算法方向】尝试修改 good_questions.json、调试 prompt 或应用其他 NLP 技术，如其他 chunk 方法，提高个人工作助手的表现。

完成不少于 400 字的笔记 ，记录自己的尝试和调试思路，涵盖全过程和改进效果截图

大作业项目选题

A.【工程方向】 参与贡献茴香豆前端，将茴香豆助手部署到下列平台

Github issue、Discord、钉钉、X

B.【应用方向】 茴香豆RAG-Agent

应用茴香豆建立一个 ROS2 的机器人Agent

C.【算法方向】 茴香豆多模态

参与茴香豆多模态的工作

# walkthrough

*the following program executed under the directory `lesson3/` with conda env activated*

*program may not be compatible if running with cpu*

## preparation

1. device

System: Ubuntu 22.04.4 LTS

CPU: Intel(R) Xeon(R) W-2295 CPU @ 3.00GHz

GPU: NVIDIA GeForce RTX 3090

(mac is overwhelmed!)

![](images/mac.png)

2. code repo preparation

```bash
git clone https://github.com/internlm/huixiangdou && cd huixiangdou
git checkout 447c6f7e68a1657fce1c4f7c740ea1700bde0440
cd ..
```

3. env preparation

```bash
### create env
conda create -n l3 python=3.10 -y
conda activate l3
### if cuda available
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
### if cuda not available, not fully tested
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 -c pytorch
### install packages
pip install protobuf==4.25.3 accelerate==0.28.0 aiohttp==3.9.3 auto-gptq==0.7.1 bcembedding==0.1.3 beautifulsoup4==4.8.2 einops==0.7.0 faiss-gpu==1.7.2 langchain==0.1.14 loguru==0.7.2 lxml_html_clean==0.1.0 openai==1.16.1 openpyxl==3.1.2 pandas==2.2.1 pydantic==2.6.4 pymupdf==1.24.1 python-docx==1.1.0 pytoml==0.1.21 readability-lxml==0.8.1 redis==5.0.3 requests==2.31.0 scikit-learn==1.4.1.post1 sentence_transformers==2.2.2 textract==1.6.5 tiktoken==0.6.0 transformers==4.39.3 transformers_stream_generator==0.0.5 unstructured==0.11.2
```

4. model weight download

run `python model_download.py` modified from the [tutorial](https://github.com/InternLM/Tutorial/blob/camp2/helloworld/hello_world.md#22-%E4%B8%8B%E8%BD%BD-internlm2-chat-18b-%E6%A8%A1%E5%9E%8B) to download weights for models `internlm2-chat-1.8b`, `internlm2-chat-7b`, `internlm-xcomposer2-7b`, `internlm-xcomposer2-vl-7b`.

search models needed in [modelscope](https://modelscope.cn/models)

![]()

## basic part

### 1. my huixiangdou web app

1. wechat group deployment

2. online huixiangdou

3. self-hosted server

### 2. huixiangdou on InternLM Studio

just check

![](images/how_to_deploy.png)

## advanced part
### [application] `huixiangdou-math` for my high school teachers!


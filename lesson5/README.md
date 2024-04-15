# 第五节课作业（请交到第5节课）

## 基础作业（结营必做）

完成以下任务，并将实现过程记录截图：

- 配置 LMDeploy 运行环境
- 以命令行方式与 InternLM2-Chat-1.8B 模型对话

## 进阶作业

完成以下任务，并将实现过程记录截图：

- 设置KV Cache最大占用比例为0.4，开启W4A16量化，以命令行方式与模型对话。（优秀学员必做）
- 以API Server方式启动 lmdeploy，开启 W4A16量化，调整KV Cache的占用比例为0.4，分别使用命令行客户端与Gradio网页客户端与模型对话。（优秀学员）
- 使用W4A16量化，调整KV Cache的占用比例为0.4，使用Python代码集成的方式运行internlm2-chat-1.8b模型。（优秀学员必做）
- 使用 LMDeploy 运行视觉多模态大模型 llava gradio demo （优秀学员必做）
- 将 LMDeploy Web Demo 部署到 [OpenXLab](https://github.com/InternLM/Tutorial/tree/camp2/tools/openxlab-deploy) （OpenXLab cuda 12.2 的镜像还没有 ready，可先跳过，一周之后再来做）


# walkthrough

## basic part

### 1. config LMDeploy

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#1lmdeploy%E7%8E%AF%E5%A2%83%E9%83%A8%E7%BD%B2

studio

local

### 2, chat with InternLM2-Chat-1.8B through command line

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#2lmdeploy%E6%A8%A1%E5%9E%8B%E5%AF%B9%E8%AF%9Dchat

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#24-%E4%BD%BF%E7%94%A8lmdeploy%E4%B8%8E%E6%A8%A1%E5%9E%8B%E5%AF%B9%E8%AF%9D

## advanced part

### 1. KV Cache 0.4, W4A16 quantization, chat through command line

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#3lmdeploy%E6%A8%A1%E5%9E%8B%E9%87%8F%E5%8C%96lite

### 2. LMDeploy with API Server, KV Cache 0.4, W4A16 quantization, chat through command line and gradio

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#3lmdeploy%E6%A8%A1%E5%9E%8B%E9%87%8F%E5%8C%96lite

### 3. KV Cache 0.4, W4A16 quantization, chat through coding

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#2lmdeploy%E6%A8%A1%E5%9E%8B%E5%AF%B9%E8%AF%9Dchat

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#5python%E4%BB%A3%E7%A0%81%E9%9B%86%E6%88%90

### 4. llava gradio demo with LMDeploy

https://github.com/InternLM/Tutorial/blob/camp2/lmdeploy/README.md#61-%E4%BD%BF%E7%94%A8lmdeploy%E8%BF%90%E8%A1%8C%E8%A7%86%E8%A7%89%E5%A4%9A%E6%A8%A1%E6%80%81%E5%A4%A7%E6%A8%A1%E5%9E%8Bllava

### 5. LMDeploy Web Demo on OpenXLab

https://github.com/InternLM/Tutorial/tree/camp2/tools/openxlab-deploy

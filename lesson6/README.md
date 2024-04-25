# 作业
Tip

结营必做基础作业；优秀学员或进入对应 SIG 需完成进阶作业。

基础作业

完成 Lagent Web Demo 使用，并在作业中上传截图。文档可见 Lagent Web Demo

完成 AgentLego 直接使用部分，并在作业中上传截图。文档可见 直接使用 AgentLego。

进阶作业

完成 AgentLego WebUI 使用，并在作业中上传截图。文档可见 AgentLego WebUI。

使用 Lagent 或 AgentLego 实现自定义工具并完成调用，并在作业中上传截图。文档可见：

用 Lagent 自定义工具

用 AgentLego 自定义工具

大作业选题

算法方向

在 Lagent 或 AgentLego 中实现 RAG 工具，实现智能体与知识库的交互。

基于 Lagent 或 AgentLego 实现工具的多轮调用，完成复杂任务。如：智能体调用翻译工具，再调用搜索工具，最后调用生成工具，完成一个完整的任务。

...

应用方向

基于 Lagent 或 AgentLego 实现一个客服智能体，帮助用户解决问题。

基于 Lagent 或 AgentLego 实现一个智能体，实现艺术创作，如生成图片、视频、音乐等。

...

# Walkthrough

## basic part

**env preparation**

```bash
mkdir -p /root/agent
studio-conda -t agent -o pytorch-2.1.2
cd /root/agent
conda activate agent
git clone https://gitee.com/internlm/lagent.git
cd lagent && git checkout 581d9fb && pip install -e . && cd ..
git clone https://gitee.com/internlm/agentlego.git
cd agentlego && git checkout 7769e0d && pip install -e . && cd ..
pip install lmdeploy==0.3.0
```

![](images/env.png)

**code preparation**

```bash
cd /root/agent
git clone -b camp2 https://gitee.com/internlm/Tutorial.git
```

![](images/code.png)

### 1. Lagent Web Demo

### 2. use AgentLego

## advanced part

### 1. AgentLego WebUI

### 2. customized Lagent and AgentLego
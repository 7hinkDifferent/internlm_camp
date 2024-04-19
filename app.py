import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

base_path = './internlm2-chat-1_8b-assistant'
os.system(f'git clone https://code.openxlab.org.cn/ThinkDifferent/internlm2-chat-1_8b-assistant.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')

tokenizer = AutoTokenizer.from_pretrained(base_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path, trust_remote_code=True, torch_dtype=torch.float32)

def chat(message,history):
    for response,history in model.stream_chat(tokenizer,message,history,max_length=2048,top_p=0.7,temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="InternLM2-Chat-1_8B-Assistant",
                description="""
InternLM is mainly developed by Shanghai AI Laboratory.  
                 """,
                 ).queue(1).launch()

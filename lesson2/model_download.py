import os
from modelscope.hub.snapshot_download import snapshot_download

# 创建保存模型目录
os.makedirs('models', exist_ok=True)

# save_dir是模型保存到本地的目录
save_dir='models'

model_cards = [
    ['Shanghai_AI_Laboratory/internlm2-chat-1_8b', 'v1.1.0'],
    ['Shanghai_AI_Laboratory/internlm2-chat-7b', 'v1.1.0'],
    ['Shanghai_AI_Laboratory/internlm-xcomposer2-7b', 'v1.0.0'],
    ['Shanghai_AI_Laboratory/internlm-xcomposer2-vl-7b', 'v1.0.0'],
    # ['Shanghai_AI_Laboratory/internlm-xcomposer2-7b-4bit', 'v1.0.0']
]

for model_id, revision in model_cards:
    print('downloading model...', model_id)
    snapshot_download(model_id=model_id, 
                      cache_dir=save_dir, 
                      revision=revision)
    print('downloaded model:', model_id)
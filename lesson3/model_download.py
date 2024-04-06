import os
from modelscope.hub.snapshot_download import snapshot_download

# 创建保存模型目录
os.makedirs('models', exist_ok=True)

# save_dir是模型保存到本地的目录
save_dir='models'

model_cards = [
    ['Shanghai_AI_Laboratory/internlm2-chat-7b', 'v1.1.0'],
    ['maidalun/bce-embedding-base_v1', None],
    ['maidalun/bce-reranker-base_v1', None]
]

for model_id, revision in model_cards:
    print('downloading model...', model_id)
    snapshot_download(model_id=model_id, 
                      cache_dir=save_dir, 
                      revision=revision)
    print('downloaded model:', model_id)
from huggingface_hub import hf_hub_download

# https://huggingface.co/internlm/internlm2-chat-7b/tree/main
hf_hub_download(repo_id='internlm/internlm2-chat-7b', filename='config.json', cache_dir='internlm2-chat-7b/cache')
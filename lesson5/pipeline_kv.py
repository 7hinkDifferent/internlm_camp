from lmdeploy import pipeline, TurbomindEngineConfig

backend_config = TurbomindEngineConfig(cache_max_entry_count=0.4)

pipe = pipeline('/root/models/internlm2-chat-1_8b-4bit',
                backend_config=backend_config)
response = pipe(['Hi, pls intro yourself', '上海是'])
print(response)
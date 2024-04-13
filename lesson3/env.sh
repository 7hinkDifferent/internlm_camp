export PYTHONUNBUFFERED=1
# Redis 的 IP 地址
export REDIS_HOST=10.1.52.22
# Redis 的密码
export REDIS_PASSWORD=${REDIS_PASSWORD}
# Redis 的端口，默认为 6379
export REDIS_PORT=6380
# JWT_SECRET 是指用于签名 JSON Web Token (JWT) 的密钥或密钥对，可以使用 `openssl rand -base64 32` 命令生成
export JWT_SECRET=${JWT_SEC}
# 茴香豆的后台服务端口，可以自定义
export SERVER_PORT=7860
# 飞书的 LARK_ENCRYPT_KEY，参考地址：https://open.larksuite.com/document/server-docs/event-subscription/event-subscription-configure-/request-url-configuration-case
# 如果不需要接通飞书忽略即可
export HUIXIANGDOU_LARK_ENCRYPT_KEY=thisiskey
export HUIXIANGDOU_LARK_VERIFY_TOKEN=sMzyjKi9vMlEhKCZOVtBMhhl8x23z0AG

# set your service endpoint(open to Internet callback from lark and wechat)
# 回调端口，建议填写 7860，然后将 7860 端口通过公网 IP 代理出去，例如 http://10.1.52.36:18443
export HUIXIANGDOU_MESSAGE_ENDPOINT=http://10.1.52.36:18443
# 如果使用 https 安全连接就把 COOKIE_SECURE 设置为 1；如果不是，则将 `export COOKIE_SECURE=1` 替换为 `unset COOKIE_SECURE`
export COOKIE_SECURE=1
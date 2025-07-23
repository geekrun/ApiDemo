# ApiDemo

一个基于 Flask 的简单云函数 Demo，支持通过 gunicorn 启动，适合云函数或容器化部署。

## 依赖

- Flask
- gunicorn

安装依赖：
```bash
pip install -r requirements.txt
```

## 启动方式

本地开发：
```bash
python main.py
```

生产部署（推荐）：
```bash
gunicorn -w 2 -b 0.0.0.0:5000 main:app
```

## API

### 1. 根接口 `/`
- 方法：GET
- 说明：返回 Hello, World! 及当前时间
- 示例响应：
```json
{"message": "Hello, World! Now: 2024-05-10T12:34:56.789012"}
```

### 2. 生成 Key `/gen_key`
- 方法：GET 或 POST
- 参数：`license`（string，必填）
- 说明：返回 license 的 md5 值
- 示例请求：
```bash
curl "http://localhost:5000/gen_key?license=test123"
```
- 示例响应：
```json
{"license": "test123", "key": "cc03e747a6afbbcbf8be7668acfebee5"}
```
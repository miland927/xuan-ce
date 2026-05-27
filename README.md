# 玄策

本项目为 `yijing-merged.html` 原型补充本地 FastAPI 后端。

## 启动后端

```powershell
cd D:\yiapp\yizhan
C:\Users\35538\AppData\Local\Programs\Python\Python312\python.exe -m uvicorn main:app --reload --port 8000
```

## 打开前端（推荐）

浏览器打开：

```text
http://127.0.0.1:8000/
```

也可以直接打开本地文件：

```text
file:///D:/yiapp/yizhan/yijing-merged.html
```

## 接口

- `GET /`：前端页面
- `GET /health`：服务健康检查
- `GET /daily`：今日卦，同一天结果固定
- `POST /bazi`：八字推算，参数示例 `{"year":1995,"month":8,"day":18,"hour":9}`
- `POST /gua`：起卦，参数示例 `{"method":"random"}`
- `GET /docs`：Swagger 文档

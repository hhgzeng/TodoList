# Todo List 应用

一个简洁的待办事项管理应用，采用前后端分离架构开发。

## 技术栈

### 前端
- Vue 3
- Vite
- Element Plus
- Pinia
- Axios

### 后端
- Django 4.2
- Django REST framework
- PostgreSQL
- Gunicorn

## 功能特点

- ✨ 简洁现代的用户界面
- 🌓 支持亮色/暗色主题切换
- ✅ 待办事项的增删改查
- 📱 响应式设计，支持移动端
- 🔄 实时状态同步
- 📊 任务完成进度统计

## 项目结构

```
Todo List/
├── todolist-frontend/     # 前端项目
│   ├── src/              # 源代码
│   ├── public/           # 静态资源
│   └── ...
└── todolist_backend/     # 后端项目
    ├── todolist/         # Django应用
    ├── manage.py
    └── ...
```

## 开始使用

### 前端部署
```bash
cd todolist-frontend
npm install
npm run dev
```

### 后端部署
```bash
cd todolist_backend
python -m venv env
source env/bin/activate  # Windows使用: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API 接口

- GET `/api/get-todo` - 获取所有待办事项
- POST `/api/add-todo` - 添加新待办事项
- POST `/api/update-todo/` - 更新待办事项状态
- POST `/api/del-todo/` - 删除待办事项

## 环境变量配置

### 前端 (.env.development)
```
VITE_API_BASE_URL=http://localhost:8000
```

### 后端
需要配置数据库连接等相关环境变量

## 开发团队

- 前端开发：[jing]
- 后端开发：[jing]

## License

MIT License

Copyright (c) [2025] [jing]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

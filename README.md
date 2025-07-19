# 甲骨文识别系统 - YOLOv8 + Flask 实现


## 项目概述

这是一个基于深度学习目标检测模型 YOLOv8 和 Flask Web 框架的甲骨文识别系统，用户可以通过简单上传甲骨文图片获取识别结果。项目实现了完整的图像处理流程，从上传、识别到结果展示的一站式体验。

**核心功能亮点**:
- 🖼️ 图像上传与处理系统
- 🧠 YOLOv8 甲骨文字符识别
- 🔍 检测结果可视化展示
- 📱 响应式Web界面设计
- ⚡ Flask高效后端服务


> *完整交互式演示：点击右上角Open in GitHub Codespaces按钮体验*

## 技术栈

| 组件 | 技术 |
|------|------|
| 核心算法 | **YOLOv8** (Ultralytics) |
| Web框架 | **Flask** (Python) |
| 图像处理 | **OpenCV**, **PIL** |
| 前端界面 | **HTML5**, **CSS3**, **JavaScript** |
| 部署方式 | Docker, Flask内置服务器 |

## 安装指南

### 本地运行

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/oracle-bone-recognition.git
cd oracle-bone-recognition

# 2. 安装依赖
pip install -r requirements.txt

# 3. 下载预训练模型 (约150MB)
wget https://example.com/models/oracle_yolov8.pt -P models/

# 4. 启动应用
python app.py

# 5. 访问应用
打开浏览器访问 http://localhost:5000
```

### Docker 部署
```bash
# 构建Docker镜像
docker build -t oracle-detection .

# 运行容器
docker run -p 5000:5000 oracle-detection
```

## 使用说明

1. 访问应用主页 (`http://localhost:5000`)
2. 点击"选择文件"按钮上传甲骨文图片
3. 支持格式: JPG, PNG
4. 点击"识别甲骨文"提交处理
5. 查看检测结果页面
   - 左侧: 原始图片
   - 右侧: 识别结果(带标注框)
6. 点击"返回首页"继续识别其他图片

## 项目结构

```
oracle-bone-recognition/
├── app.py                 # Flask主程序
├── Dockerfile             # 容器化部署配置
├── models/
│   └── oracle.pt   # 训练好的模型
├── templates/
│   ├── index.html         # 上传页面
│   └── result.html        # 结果展示页面
├── static/
│   ├── uploads/           # 用户上传图片存储
│   ├── results/           # 处理结果图片存储
│   └── demo.gif           # 项目演示动图
├── requirements.txt       # Python依赖列表
├── README.md              # 项目说明
└── .gitignore             # Git忽略规则
```

## 模型训练（可选）

如需训练自己的甲骨文识别模型：

```python
from ultralytics import YOLO

# 1. 加载基础模型
model = YOLO('yolov11n.pt')  # 使用nano版本

# 2. 训练配置
results = model.train(
    data='oracle_dataset.yaml',  # 数据集配置
    imgsz=640,                   # 图像尺寸
    epochs=100,                   # 训练轮数
    batch=8,                      # 批量大小
    optimizer='Adam',             # 优化器
    name='oracle_yolov8',         # 实验名称
    save_period=10                # 每10轮保存一次
)

# 3. 模型导出
model.export(format='onnx')  # 导出为ONNX格式
```

## 贡献指南

我们欢迎任何形式的贡献！以下是参与项目的方式：

1. **报告问题**:
   - 提交Issue描述遇到的问题

2. **功能请求**:
   - 提出改进建议或新功能想法

3. **代码贡献**:
   ```bash
   # 1. Fork仓库
   # 2. 创建功能分支
   git checkout -b feature/new-detection
   # 3. 提交修改
   git commit -m "添加新的甲骨文检测功能"
   # 4. 推送到Fork
   git push origin feature/new-detection
   # 5. 创建Pull Request
   ```

## 许可证

本项目采用 [MIT License](LICENSE)

## 技术交流

如有任何技术问题，欢迎：
- 在GitHub Issues区提问
- 发送邮件至：oracletech@example.com

---

**探索古代智慧，感受科技魅力**  
*让千年甲骨文遇见现代人工智能*

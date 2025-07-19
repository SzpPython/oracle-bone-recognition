项目结构
复制复制oracle-char-recognition/
├── app.py                 # Flask主程序
├── models/                # 存放YOLO模型
├── templates/             # HTML模板
├── static/                # 静态文件（CSS, JS, 图片）
├── requirements.txt       # Python依赖
├── Procfile               # Heroku部署配置文件
└── README.md
安装与运行
环境要求

Python 3.8+
CUDA 11.0+ (GPU加速，可选)

步骤


创建虚拟环境并激活

bashbash复制复制python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows

安装依赖

bashbash复制bash复制pip install -r requirements.txt

下载模型
由于模型文件较大，请从此链接下载，并放入models目录，命名为oracle_yolov8.pt。

或者，可以自己训练模型：
bashbash复制bash复制python train.py

运行Flask应用

bashbash复制bash复制python app.py

访问应用
打开浏览器访问：http://localhost:5000

部署到Heroku

注册Heroku账号并安装Heroku CLI
登录Heroku

bashbash复制bash复制heroku login

创建Heroku应用

bashbash复制bash复制heroku create your-app-name

部署代码

bashbash复制bash复制git push heroku master

打开应用

bashbash复制bash复制heroku open
使用说明

访问应用后，点击“上传图片”选择包含甲骨文的图片。
点击“识别甲骨文”按钮提交。
等待系统处理，稍后显示识别结果。

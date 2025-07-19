import os
import cv2
from flask import Flask, render_template, request, send_from_directory
from ultralytics import YOLO
from PIL import Image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# 确保目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# 加载训练好的模型
model = YOLO("models/best.pt")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # 保存原始文件
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(upload_path)

        # 处理图片
        result_filename = process_image(upload_path, file.filename)

        return render_template('result.html',
                               original=file.filename,
                               result=result_filename)


def process_image(image_path, filename):
    """使用YOLOv11进行甲骨文识别"""
    # 读取图片
    img = cv2.imread(image_path)

    # 运行YOLOv8推理
    results = model(img, conf=0.5)

    # 绘制检测结果
    annotated = results[0].plot(labels=True, boxes=True)

    # 转换颜色空间
    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    # 保存结果
    result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
    Image.fromarray(annotated).save(result_path)

    return filename


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
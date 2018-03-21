# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import server_coal_detector

__author__ = 'RTG Studio'


'''
安装依赖
Linux need to install libcm6
pip3 install flask
pip3 install requests  
pip3 install opencv-python
    
运行环境
Python 3.5.x
OpenCv 3.4

发送测试数据样例
curl -i -H "Content-Type:application/json" -X POST -d'{ "data": [ { "id": "camera-1", "rtsp": "video/01.mp4", "detect_x": 250, "detect_y": 240, "detect_width": 550, "detect_height": 60, "belt_y": 270, "belt_width": 400, "thresh":100 }, { "id": "camera-2", "rtsp": "video/02.mp4", "detect_x": 250, "detect_y": 400, "detect_width": 400, "detect_height": 30, "belt_y": 415, "belt_width": 450, "thresh":160 } ] }' http://127.0.0.1:10086/detector/init

curl -i -H "Content-Type:application/json" -X POST -d'{ "data": [ { "id": "camera-1", "rtsp": "video/01.mp4", "detect_x": 270, "detect_y": 240, "detect_width": 530, "detect_height": 60, "belt_y": 270, "belt_width": 400, "thresh":100 } ] }' http://127.0.0.1:10086/detector/init

curl -i -H "Content-Type:application/json" -X POST -d'{"data": [{"id": "camera-1", "rtsp": "video/NVR_ch10_main_20180201100001_20180201110002.dav", "detect_x": 350, "detect_y": 400, "detect_width": 1300, "detect_height": 120, "belt_y": 470, "belt_width": 1150, "thresh": 135}]}' http://127.0.0.1:10086/detector/init

curl -i -H "Content-Type:application/json" -X POST -d'{"data": [{"id": "camera-1", "rtsp": "video/NVR_ch10_main_20180201110002_20180201120001.dav", "detect_x": 350, "detect_y": 400, "detect_width": 1300, "detect_height": 120, "belt_y": 470, "belt_width": 1150, "thresh": 135}]}' http://127.0.0.1:10086/detector/init

停止当前的图像识别（不会停止后台服务）
curl http://host:port/detector/reset

@port： 视频检测服务运行端口
@return_data_api： 返回检测结果数据所要访问的API
@server_mode：False显示可视化窗口
            True仅在Terminal内输出（无桌面Linux需要设置为True）
            注：如果设置为False出现运行问题，请先设置为True进行测试
@offline：False发送结果至 return_data_api
        True仅在Terminal内输出
@host： 服务运行地址，默认为 127.0.0.1，可以设置为 0.0.0.0
'''

if __name__ == '__main__':
    server_coal_detector.run(port=10086,
                             return_data_api='http://127.0.0.1:10087/data',
                             server_mode=True,
                             offline=True)

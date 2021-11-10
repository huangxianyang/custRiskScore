# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 12:16 下午
# @Author  : HuangSir
# @FileName: main.py
# @Software: PyCharm
# @Desc: 启动服务

import uvicorn
from app import create_app
app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8005,
        debug=True,
        reload=False
    )
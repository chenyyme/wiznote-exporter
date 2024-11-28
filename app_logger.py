import logging
import os
from datetime import datetime


def init_logger(name='root'):
    """
    配置日志输出
    :return: 日志对象
    """
    # 创建日志器对象
    log = logging.getLogger(name)
    # 设置logger可输出日志级别范围
    log.setLevel(logging.DEBUG)
    # 设置格式并赋予handler
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    # 添加日志文件handler，用于输出日志到文件中
    log_file = f'wiznote-exporter_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    file_handler = logging.FileHandler(filename=os.path.join('logs', log_file), encoding='UTF-8')
    file_handler.setFormatter(formatter)

    # 控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 将handler添加到日志器中
    log.addHandler(file_handler)
    log.addHandler(console_handler)
    return log


logger = init_logger(__name__)

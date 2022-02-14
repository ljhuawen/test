# encoding = utf-8
import datetime
import logging


def getlog():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置logger日志等级

    # 如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        # 创建handler
        time_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S')
        log_file_name = "logs/{}.log".format(time_str)
        fh = logging.FileHandler(log_file_name, encoding="utf-8")
        ch = logging.StreamHandler()
        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s %(filename)s %(message)s",
            datefmt="%Y/%m/%d %X"
        )
        # 为handler指定输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


log = getlog()

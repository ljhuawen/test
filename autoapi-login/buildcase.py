# encoding = utf-8
from module.passport.createTestCaseFile import build
from common.Log import log

if __name__ == '__main__':
    log.info("=============开始构建测试用例=============")
    # build("pre")
    build("online")
    log.info("=============用例构建完毕=============")

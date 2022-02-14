# encoding = utf-8
from module.passport.passport import passport_online, passport_pre

if __name__ == '__main__':
    p = passport_online()
    # p = passport_pre()
    p.run_testcase()

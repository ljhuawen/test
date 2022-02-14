# encoding = utf-8
# app字典
app_mapping = {"WEB": "WEB", "生学堂": "SXT", "云平台": "XWCZ", "晓我课堂": "XWKT", "晓我课外": "XWKW", "晓我课堂平板": "MDM", "壹教云": "1N"}
# platform字典
platform_mapping = {"PC": "PC", "手机": "ANDROID", "微信": "WECHAT", "龙泉": "PC", "壹教云": "PC"}
# accountType字典
accountType_mapping = {"手机号": 0, "身份证号": 1, "用户名": 2, "手机验证码": 8, "龙泉登录": 9, "生学号": 10, "网阅临时账号": 7}
# userType字典
userType_mapping = {"学生": "1", "教师": "2", "家长": "3", "管理员": "5"}
# client字典
client_mapping = {"学生": "STUDENT", "教师": "TEACHER", "家长": "PARENTS", "管理员": "MANAGER"}
# 场景设计
changjing_list = ["正常", "错误密码", "账号为空", "密码为空", "账号过长", "密码过长", "已禁用的用户登录", "XSS", "黑名单"]
# 错误密码
wrong_passport = "1234567890123456"
# 长账号
long_account = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
# 长密码
long_password = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
# XSS
XSS_text = '''<script>alert('XSS');</script>'''
